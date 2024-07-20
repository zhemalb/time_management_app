import reflex as rx

from .common import make_input_with_icon, box_with_text

from ..utils.state.auth import AuthState
from ..utils.config import LanguageConfig, language_data


def register_page() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/logo.jpg",
                    width="2.5em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    LanguageConfig.language["register"]["title"],
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            make_input_with_icon(LanguageConfig.language["register"]["email_text"],
                                 LanguageConfig.language["register"]["email_placeholder"],
                                 rx.icon("user"), AuthState.set_email),
            make_input_with_icon(
                LanguageConfig.language["register"]["password_text"],
                LanguageConfig.language["register"]["password_placeholder"],
                rx.icon("lock"), AuthState.set_password),
            make_input_with_icon(
                LanguageConfig.language["register"]["repeat_password_text"],
                LanguageConfig.language["register"]["repeat_password_placeholder"],
                rx.icon("lock"), AuthState.set_confirm_password),
            box_with_text(
                LanguageConfig.language["register"]["confirm_with_rules"]),
            rx.button(LanguageConfig.language["register"]["button_text"], size="3",
                      width="100%",
                      on_click=AuthState.signup),
            rx.center(
                rx.text(LanguageConfig.language["register"]["already_registered"],
                        size="3"),
                rx.link(LanguageConfig.language["register"]["login_link"],
                        href="#",
                        size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        max_width="28em",
        size="4",
        width="100%",
    )
