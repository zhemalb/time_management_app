import reflex as rx

from ..pages.beautiful_tag_selection import BasicChipsState


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text("Hi,", font_style="Open Sans", font_weight="regular", font_size="20px", align="left",
                        color="white"),
                rx.text(BasicChipsState.user.name, font_style="Open Sans", font_weight="bold", font_size="20px",
                        align="left",
                        color="white"),
                padding="0px",
                margin="0px",
                bg="#181818",
                align_items="left",
                justify="center",
                width="100%",
            ),
            width="100%",
            padding="10px",
            bg="#181818",
            border_bottom="2px solid #777777"
        ),
        width="100%",
        bg="#181818",
    )
