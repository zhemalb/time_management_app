import reflex as rx

from ..utils.state.tasks import TaskState
from ..utils.config import LanguageConfig


def make_input(title: str, placeholder: str, callback: callable, is_password: bool = False):
    return rx.vstack(
        rx.text(title, color="black", font_size="14px", font_family="Open Sans", font_weight="bold"),
        rx.chakra.input(
            placeholder=placeholder,
            color="black",
            type="text" if not is_password else "password",
            border="1.5px solid lightgray",
            border_radius="20px",
            font_family="Open Sans",
            on_change=callback
        ),
        width="100%",
        spacing="1"
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
        LanguageConfig.language["register"]["title"] if is_registration else LanguageConfig.language["login"]["title"],
        color_scheme="red",
        variant="solid",
        font_size="18px",
        width="100%",
        size="3",
        font_weight="bold",
        border_radius="20px",
        padding="1em 0em",
        on_click=register if is_registration else login,
        font_family="Open Sans"
    )


def render_vk_button(is_registration: bool, register: callable, login: callable):
    return rx.button(
        rx.hstack(
            rx.text(
                LanguageConfig.language["register"]["vk_auth"] if is_registration else LanguageConfig.language["login"][
                    "vk_auth"], color="white",
                font_family="Open Sans"),
        ),
        color_scheme="blue",
        variant="solid",
        size="3",
        font_weight="bold",
        width="100%",
        border_radius="20px",
        padding="1em 0em",
        on_click=register if is_registration else login
    )


def render_agreement(agreement_text: str, rules: str, other_rules: str):
    return rx.hstack(
        rx.checkbox(color_scheme="blue"),
        rx.text(agreement_text, color="black", font_family="Open Sans"),
        rx.link(rules, href="#", color="blue"),
        rx.text(", ", color="black", font_family="Open Sans"),
        rx.link(other_rules, href="#", color="blue"),
        spacing="1"
    )


def render_remember_me(remember_me: str, forgot_password: str):
    return rx.hstack(
        rx.hstack(
            rx.checkbox(color_scheme="blue"),
            rx.text(remember_me, color="black", font_family="Open Sans"),
        ),
        rx.link(forgot_password, href="#", color="blue", align='right'),
        justify="between",
        width="100%"
    )


def render_footer(is_registration: bool, have_account: str, dont_have_account: str, login: str, register: str):
    return rx.text(
        have_account if is_registration else dont_have_account, ' ',
        rx.link(login if is_registration else register, href="#", color="blue",
                on_click=rx.redirect("/login" if is_registration else "/register")),
        text_align="center",
        width="100%",
        color="black",
        font_family="Open Sans",
        margin_bottom="10px",
    )


#########################
def render_main_component(is_registration: bool):
    return rx.vstack(
        rx.vstack(
            rx.link(
                LanguageConfig.language["common"]["back_button"],
                href="/",
                color="black",
                font_family="Open Sans",
                font_weight="bold"
            ),
            justify_content="flex-start",
            margin="1em",
        ),
        rx.vstack(
            rx.text(
                LanguageConfig.language["register"]["title"] if is_registration else
                LanguageConfig.language["login"]["title"],
                font_size="40px",
                font_weight="bold",
                color="red",
                font_family="Open Sans"
            ),
            width="100%",
            display="flex",
            justify_content="center",
            align_items="center",
        ),
        rx.vstack(
            rx.cond(
                is_registration,
                make_input(LanguageConfig.language["register"]["username_text"],
                           LanguageConfig.language["register"]["username_placeholder"], TaskState.set_username),
            ),
            make_input(LanguageConfig.language["register"]["email_text"],
                       LanguageConfig.language["register"]["email_placeholder"], TaskState.set_email),
            make_input(LanguageConfig.language["register"]["password_text"],
                       LanguageConfig.language["register"]["password_placeholder"], TaskState.set_password,
                       True),
            rx.cond(
                is_registration,
                make_input(LanguageConfig.language["register"]["repeat_password_text"],
                           LanguageConfig.language["register"]["repeat_password_placeholder"],
                           TaskState.set_confirm_password,
                           True),
                render_remember_me(LanguageConfig.language["register"]["remember_me"],
                                   LanguageConfig.language["register"]["forgot_password"]),
            ),
            rx.cond(
                is_registration,
                render_agreement(LanguageConfig.language["register"]["arrangement_rules"],
                                 LanguageConfig.language["register"]["rules_name"],
                                 LanguageConfig.language["register"]["other_rules_name"]),
                rx.box()
            ),
            spacing="4",
            width="100%",
            padding="1.5% 5%"
        ),
        rx.vstack(
            render_event_trigger(is_registration, TaskState.signup, TaskState.login),
            render_vk_button(is_registration, TaskState.signup, TaskState.login),
            width="100%",
            padding="1.5% 5%"
        ),
        rx.vstack(
            render_footer(is_registration, LanguageConfig.language["register"]["already_registered"],
                          LanguageConfig.language["login"]["dont_have_account"],
                          LanguageConfig.language["register"]["already_registered_action"],
                          LanguageConfig.language["login"]["dont_have_account_action"],
                          ),
            width="100%",
            z_index="10",
            display="flex",
            padding="auto auto",
            align_items="center"
        ),
        width="100%",
        spacing="5",
        bg="white",
        border_radius="12px",
        border="2px solid lightgray"
    )


@rx.page("/register")
def register() -> rx.Component:
    """Главная страница приложения"""
    return rx.center(
        render_main_component(True),
        width="100%",
        height="100vh",
        bg="white"
    )


@rx.page("/login")
def login() -> rx.Component:
    """Главная страница приложения"""
    return rx.center(
        render_main_component(False),
        width="100%",
        height="100vh",
        bg="white"
    )
