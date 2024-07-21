import reflex as rx

from ..utils.state.tasks import TaskState
from ..database.models import Task, Tag
from ..database.core import *
from .task_creation import tasks_page


def make_input(title: str, placeholder: str, callback: callable, is_password: bool = False):
    return rx.center(
        rx.vstack(
            rx.text(title, color="black", font_size="16px", font_family="Montserrat", font_weight="bold"),
            rx.chakra.input(
                placeholder=placeholder,
                color="black",
                type="text" if not is_password else "password",
                width="200%",
                padding="1em",
                border="1px solid lightgray",
                border_radius="5px",
                font_family="Montserrat",
                on_change=callback
            )
        ),
        width="50%"
    )


def box_with_text(text, default: bool = False):
    return rx.box(
        rx.checkbox(
            text,
            default_checked=default,
            spacing="2",
        ),
        width="100%",
    ),


def render_event_trigger(is_registration: bool, register: callable, login: callable):
    return rx.button(
        "Создать аккаунт" if is_registration else "Войти",
        color_scheme="red",
        variant="solid",
        font_size="18px",
        width="100%",
        border_radius="5px",
        padding="1em 0em",
        on_click=register if is_registration else login,
        font_family="Montserrat"
    )


def render_vk_button(is_registration: bool, register: callable, login: callable):
    return rx.button(
        rx.hstack(
            rx.text("Регистрация через ВКонтакте" if is_registration else "Войти через ВКонтакте", color="white",
                    font_family="Montserrat"),
        ),
        color_scheme="blue",
        variant="solid",
        size="lg",
        width="100%",
        border_radius="5px",
        padding="1em 0em",
        on_click=register if is_registration else login
    )


def render_agreement(agreement_text: str, rules: str, other_rules: str):
    return rx.hstack(
        rx.checkbox(color_scheme="blue"),
        rx.text(agreement_text, color="black", font_family="Montserrat"),
        rx.link(rules, href="#", color="blue"),
        rx.text(", ", color="black", font_family="Montserrat"),
        rx.link(other_rules, href="#", color="blue"),
        spacing="0.5em"
    )


def render_remember_me(remember_me: str, forgot_password: str):
    return rx.hstack(
        rx.checkbox(color_scheme="blue"),
        rx.text(remember_me, color="black", font_family="Montserrat"),
        rx.link(forgot_password, href="#", color="blue"),
        justify="between",
        align="center",
        width="100%"
    )


def render_footer(is_registration: bool, have_account: str, dont_have_account: str, login: str, register: str):
    return rx.text(
        "Уже есть аккаунт? " if is_registration else "Еще нет аккаунта? ",
        rx.link("Войти" if is_registration else "Зарегистрироваться", href="#", color="blue",
                on_click=rx.redirect("/login" if is_registration else "/register")),
        text_align="center",
        width="100%",
        margin_top="1em",
        color="black",
        font_family="Montserrat"
    )


#########################
def render_main_component(is_registration: bool):
    return rx.vstack(
        rx.hstack(
            rx.link("< Назад", href="#", color="white"),
            justify_content="flex-start",
            align_items="center",
            padding="1em",
            width="100%",
        ),
        rx.box(
            width="100%",
            height="50px",
            bg="red",
        ),
        rx.center(
            rx.text("Регистрация" if is_registration else "Добро пожаловать", font_size="24px", font_weight="bold",
                    color="red", font_family="Montserrat"),
            width="100%",
            padding="1em",
            bg="white",
            border_radius="0px 0px 10px 10px"
        ),
        rx.vstack(
            rx.cond(
                is_registration,
                make_input("Имя пользователя", "Введите имя пользователя", TaskState.set_username),
            ),
            make_input("Электронная почта", "Введите адрес электронной почты", TaskState.set_email),
            make_input("Пароль", "Введите пароль", TaskState.set_password, True),
            rx.cond(
                is_registration,
                make_input("Повторите пароль", "Снова введите пароль", TaskState.set_confirm_password, True),
                render_remember_me("Запомнить", "хуй"),
            ),
            rx.cond(
                is_registration,
                render_agreement("111", "222", "333"),
                rx.box()
            ),
            render_event_trigger(is_registration, TaskState.signup, TaskState.login),
            render_vk_button(is_registration, TaskState.signup, TaskState.login),
            render_footer(is_registration, "huy", "pizda", "zalupa", "kiska"),
            width="100%",
            padding="2em",
            spacing="1em",
            bg="white",
            border_radius="0px 0px 10px 10px",
        ),
        width=["100%", "100%", "65%", "50%", "35%"],
        margin="auto",
        bg="red",
        border="0.75px solid #e0e0e0",
        border_radius="10px",
        box_shadow="0px 8px 16px 6px rgba(0, 0, 0, 0.25)",
    )


@rx.page("/register", on_load=TaskState.load_tasks)
def register() -> rx.Component:
    """Главная страница приложения"""
    return rx.center(
        render_main_component(True),
        width="100%",
        height="100vh",
        bg="#f0f0f0",
        padding="2em"
    )


@rx.page("/login", on_load=TaskState.load_tasks)
def login() -> rx.Component:
    """Главная страница приложения"""
    return rx.center(
        render_main_component(False),
        width="100%",
        height="100vh",
        bg="#f0f0f0",
        padding="2em"
    )
