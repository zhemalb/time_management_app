import os
import sys

import reflex as rx

from .pages.task_creation import tasks_page
from .pages.sign_system import render_main_component
from .pages.settings import render_settings, render_projects_page
from .pages.statuses_page import render_statuses_page
from .pages.show_all_lists import render_all_lists
from .pages.test import SpeedDialMenu

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
    return rx.center(
        tasks_page(),
        height="100vh",
        width="100%",
        bg="#191919"
    )


@rx.page("/settings")
def settings():
    return rx.center(
        render_settings(),
        width="100%",
        height="100vh",
        bg="#191919"
    )


@rx.page("/statuses")
def statuses():
    return rx.center(
        render_statuses_page(),
        width="100%",
        height="100vh",
        bg="#191919"
    )


@rx.page("/projects")
def projects():
    return render_projects_page()


@rx.page("/lists")
def lists():
    return render_all_lists()


speed_dial_menu = SpeedDialMenu.create


@rx.page("/test")
def render_menu():
    return rx.center(
        speed_dial_menu(),
        height="100vh",
        position="relative",
        width="100%",
        bg="#181818",
    )


# @rx.page("/test")
# def test():
#     pass

STYLES = {
    "::placeholder": {
        "font-weight": "bold",
        "font-size": "17px",
        "font-style": "Open Sans",
        "color": "#999999",
    }
}

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap",
        "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap",
    ],
    style=STYLES
)
