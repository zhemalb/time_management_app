import datetime
import reflex as rx

from typing import Annotated


class User(rx.Model):
    id: int = 0
    username: str
    password: str
    email: str


# class User:
#     def __init__(self, name: str, email: str, password: str, id: int = 0):
#         self.__name = name
#         self.__email = email
#         self.__password = password
#         self.__id = id
#
#     def get_name(self) -> str:
#         return self.__name
#
#     def get_email(self) -> str:
#         return self.__email
#
#     def get_password(self) -> str:
#         return self.__password
#
#     def get_id(self) -> int:
#         return self.__id


class Status:
    def __init__(self, name: str, user: User, urgency: int, id: int = 0, color: str = '505050'):
        self.__name = name
        self.__urgency = urgency
        self.__color = color
        self.__user = user
        self.__id = id

    def get_name(self):
        return self.__name

    def get_urgency(self):
        return self.__urgency

    def get_color(self):
        return self.__color

    def get_user(self):
        return self.__user

    def get_id(self):
        return self.__id


class Tag:
    def __init__(self, name: str, desc: str, user: User, id: int = 0, color: str = '505050'):
        self.__name = name
        self.__desc = desc
        self.__color = color
        self.__user = user
        self.__id = id

    def get_name(self):
        return self.__name

    def get_desc(self):
        return self.__desc

    def get_color(self):
        return self.__color

    def get_user(self):
        return self.__user

    def get_id(self):
        return self.__id


class Project:
    def __init__(self, project_name: str, user: User, id: int = 0, project_desc: str = '', color: str = '#505005'):
        self.__name = project_name
        self.__desc = project_desc
        self.__user = user
        self.__color = color
        self.__id = id

    def get_name(self):
        return self.__name

    def get_desc(self):
        return self.__desc

    def get_user(self):
        return self.__user

    def get_id(self):
        return self.__id

    def get_color(self):
        return self.__color


class Task:
    def __init__(self, name: str, tags: list[Tag], user: User, color: str = '#505050', id: int = 0, desc: str = '',
                 project: (Project | None) = None, status: (Status | None) = None,
                 deadline: datetime.datetime = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
                     days=7)):
        self.__name = name
        self.__tags = tags
        self.__user = user
        self.__color = color
        self.__desc = desc
        self.__project = project
        self.__status = status
        self.__id = id
        self.__deadline = deadline

    def get_name(self):
        return self.__name

    def get_tags(self):
        return self.__tags

    def get_user(self):
        return self.__user

    def get_desc(self):
        return self.__desc

    def get_id(self):
        return self.__id

    def get_project(self):
        return self.__project

    def get_status(self):
        return self.__status

    def get_color(self):
        return self.__color

    def get_deadline(self):
        return self.__deadline
