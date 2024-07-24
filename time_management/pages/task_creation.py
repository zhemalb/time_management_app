import reflex as rx
import datetime

# from ..utils.state.tasks import BasicChipsState
from ..database.models import Task, Tag

from .date_time_select import *
from .task_edit import task_edit_buttons

from .beautiful_tag_selection import BasicChipsState
from .footer import render_footer


def get_badge(tag: Tag):
    return rx.badge(
        rx.text(tag.name, font_style="Open Sans", font_size="14px", font_weight="bold", color="black"),
        color=tag.color,
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
        background_color="white",
        padding="8px",
        border="1px solid gray",
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
                    style={"height": 30},
                    width="90%"
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
                            rx.text(task.deadline, color="black", font_style="Open Sans",
                                    font_size="16px",
                                    font_weight="bold"),
                        ),
                        rx.cond(
                            BasicChipsState.tasks_status[task.id.to_int()] is not None,
                            rx.text(BasicChipsState.tasks_status[task.id.to_int()].name, color="black",
                                    font_style="Open Sans",
                                    font_size="16px",
                                    font_weight="bold"),
                        ),
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
                    on_click=BasicChipsState.toggle_edit_buttons(task.id)
                ),
                rx.cond(BasicChipsState.show_edit_buttons == task.id, task_edit_buttons(task)),
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
                rx.vstack(
                    rx.text("Current Tasks", font_size="28px", font_style="Open Sans", font_weight="900"),
                    rx.text("All your tasks to do here", font_size="16px", font_style="Open Sans", font_weight="400",
                            color="gray"),
                    align_items="left",
                    spacing="0",
                    padding="0px",
                ),
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
                padding="5px",
            ),
            rx.scroll_area(
                rx.vstack(
                    rx.flex(
                        rx.foreach(
                            BasicChipsState.tasks,
                            render_task
                        ),
                        direction="column",
                        width="100%",
                        spacing="3",
                        height="100%",
                    ),
                    width="100%",
                    height="100%",
                ),
                scrollbars="vertical",
                width="100%",
                height="100%",
                padding="5px"
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
