import datetime
import reflex as rx

from typing import Optional, List
from sqlmodel import Field, Relationship


class User(rx.Model, table=True):
    name: str
    email: str
    password: str
    registered_at: datetime.datetime = datetime.datetime.now(tz=datetime.timezone.utc)

    status: Optional["Status"] = Relationship(back_populates='user')
    project: Optional["Project"] = Relationship(back_populates='user')
    tags: List["Tag"] = Relationship(back_populates='user')
    tasks: Optional[List["Task"]] = Relationship(back_populates='user')


class Status(rx.Model, table=True):
    name: str
    urgency: int = 0
    color: str = "#505050"

    user_id: int = Field(foreign_key="user.id")

    user: User = Relationship(back_populates="status")
    tasks: List["Task"] = Relationship(back_populates="status")


class Project(rx.Model, table=True):
    name: str
    desc: Optional[str] = None
    color: str = "#505050"

    user_id: int = Field(foreign_key="user.id")

    user: User = Relationship(back_populates="project")
    tasks: List["Task"] = Relationship(back_populates="project")


class TagTaskLink(rx.Model, table=True):
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)
    task_id: Optional[int] = Field(default=None, foreign_key="task.id", primary_key=True)


class Tag(rx.Model, table=True):
    name: str
    desc: Optional[str] = None
    color: str = "#505050"

    user_id: int = Field(foreign_key="user.id")

    user: User = Relationship(back_populates="tags")
    tasks: List["Task"] = Relationship(back_populates="tags", link_model=TagTaskLink)

    def __str__(self):
        return f"{self.name} - {self.id}"


class Task(rx.Model, table=True):
    name: str
    desc: Optional[str] = None
    color: str = "#505050"
    created_at: datetime.datetime = datetime.datetime.now(tz=datetime.timezone.utc)
    deadline: Optional[datetime.datetime] = None

    is_info: bool = False
    is_degibile: bool = False
    is_complex: bool = False

    user_id: int = Field(foreign_key="user.id")
    status_id: Optional[int] = Field(foreign_key="status.id")
    project_id: Optional[int] = Field(foreign_key="project.id")

    user: User = Relationship(back_populates="tasks")
    tags: List["Tag"] = Relationship(back_populates="tasks", link_model=TagTaskLink)
    project: Optional["Project"] = Relationship(back_populates="tasks")
    status: Optional["Status"] = Relationship(back_populates="tasks")
