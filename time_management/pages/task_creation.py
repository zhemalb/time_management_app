import reflex as rx
import datetime

# from ..utils.state.tasks import BasicChipsState
from ..components.header import header
from ..database.models import Task, Tag

from .date_time_select import *
from .task_edit import task_edit_buttons

from .beautiful_tag_selection import BasicChipsState
from .footer import render_footer


def get_badge(tag: Tag):
    return rx.badge(
        rx.text(tag.name, font_style="Open Sans", font_size="14px", font_weight="bold", color="black"),
        bg=tag.color,
        padding="8px",
        border_radius="12px",
        border="1px solid #202020"
    )


def get_header_badge(tag: Tag):
    return rx.badge(
        rx.text(tag.name, font_style="Open Sans", font_size="14px", font_weight="bold", color="black"),
        rx.box(
            rx.text(BasicChipsState.tasks_count_of_tags[tag.id.to_int()], font_style="Open Sans", font_size="14px",
                    font_weight="bold", color="white"),
            bg=tag.color,
            border_radius="12px",
            padding="2px 6px",
        ),
        bg="white",
        padding="8px",
        border="1px solid gray",
        border_radius="12px",
    )


def render_task(task: Task):
    return rx.vstack(
        rx.hstack(
            rx.vstack(
                rx.text(task.name, font_size="20px", font_weight="bold", font_style="Open Sans", color="white"),
                rx.vstack(
                    rx.scroll_area(
                        rx.vstack(
                            rx.flex(
                                rx.text(
                                    task.desc,
                                    color="white",
                                    font_size="16px",
                                    font_style="Open Sans",
                                    trim="both"
                                ),
                                direction="column",
                                spacing="4",
                                width="90vw",
                            ),
                            width="100%",
                        ),
                        type="always",
                        scrollbars="vertical",
                        style={"height": 60},
                    ),
                    width="100%",
                ),
                rx.vstack(
                    rx.scroll_area(
                        rx.vstack(
                            rx.flex(
                                rx.foreach(
                                    BasicChipsState.tasks_tags[task.id.to_int()],
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
                        rx.cond(
                            task.deadline is not None,
                            rx.text("test deadline value", color="white", font_style="Open Sans",
                                    font_size="16px",
                                    font_weight="bold"),
                        ),
                        rx.text(BasicChipsState.tasks_status[task.id.to_int()].name, color="white",
                                font_style="Open Sans",
                                font_size="16px",
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
                    rx.text("...", font_size="32", font_weight="bold", font_style="Open Sans", color="white"),
                    background_color="#191919",
                    margin="2px 4px 0px 0px"
                ),
                rx.cond(BasicChipsState.show_edit_buttons, task_edit_buttons(task)),
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
            header(),
            min_height="50px",
            width="100%",
            position="fixed",
            top="0",
        ),
        rx.vstack(
            rx.vstack(
                rx.text("Current Tasks", font_size="28px", font_style="Open Sans", font_weight="900",
                        color="white"),
                rx.text("All your tasks to do here", font_size="16px", font_style="Open Sans", font_weight="400",
                        color="#777777"),
                align_items="left",
                spacing="0",
                padding="0px",
                width="100%",
                height="100%",
            ),
            rx.vstack(
                rx.scroll_area(
                    rx.vstack(
                        rx.flex(
                            rx.foreach(
                                BasicChipsState.tags,
                                get_header_badge
                            ),
                            direction="row",
                        ),
                        width="100%",
                    ),
                    scrollbars="horizontal",
                    style={"width": 90},
                    width="100%",
                    padding="5px"
                ),
                width="100%",
                height="100%",
            ),
            rx.vstack(
                rx.scroll_area(
                    rx.flex(
                        rx.foreach(
                            BasicChipsState.actual_tasks_list,
                            render_task
                        ),
                        direction="column",
                        width="100vw",
                        spacing="4",
                    ),
                    type="always",
                    scrollbars="vertical",
                    width="100vw",
                    min_height="65vh",
                ),
                width="100%",
                height="100%",
            ),
            width="100%",
            bg="#191919",
            border_radius="10px",
        ),
        rx.vstack(
            render_footer(),
            position="absolute",
            bottom="0",
            width="100%",
            min_height="50px",
        ),
        width=["100%", "100%", "55%", "50%", "35%"],
        bg="#191919",
        padding="0px",
        box_shadow="0px 8px 16px 6px rgba(0, 0, 0, 0.25)"
    )
