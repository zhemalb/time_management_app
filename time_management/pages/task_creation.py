import reflex as rx

# from ..utils.state.tasks import BasicChipsState
from ..database.models import Task, Tag

from .date_time_select import *
from .beautiful_tag_selection import BasicChipsState
from .footer import render_footer


def get_badge(tag: Tag):
    return rx.badge(
        tag.name,
        background_color=tag.color,
        color="black",
        font_style="Open Sans",
        font_size="14px",
        padding="8px",
        border_radius="12px",
    )


def render_task(task: Task):
    return rx.vstack(
        rx.hstack(
            rx.vstack(
                rx.text(task.name, font_size="20px", font_weight="bold", font_style="Open Sans", color="black"),
                rx.scroll_area(
                    rx.flex(
                        rx.text(
                            task.desc,
                            color="#505050",
                            font_size="15px",
                            font_style="Open Sans",
                        ),
                        direction="column",
                        spacing="4",
                    ),
                    scrollbars="vertical",
                    max_height="10%",
                    width="90%"
                ),
                rx.vstack(
                    rx.scroll_area(
                        rx.vstack(
                            rx.flex(
                                rx.foreach(
                                    task.tags,
                                    get_badge
                                ),
                                direction="row",
                            ),
                            width="100%",
                        ),
                        scrollbars="horizontal",
                        style={"width": 90},
                        width="100%"
                    ),
                    width="90%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text("15/07/2024 - 15:15", color="black", font_style="Open Sans", font_size="16px",
                                font_weight="bold"),
                        rx.text(task.status.name, color="black", font_style="Open Sans", font_size="16px",
                                font_weight="bold"),
                        spacing="2"
                    )
                ),
                padding="1vh 0px 0px 5vw",
                margin_bottom="1vh",
                width="90%"
            ),
            rx.vstack(
                rx.button(
                    rx.text("...", font_size="32", font_weight="bold", font_style="Open Sans", color="black"),
                    background_color="white",
                ),
            ),
            padding_right="10px",
            width="100%",
        ),
        border_radius="12px",
        border=f"2px solid",
        border_color=task.status.color,
        width="100%"
    )


def tasks_page() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.hstack(
                rx.icon(name="bell", tag="air_vent"),
                justify_content="space-between",
                align_items="center",
                padding="1em",
                width="100%",
            ),
            rx.vstack(
                rx.text("Hello world", text_size="32px", text_font="Open Sans", text_weight="bold"),
                width="100%",
                padding="5px",
                align_items="center",
            ),
            rx.vstack(
                rx.foreach(
                    BasicChipsState.tasks,
                    render_task
                ),
                width="100%",
                height="100%",
            ),
            width="100%",
            bg="white",
            border_radius="10px",
        ),
        render_footer(),
        width="100%",
        height="100%",
        bg="white",
        padding="0px"
    )
