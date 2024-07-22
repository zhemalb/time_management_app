import os
import sys

import reflex as rx

from .pages.footer import render_footer
from .pages.register import register_page
from .pages.task_creation import tasks_page

from .utils.state.auth import AuthState

sys.path.insert(1, os.path.join(sys.path[0], '..'))


# todo: Need to complete this block
@rx.page("/")
def index():
    return render_footer()


@rx.page("/register")
def login():
    return register_page()


@rx.page("/tasks")
def aaa():
    return tasks_page()


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap",
        "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap",
    ],
)
