import reflex as rx
from sqlmodel import select

from time_management.components.test_inputs import empty_filled_input
from time_management.database.models import Status

from ..beautiful_tag_selection import BasicChipsState

from .dialog_color_select import render_select_dialog


def status_creation_window():
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
                        color=BasicChipsState.status_color,
                    ),
                    rx.dialog.close(
                        rx.icon_button(
                            rx.icon(
                                tag="check",
                                height="20px"
                            ),
                            bg="#191919",
                            on_click=BasicChipsState.create_status
                        ),
                    ),
                    justify="between",
                    align_items="center",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.dialog.root(
                            rx.dialog.trigger(
                                rx.icon_button(
                                    rx.icon(
                                        tag="pipette",
                                        color="white",
                                        height="20px",
                                    ),
                                    background_color="#191919"
                                )
                            ),
                            render_select_dialog(BasicChipsState.set_status_color)
                        ),
                        empty_filled_input("", "Название", BasicChipsState.set_status_name),
                        spacing="2",
                        align_items="center",
                    ),
                    rx.vstack(
                        rx.text(
                            f"Срочность - {BasicChipsState.urgency}",
                            font_style="Open Sans",
                            font_size="16px", font_weight="bold",
                            color="white"
                        ),
                        rx.chakra.slider(
                            on_change_end=BasicChipsState.set_status_urgency,
                            min_=1,
                            max_=10,
                            min_steps_between_thumbs=1,
                            width="70%",
                            default_value=5
                        ),
                        margin_bottom="20px",
                        width="100%",
                        align_items="center"
                    ),
                    align_items="center",
                    width="100%",
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
