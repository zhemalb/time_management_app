import os
import sys

import reflex as rx

from .pages.task_creation import tasks_page
from .pages.common import render_main_component
from .pages.settings import render_settings
from .pages.show_all_lists import render_all_lists

from .pages.beautiful_tag_selection import BasicChipsState

from .utils.state.base import State

sys.path.insert(1, os.path.join(sys.path[0], '..'))


@rx.page("/register")
def register() -> rx.Component:
    """Главная страница приложения"""
    return rx.center(
        render_main_component(True),
        width="100%",
        height="100vh",
        bg="white"
    )


@rx.page("/")
def login() -> rx.Component:
    """Главная страница приложения"""
    return rx.center(
        render_main_component(False),
        width="100%",
        height="100vh",
        bg="white"
    )


@rx.page("/tasks", on_load=BasicChipsState.initialize)
def main_page():
    return tasks_page()


@rx.page("/settings")
def settings():
    return render_settings()


@rx.page("/lists")
def lists():
    return render_all_lists()


# @rx.page("/test")
# def test():
#     pass


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap",
        "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap",
    ],
)
