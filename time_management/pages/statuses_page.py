import reflex as rx

from .footer import render_footer
from .beautiful_tag_selection import BasicChipsState

from ..database.models import Status


def subpages_header() -> rx.Component:
    return rx.hstack(
        rx.button(
            rx.icon(
                tag='arrow-big-left',
                color="white",
                size=30
            ),
            on_click=rx.redirect("/settings"),
            bg="#181818",
        ),
        rx.text("Статусы", font_style="Open Sans", font_weight="bold", font_size="28px", color="white"),
        rx.button(
            rx.icon(
                tag="info",
                color="white",
                size=30
            ),
            bg="#181818",
        ),
        justify="between",
        width="100%",
    )


def render_status(status: Status):
    return rx.vstack(
        rx.hstack(
            rx.vstack(
                rx.text(status.name, font_size="20px", font_weight="bold", font_style="Open Sans", color="black"),
                rx.text(status.urgency, font_size="20px", font_weight="bold", font_style="Open Sans",
                        color=status.color),
                padding="1vh 0px 0px 5vw",
                margin_bottom="1vh",
                width="90%"
            ),
            rx.vstack(
                rx.button(
                    rx.text("...", font_size="32", font_weight="bold", font_style="Open Sans", color="black"),
                    bg="white",
                ),
            ),
            padding_right="10px",
            width="100%",
        ),
        border_radius="12px",
        border=f"2px solid",
        border_color=status.color,
        width="100%"
    )


def render_statuses_page() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            subpages_header(),
            min_height="50px",
            width="100%",
            position="fixed",
            top="0",
            margin="5px 0px"
        ),
        rx.vstack(
            rx.scroll_area(
                rx.vstack(
                    rx.flex(
                        rx.foreach(
                            BasicChipsState.statuses,
                            render_status
                        ),
                        direction="column",
                        width="100%",
                        spacing="3",
                        height="100%",
                        bg="#181818"
                    ),
                    width="100%",
                    height="100%",
                    bg="#181818"
                ),
                scrollbars="vertical",
                width="100%",
                height="55vh",
                padding="5px",
                bg="#181818"
            ),
            background_color="#181818"
        ),
        rx.vstack(
            render_footer(),
            position="absolute",
            bottom="0",
            width="100%",
            min_height="50px",
        ),
        width=["100%", "100%", "55%", "50%", "35%"],
        bg="#181818",
        padding="0px",
        box_shadow="0px 8px 16px 6px rgba(0, 0, 0, 0.25)"
    )
