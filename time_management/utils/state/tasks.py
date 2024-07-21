import reflex as rx
from typing import List, Optional
from sqlmodel import select

from .base import State, User
from .auth import AuthState

from time_management.database.models import Task


class TaskState(AuthState):
    tasks: List["Task"] = []

    add_task_modal_open: bool = False
    is_registration: bool = True

    new_task_title: str = ""
    new_task_description: str = ""
    new_task_categories: str = ""
    new_task_date: str = ""
    new_task_urgency: int = 0

    def load_tasks(self):
        self.tasks = []

    def add_task(self):
        print(f"Title: {self.new_task_title}")
        print(f"Description: {self.new_task_description}")
        print(f"Categories: {self.new_task_categories}")
        print(f"Date: {self.new_task_date}")
        print(f"Urgency: {self.new_task_urgency}")
        self.new_task_title = ""
        self.new_task_description = ""
        self.new_task_categories = ""
        self.new_task_date = ""
        self.new_task_urgency = 0
        self.add_task_modal_open = False
