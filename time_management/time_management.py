import os
import sys

import reflex as rx

from .pages.task_creation import tasks_page
from .pages.sign_system import render_main_component
from .pages.settings import render_settings
from .pages.statuses_page import render_statuses_page
from .pages.show_all_lists import render_all_lists
from .pages.test import SpeedDialMenu
from .pages.projects import render_projects_page
from .pages.more_info_projects import render_more_info_projects

from .pages.beautiful_tag_selection import BasicChipsState

from .utils.state.base import State

sys.path.insert(1, os.path.join(sys.path[0], '..'))

STYLES = {
    "::placeholder": {
        "font-weight": "regular",
        "font-size": "16px",
        "font-style": "Open Sans",
        "color": "#777777",
    }
}

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap",
        "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap",
    ],
    style=STYLES
)


@rx.page("/register")
def register() -> rx.Component:
    """Главная страница приложения"""
    return rx.center(
        render_main_component(True),
        width="100%",
        height="100vh",
        bg="#181818"
    )


@rx.page("/")
def login() -> rx.Component:
    """Главная страница приложения"""
    return rx.center(
        render_main_component(False),
        width="100%",
        height="100vh",
        bg="#181818"
    )


@rx.page("/tasks", on_load=BasicChipsState.load_actual_tasks)
def main_page():
    return rx.center(
        tasks_page("Актуальные задачи", "Просто смотрите и делайте"),
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


@rx.page("/long_term", on_load=BasicChipsState.load_long_terms_tasks)
def long_term_tasks():
    return rx.center(
        tasks_page("Долгосрочные задачи", "О их дедлайне можно не переживать"),
        width="100%",
        height="100vh",
        bg="#191919"
    )


@rx.page("/delegable", on_load=BasicChipsState.load_delegable_tasks)
def long_term_tasks():
    return rx.center(
        tasks_page("Делегированные задачи", "Не забудьте написать исполнителю"),
        width="100%",
        height="100vh",
        bg="#191919"
    )


@rx.page("/postponed", on_load=BasicChipsState.load_postponed_tasks)
def long_term_tasks():
    return rx.center(
        tasks_page("Отложенные задачи", "Вернитесь к рассмотрению потом"),
        width="100%",
        height="100vh",
        bg="#191919"
    )


@rx.page("/complex", on_load=BasicChipsState.load_complex_tasks)
def long_term_tasks():
    return rx.center(
        tasks_page("Комплексные задачи", "Если над ними нужно поломать голову"),
        width="100%",
        height="100vh",
        bg="#191919"
    )


@rx.page("/archive", on_load=BasicChipsState.load_archive_tasks)
def long_term_tasks():
    return rx.center(
        tasks_page("Архив", "Если нужно просмотреть старые задачи"),
        width="100%",
        height="100vh",
        bg="#191919"
    )


@rx.page("/lists")
def lists():
    return rx.center(
        render_all_lists(),
        width="100%",
        height="100vh",
        bg="#191919"
    )


@rx.page("/bin", on_load=BasicChipsState.load_bin)
def lists():
    return rx.center(
        tasks_page("Корзина", "Здесь ВСЕ твои задачи"),
        width="100%",
        height="100vh",
        bg="#191919"
    )


speed_dial_menu = SpeedDialMenu.create


@rx.page("/projects", on_load=BasicChipsState.initialize)
def render_projects():
    return rx.center(
        render_projects_page(),
        width="100%",
        height="100vh",
        bg="#191919"
    )


@rx.page(route="/projects/[project_id]")
def render_more_projects():
    return rx.center(
        render_more_info_projects(),
        width="100%",
        height="100vh",
        bg="#191919",
    )

# @rx.page("/test")
# def test():
#     pass
