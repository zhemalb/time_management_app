import reflex as rx
from sqlmodel import select

from time_management.components.test_inputs import empty_filled_input
from time_management.database.models import Status

from ..beautiful_tag_selection import BasicChipsState

from .dialog_color_select import render_select_dialog


def render_tag_creation():
    return rx.dialog.content(
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.dialog.close(
                        rx.icon_button(
                            rx.icon(
                                tag="arrow-left",
                                height="20px"
                            ),
                            bg="#191919",
                        ),
                    ),
                    rx.text(
                        "Новый статус",
                        font_size="16px",
                        font_style="Open Sans",
                        font_weight="bold",
                        color="white"
                    ),
                    rx.dialog.close(
                        rx.icon_button(
                            rx.icon(
                                tag="check",
                                height="20px"
                            ),
                            bg="#191919",
                            on_click=BasicChipsState.create_tag
                        ),
                    ),
                    justify="between",
                    align_items="center",
                    width="100%",
                ),
                rx.vstack(
                    empty_filled_input("", "Название", BasicChipsState.set_tag_name),
                    spacing="2",
                    align_items="center",
                ),
                height="100%",
                width="100%",
                bg="#191919"
            ),
            height="100%",
            width="100%",
        ),
        padding="0",
        width="100%",
    )
