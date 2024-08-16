import reflex as rx

from ..beautiful_tag_selection import BasicChipsState
from time_management.components.test_inputs import empty_selector, empty_filled_input

from .dialog_select_creation import status_creation_window

from time_management.database.models import Status


class ToggleStatusState(rx.State):
    toggle: bool = False
    chosen_status: Status | None = None

    def toggle_value(self, value: bool):
        self.toggle = value

    def choose_status(self, status: Status):
        self.chosen_status = status
        print(status["name"], status["urgency"])


def menu_item(status: Status) -> rx.Component:
    return rx.dialog.close(
        rx.button(
            rx.hstack(
                rx.box(
                    height="20px",
                    width="20px",
                    border_radius="1000px",
                    bg=status.color,
                ),
                rx.text(f"{status.name} ({status.urgency})",
                        font_style="Open Sans",
                        font_size="14px",
                        weight="bold",
                        color="white"),
                align="center",
                position="relative",
                width="100%",
            ),
            width="100%",
            align_items="center",
            _hover={
                "opacity": "1",
            },
            opacity="0.75",
            cursor="pointer",
            bg="#191919",
            on_click=BasicChipsState.set_status_selected(status)
        )
    )


def select_content():
    return rx.dialog.content(
        rx.center(
            rx.vstack(
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(
                            rx.text("(+) Новый статус", font_style="Open Sans", font_weight="bold",
                                    font_size="14px",
                                    color="white"),
                            width="100%",
                            bg="#181818",
                            _hover={
                                "opacity": "1",
                            },
                            opacity="0.75",
                            cursor="pointer",
                            align_items="center",
                        ),
                    ),
                    status_creation_window(),
                    on_open_change=BasicChipsState.change_status_open
                ),
                rx.scroll_area(
                    rx.vstack(
                        rx.flex(
                            rx.foreach(
                                BasicChipsState.statuses,
                                menu_item
                            ),
                            direction="column",
                            bg="#181818",
                            align_items="center"
                        ),
                        width="90%",
                        bg="#181818",
                        margin="0px 3px"
                    ),
                    type="always",
                    scrollbars="vertical",
                    style={"height": 250},
                    padding="5px",
                    bg="#181818",
                    width="100%",
                ),
                align_items="center",
                bg="#191919",
                width="100%",
            ),
            height='100%',
            border="2px solid gray",
            bg="#191919",
            width="100%",
        ),
        padding="0px",
        width="90%",
    )
