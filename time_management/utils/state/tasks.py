import datetime

import reflex as rx
from typing import List, Optional
from sqlmodel import select

from .base import State, User
from .auth import AuthState

from time_management.database.models import Task, Tag, Status, Project, TagTaskLink


class TaskState(AuthState):
    tasks: List["Task"] = []
    tags: List["Tag"] = []

    add_task_modal_open: bool = False
    is_registration: bool = True

    new_task_title: str = ""
    new_task_description: str = ""
    new_task_categories: str = ""
    new_task_date: str = ""
    new_task_urgency: int = 0

    task_name: str
    task_color: str = "#505050"
    task_desc: str | None = None
    task_tags: list[Tag]
    task_status: Status
    task_project: Project
    task_deadline: datetime.datetime | None = None

    def load_tasks(self):
        with rx.session() as session:
            tasks = session.exec(
                select(Task).where(Task.user_id == self.user.id)
            ).all()

            self.tasks = list(tasks)

    def add_task(self):
        with rx.session() as session:
            current_task = Task(name=self.task_name, description=self.task_desc, color=self.task_color,
                                deadline=self.task_deadline, user_id=self.user.id, status_id=self.task_status.id,
                                project_id=self.task_project.id)
            session.add(current_task)
            session.commit()

            for tag in self.task_tags:
                session.add(TagTaskLink(tag_id=tag.id, task_id=current_task.id))

            session.commit()

    def load_tags(self):
        with rx.session() as session:
            tags = session.exec(
                select(Tag).where(Tag.user_id == self.user.id)
            ).all()

            self.tags = list(tags)
