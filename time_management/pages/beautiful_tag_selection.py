import reflex as rx
import datetime
from sqlmodel import select

from ..database.models import Task, Tag, Status, Project, TagTaskLink
from ..utils.state.tasks import TaskState

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

    statuses: list[str] = []
    projects: list[str] = []

    def initialize(self):
        if self.user is None:
            return

        self.load_tasks()
        self.load_tags()

        with rx.session() as session:
            tags = session.exec(
                select(Tag).where(Tag.user_id == self.user.id)
            ).all()

            statuses = session.exec(
                select(Status).where(Status.user_id == self.user.id)
            ).all()

            projects = session.exec(
                select(Project).where(Project.user_id == self.user.id)
            ).all()

            self.available_tags = [str(tag) for tag in tags]
            self.statuses = [str(status) for status in statuses]
            self.projects = [str(project) for project in projects]

    def create_task(self):
        print(self.task_date, self.task_time)
        task = Task(name=self.task_name, desc=self.task_desc, is_info=self.is_info, is_deligable=self.is_deligable,
                    is_complex=self.is_complex, user_id=self.user.id, status_id=self.task_status.id,
                    project_id=self.task_project.id)

        with rx.session() as session:
            session.add(task)
            session.commit()

            for tag in self.chosen_tags:
                if tag == '+':
                    continue

                result = session.exec(
                    select(Tag).where(Tag.user_id == self.user.id and Tag.name == tag)
                ).one()

                session.add(TagTaskLink(tag_id=result.id, task_id=task.id))

            session.commit()

        BasicChipsState.chosen_tags = ["+"]

        with rx.session() as session:
            tags = session.exec(
                select(Tag).where(Tag.user_id == self.user.id)
            ).all()

            self.available_tags = [str(tag) for tag in tags]

        return rx.redirect("/")

    def select_status(self, item: str):
        with rx.session() as session:
            result = session.exec(
                select(Status).where(Status.user_id == self.user.id and Status.name == item)
            ).one()

            self.task_status = result

    def select_project(self, item: str):
        with rx.session() as session:
            result = session.exec(
                select(Project).where(Project.user_id == self.user.id and Project.name == item)
            ).one()

            self.task_project = result

    def add_selected(self, item: str):
        self.show_select = False

        self.available_tags.remove(item)
        self.chosen_tags.append(item)

    def remove_selected(self, item: str):
        self.available_tags.append(item)
        self.chosen_tags.remove(item)

    def add_tags_to_default(self, lst):
        for tag in lst:
            self.add_selected(tag["name"])

    def initialize_state(self, task: Task):
        self.task_status = task["status"].to_string()
        self.task_project = task["project"].to_string()
        self.add_tags_to_default(task["tags"])

    def remove_selection(self):
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
        self.task_project = None
        self.is_deligable = False
        self.is_info = False
        self.is_complex = False
        self.show_edit_buttons = False

        self.task_date = None
        self.task_time = None


def selected_item_chip(item: str) -> rx.Component:
    return rx.cond(
        BasicChipsState.actions.contains(item),
        rx.cond(
            BasicChipsState.available_tags.length() > 0,
            rx.badge(
                item,
                color_scheme="gray",
                **chip_props,
                border_radius="12px",
                padding="0.5em",
                margin="0.2em",
                on_click=BasicChipsState.set_show_select(True),
            ),
        ),
        rx.badge(
            item,
            rx.icon("circle-x", size=18),
            color_scheme="gray",
            **chip_props,
            border_radius="12px",
            padding="0.5em",
            margin="0.2em",
            on_click=BasicChipsState.remove_selected(item),
        ),
    )


def items_selector() -> rx.Component:
    return rx.vstack(
        rx.cond(
            BasicChipsState.show_select,
            rx.select(
                BasicChipsState.available_tags,
                placeholder="Choose tags",
                on_change=BasicChipsState.add_selected,
                width="100%",
                radius="large",
                position="popper",
            ),
            rx.flex(
                rx.foreach(
                    BasicChipsState.chosen_tags,
                    selected_item_chip,
                ),
                wrap="wrap",
                spacing="2",
                justify_content="start",
            )
        ),
        width="100%",
    )
