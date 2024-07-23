import datetime

import reflex as rx
from typing import List, Optional
from sqlmodel import select

from .base import State, User
from .auth import AuthState

from time_management.database.models import Task, Tag, Status, Project, TagTaskLink


class TaskState(AuthState):
    tasks: list[Task] = []

    tags: list[Tag] = []
    tags_str: list[str] = []

    add_task_modal_open: bool = False
    is_registration: bool = True

    task_name: str
    task_desc: str | None = None
    task_status: Status | None = None
    task_project: Project | None = None
    is_deligable: bool = False
    is_info: bool = False
    is_complex: bool = False

    task_date: str | None = None
    task_time: str | None = None

    def load_tasks(self):
        with rx.session() as session:
            tasks = session.exec(
                select(Task).where(Task.user_id == self.user.id)
            ).all()

            self.tasks = tasks

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
            self.tags_str = [str(tag) for tag in self.tags]
