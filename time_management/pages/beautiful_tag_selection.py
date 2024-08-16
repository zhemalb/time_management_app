import reflex as rx
import datetime
from sqlmodel import select

from ..database.models import Task, Tag, Status, Project, TagTaskLink
from ..utils.state.tasks import TaskState

from time_management.utils.state.base import State

chip_props = {
    "radius": "full",
    "variant": "surface",
    "size": "3",
    "cursor": "pointer",
    "style": {"_hover": {"opacity": 0.75}},
}


class BasicChipsState(TaskState):
    show_select: bool = False

    chosen_tags: list[str] = ["+"]
    available_tags: list[str] = []
    actions: list[str] = ["+"]

    statuses: list[Status] = []
    projects: list[Project] = []

    statuses_dict: dict[int, Status] = {}

    tag_name: str = ""
    tag_desc: str = ""

    status_name: str = ""
    status_color: str = "777777"
    status_urgency: int = 5

    project_name: str = ""
    project_desc: str = ""
    project_color: str = "#777777"
    project_tasks: list[Task] = []
    project_available_tasks: list[Task] = []

    selected_status: Status | None = None
    selected_project: Project | None = None

    actual_tasks_list: list[Task] = []
    nearst_tasks: int = 7

    chosen_project: Project | None = None

    def load_actual_tasks(self):
        if self.user is None:
            return

        self.initialize()

        with rx.session() as session:
            data = list(session.exec(
                select(Task).where(Task.user_id == self.user.id)
            ).all())

            nearst_tasks_timedelta = datetime.timedelta(days=self.nearst_tasks)
            zero_timedelta = datetime.timedelta(days=0)

            self.actual_tasks_list = [
                task for task in data
                if
                task.deadline is not None and (task.deadline - datetime.datetime.now()) <= nearst_tasks_timedelta and (
                        task.deadline - datetime.datetime.now()) >= zero_timedelta and not task.is_archive
            ]

        self.sort_actual_tasks()

    def load_long_terms_tasks(self):
        self.initialize()

        with rx.session() as session:
            data = list(session.exec(
                select(Task).where(Task.user_id == self.user.id)
            ).all())

            nearst_tasks_timedelta = datetime.timedelta(days=self.nearst_tasks)

            self.actual_tasks_list = [
                task for task in data
                if task.deadline is not None and (task.deadline - datetime.datetime.now()) > nearst_tasks_timedelta
            ]

        self.sort_actual_tasks()

    def load_bin(self):
        self.initialize()

        with rx.session() as session:
            data = list(session.exec(
                select(Task).where(Task.user_id == self.user.id)
            ).all())

            self.actual_tasks_list = data

        self.sort_actual_tasks()

    def load_delegable_tasks(self):
        self.initialize()

        with rx.session() as session:
            data = list(session.exec(
                select(Task).where(Task.user_id == self.user.id)
            ).all())

            self.actual_tasks_list = [
                task for task in data
                if task.is_deligable and not task.is_archive
            ]

        self.sort_actual_tasks()

    def load_postponed_tasks(self):
        self.initialize()

        with rx.session() as session:
            data = list(session.exec(
                select(Task).where(Task.user_id == self.user.id)
            ).all())

            self.actual_tasks_list = [
                task for task in data
                if task.deadline is None and not task.is_archive
            ]

        self.sort_actual_tasks()

    def load_archive_tasks(self):
        self.initialize()

        with rx.session() as session:
            data = list(session.exec(
                select(Task).where(Task.user_id == self.user.id)
            ).all())

            self.actual_tasks_list = [
                task for task in data
                if task.is_archive
            ]

        self.sort_actual_tasks()

    def load_complex_tasks(self):
        self.initialize()

        with rx.session() as session:
            data = list(session.exec(
                select(Task).where(Task.user_id == self.user.id)
            ).all())

            self.actual_tasks_list = [
                task for task in data
                if task.is_complex and not task.is_archive
            ]

        self.sort_actual_tasks()

    def change_status_open(self, value: bool):
        if not value:
            self.status_urgency, self.status_name, self.status_color = 5, "", "#777777"

    def initialize_project(self):
        self.project_name = ""
        self.project_desc = ""
        self.project_color = "#777777"

    def choose_project(self, project: Project):
        self.chosen_project = project
        self.project_name = project["name"]
        self.project_desc = project["desc"]

        with rx.session() as session:
            data = session.exec(
                select(Task).where(Task.project_id == self.chosen_project["id"])
            ).all()

            self.project_tasks = list(data)
            for task in self.project_tasks:
                for available_task in self.project_available_tasks:
                    if task.id == available_task.id:
                        self.project_available_tasks.remove(available_task)

        return rx.redirect(f"/projects/{project["id"]}")

    def remove_task_from_project(self, task: Task):
        for task_ in self.project_tasks:
            if task_.id == task["id"]:
                self.project_tasks.remove(task_)
                self.project_available_tasks.append(task_)
                return

    def add_task_to_project(self, task: Task):
        for task_ in self.project_available_tasks:
            if task_.id == task["id"]:
                self.project_available_tasks.remove(task_)
                self.project_tasks.append(task_)
                return

    def create_project(self):
        current_project = Project(name=self.project_name, desc=self.project_desc, color=self.project_color,
                                  user_id=self.user.id)

        with rx.session() as session:
            session.add(current_project)
            session.commit()

            for task in self.project_tasks:
                task.project_id = current_project.id
                session.add(task)

            session.commit()

        return rx.redirect("/projects")

    def update_project(self):
        id_ = self.chosen_project["id"]

        with rx.session() as session:
            current_project = session.exec(
                select(Project).where(Project.user_id == self.user.id).where(Project.id == id_)
            ).one()

            current_project.name = self.project_name
            current_project.desc = self.project_desc

            session.add(current_project)

            all_tasks = list(session.exec(select(Task)).all())
            ids_list = [task.id for task in self.project_tasks]

            for task in all_tasks:
                if task.id in ids_list:
                    task.project_id = id_
                else:
                    if task.project_id == id_:
                        task.project_id = None

            session.commit()

        return rx.redirect("/projects")

    def delete_project(self, project: Project):
        with rx.session() as session:
            current_project = session.exec(
                select(Project).where(Project.user_id == self.user.id).where(Project.id == project["id"])
            ).one()

            session.delete(current_project)
            session.commit()

        self.initialize()
        return rx.redirect("/projects")

    @rx.var
    def get_status_line(self) -> str:
        if self.selected_status is None:
            return "Статус"

        return self.selected_status.name

    @rx.var
    def get_project_line(self) -> str:
        if self.selected_project is None:
            return "Проект"

        return self.selected_project.name

    def set_status_selected(self, status: Status):
        with rx.session() as session:
            current_status = session.exec(
                select(Status).where(Status.user_id == self.user.id).where(Status.id == status["id"])
            ).one()

            self.selected_status = current_status

    def set_project_selected(self, project: Project):
        with rx.session() as session:
            current_project = session.exec(
                select(Project).where(Project.user_id == self.user.id).where(Project.id == project["id"])
            ).one()

            self.selected_project = current_project

    @rx.var
    def urgency(self):
        return self.status_urgency

    def create_status(self):
        if self.status_name == "":
            return

        with rx.session() as session:
            if session.exec(select(Status).where(
                    Status.user_id == self.user.id).where(Status.name == self.status_name)).one_or_none() is not None:
                print("Blocked here", self.status_name, self.user.id)
                return

            new_status = Status(name=self.status_name, urgency=self.status_urgency, color=self.status_color,
                                user_id=self.user.id)
            session.add(new_status)
            session.commit()

            self.statuses_dict[new_status.id] = new_status

        self.initialize()

    def initialize(self):
        if self.user is None:
            return

        self.initialize_project()
        self.load_tasks()
        self.load_tags()
        self.update_statuses()

        self.actual_tasks_list = self.tasks

        with rx.session() as session:
            tags = session.exec(
                select(Tag).where(Tag.user_id == self.user.id)
            ).all()

            projects = session.exec(
                select(Project).where(Project.user_id == self.user.id)
            ).all()

            self.available_tags = [str(tag) for tag in tags]
            self.projects = list(projects)
            self.project_available_tasks = self.tasks

    def update_statuses(self):
        if self.user is None:
            return

        with rx.session() as session:
            statuses = session.exec(
                select(Status).where(Status.user_id == self.user.id)
            ).all()

            for status in statuses:
                self.statuses_dict[status.id] = status

            self.statuses = list(statuses)

    def create_task(self):
        if self.task_date is not None:
            year, month, day = map(int, self.task_date.split('-'))

            if self.task_time is not None:
                hour, minute = map(int, self.task_time.split(':'))
            else:
                hour, minute = 0, 0

            self.deadline = datetime.datetime(year, month, day, hour, minute)

        if self.selected_status is None:
            if self.selected_project is None:
                task = Task(name=self.task_name, desc=self.task_desc, is_deligable=self.is_deligable,
                            is_complex=self.is_complex, user_id=self.user.id, deadline=self.deadline)
            else:
                task = Task(name=self.task_name, desc=self.task_desc, is_deligable=self.is_deligable,
                            is_complex=self.is_complex, user_id=self.user.id,
                            project_id=self.selected_project.id, deadline=self.deadline)
        else:
            if self.selected_project is None:
                task = Task(name=self.task_name, desc=self.task_desc, is_deligable=self.is_deligable,
                            is_complex=self.is_complex, user_id=self.user.id,
                            status_id=self.selected_status.id, deadline=self.deadline)
            else:
                print(self.task_name, self.task_desc, self.is_deligable, self.is_complex, self.selected_project.id,
                      self.selected_status.id, self.deadline)
                task = Task(name=self.task_name, desc=self.task_desc, is_deligable=self.is_deligable,
                            is_complex=self.is_complex, user_id=self.user.id,
                            project_id=self.selected_project.id, status_id=self.selected_status.id,
                            deadline=self.deadline)

        with rx.session() as session:
            session.add(task)
            session.commit()

            for tag in self.chosen_tags:
                if tag == '+':
                    continue

                result = session.exec(
                    select(Tag).where(Tag.user_id == self.user.id).where(Tag.name == tag)
                ).one()
                self.tasks_count_of_tags[result.id] += 1

                session.add(TagTaskLink(tag_id=result.id, task_id=task.id))

            session.commit()

        BasicChipsState.chosen_tags = ["+"]

        with rx.session() as session:
            tags = session.exec(
                select(Tag).where(Tag.user_id == self.user.id)
            ).all()

            self.available_tags = [str(tag) for tag in tags]

        return rx.redirect("/tasks")

    def select_status(self, item: str):
        with rx.session() as session:
            result = session.exec(
                select(Status).where(Status.user_id == self.user.id).where(Status.name == item)
            ).one()

            self.task_status = result

    def select_project(self, item: str):
        with rx.session() as session:
            result = session.exec(
                select(Project).where(Project.user_id == self.user.id).where(Project.name == item)
            ).one()

            self.task_project = result

    def add_selected(self, tag_name: str):
        self.available_tags.remove(tag_name)
        self.chosen_tags.append(tag_name)

    def remove_selected(self, tag_name: str):
        self.available_tags.append(tag_name)
        self.chosen_tags.remove(tag_name)

    def add_tags_to_default(self, lst):
        for tag in lst:
            self.add_selected(tag.name)

    def initialize_state(self, task: Task):
        current_task = rx.session().exec(
            select(Task).where(Task.id == task["id"])
        ).one()

        with rx.session() as session:
            current_task = session.exec(
                select(Task).where(Task.id == task["id"])
            ).one()

            self.task_name = current_task.name
            self.task_desc = current_task.desc

            if current_task.deadline is not None:
                self.deadline = current_task.deadline
                self.task_date = current_task.deadline.strftime("%Y-%m-%d")

            self.is_archive = current_task.is_archive
            self.is_deligable = current_task.is_deligable
            self.is_complex = current_task.is_complex

            self.task_project = current_task.project
            self.selected_project = current_task.project

            self.task_status = current_task.status
            self.selected_status = current_task.status

            current_tags_id = session.exec(
                select(TagTaskLink.tag_id).where(TagTaskLink.task_id == current_task.id)
            ).all()

            current_tags = [session.exec(select(Tag).where(Tag.id == id_)).one() for id_ in current_tags_id]

            self.chosen_tags = ["+"]
            tags = session.exec(
                select(Tag).where(Tag.user_id == self.user.id)
            ).all()
            self.available_tags = [str(tag) for tag in tags]

            self.add_tags_to_default(current_tags)

    def remove_selection(self, value: bool):
        if value:
            return

        self.show_select = False
        self.chosen_tags = ["+"]

        with rx.session() as session:
            tags = session.exec(
                select(Tag).where(Tag.user_id == self.user.id)
            ).all()

            self.available_tags = [str(tag) for tag in tags]

        self.task_name = ""
        self.task_desc = ""

        self.task_status = None
        self.selected_status = None

        self.task_project = None
        self.selected_project = None

        self.is_deligable = False
        self.is_archive = False
        self.is_complex = False
        self.show_edit_buttons = 0

        self.task_date = None
        self.task_time = None

    def update_task(self, task: Task):
        task_id = None

        with rx.session() as session:
            current_task = session.exec(
                select(Task).where(Task.id == task["id"])
            ).one()

            if self.task_date is not None:
                year, month, day = map(int, self.task_date.split('-'))

                if self.task_time is not None:
                    hour, minute = map(int, self.task_time.split(':'))
                else:
                    hour, minute = 0, 0

                self.deadline = datetime.datetime(year, month, day, hour, minute)

            current_task.deadline = self.deadline
            current_task.name = self.task_name
            current_task.desc = self.task_desc
            current_task.is_archive = self.is_archive
            current_task.is_deligable = self.is_deligable
            current_task.is_complex = self.is_complex

            if self.selected_status is not None:
                current_task.status_id = self.selected_status.id

            if self.selected_project is not None:
                current_task.project_id = self.selected_project.id

            session.add(current_task)
            session.commit()
            task_id = current_task.id

        with rx.session() as session:
            result = session.exec(
                select(TagTaskLink).where(TagTaskLink.task_id == task_id)
            ).all()

            for res in result:
                self.tasks_count_of_tags[res.tag_id] -= 1
                session.delete(res)
                session.commit()

            print(self.chosen_tags)
            for tag in self.chosen_tags:
                if tag == '+':
                    continue

                new_result = session.exec(
                    select(Tag).where(Tag.user_id == self.user.id).where(Tag.name == tag)
                ).one()

                self.tasks_count_of_tags[new_result.id] += 1
                session.add(TagTaskLink(tag_id=new_result.id, task_id=task_id))

            session.commit()

        return rx.redirect(self.router.page.raw_path)

    def remove_task(self, task: Task):
        with rx.session() as session:
            current_task = session.exec(
                select(Task).where(Task.id == task["id"])
            ).one()

            session.delete(current_task)
            session.commit()

        self.remove_selection(False)
        return rx.redirect("/tasks")

    def add_to_archive(self, task: Task):
        with rx.session() as session:
            current_task = session.exec(
                select(Task).where(Task.id == task["id"])
            ).one()

            current_task.is_archive = True
            session.add(current_task)
            session.commit()

        return rx.redirect(self.router.page.raw_path)

    def remove_from_archive(self, task: Task):
        with rx.session() as session:
            current_task = session.exec(
                select(Task).where(Task.id == task["id"])
            ).one()

            current_task.is_archive = False
            session.add(current_task)
            session.commit()

        return rx.redirect(self.router.page.raw_path)

    def create_tag(self):
        current_tag = Tag(name=self.tag_name, user_id=self.user.id)

        with rx.session() as session:
            session.add(current_tag)
            session.commit()

            self.available_tags.append(current_tag.name)

    def sort_actual_tasks(self):
        self.actual_tasks_list.sort(
            key=lambda task: (1 if task.is_archive else (
                task.deadline.toordinal() * 0.7 - (self.statuses_dict.get(
                    task.status_id).urgency * 0.3) if self.statuses_dict.get(
                    task.status_id) is not None else 0) if task.deadline else 1e9))


from time_management.pages.dialog.dialog_creation_tags import select_tags


def selected_item_chip(tag_name: str) -> rx.Component:
    return rx.cond(
        BasicChipsState.actions.contains(tag_name),
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    "+",
                    color_scheme="gray",
                    **chip_props,
                    border_radius="12px",
                    padding="0.5em",
                    margin="0.2em",
                    display="block"
                ),
            ), select_tags()
        ),
        rx.badge(
            tag_name,
            rx.icon("circle-x", size=18),
            color_scheme="gray",
            **chip_props,
            border_radius="12px",
            padding="0.5em",
            margin="0.2em",
            on_click=BasicChipsState.remove_selected(tag_name),
        ),
    )


def items_selector() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.foreach(
                BasicChipsState.chosen_tags,
                selected_item_chip,
            ),
            wrap="wrap",
            spacing="2",
            justify_content="start",
        ),
        width="90%",
    )
