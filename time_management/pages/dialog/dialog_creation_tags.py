import reflex as rx

from ..beautiful_tag_selection import BasicChipsState

from time_management.database.models import Tag

from .dialog_tag_creation import render_tag_creation


def tag_select(tag: str) -> rx.Component:
    return rx.dialog.close(
        rx.box(
            rx.text(
                tag,
                font_style="Open Sans",
                font_weight="bold",
                font_size="16px",
                color="white",
            ),
            width="100%",
            align_items="center",
            _hover={
                "opacity": "1",
            },
            opacity="0.75",
            cursor="pointer",
            bg="#191919",
            on_click=BasicChipsState.add_selected(tag)
        )
    )


def select_tags():
    return rx.dialog.content(
        rx.center(
            rx.vstack(
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.chakra.button(
                            "(+) Создать тэг",
                            color="white",
                            font_style="Open Sans",
                            font_weight="bold",
                            font_size="16px",
                            variant="ghost",
                        ),
                    ), render_tag_creation()
                ),
                rx.scroll_area(
                    rx.vstack(
                        rx.flex(
                            rx.foreach(
                                BasicChipsState.available_tags,
                                tag_select
                            ),
                            direction="column",
                            bg="#181818",
                            align_items="center",
                            width="100%",
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
