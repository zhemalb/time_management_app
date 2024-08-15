import reflex as rx

from time_management.components.test_inputs import *
from time_management.database.models import Task

from ..beautiful_tag_selection import BasicChipsState

from .dialog_color_select import render_select_dialog


def render_task_line(task: Task, icon: str, callback: callable):
    return rx.hstack(
        rx.text(
            task.name,
            font_style="Open Sans",
            font_weight="bold",
            font_size="20px",
            color="white"
        ),
        rx.icon_button(
            rx.icon(
                tag=icon,
                color="white",
                height="30px"
            ),
            on_click=callback,
            variant="ghost",
        )
    )


def render_project_creation_dialog() -> rx.Component:
    return rx.dialog.content(
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.icon(tag="arrow-left", height="46px", color="white"),
                    rx.text("New Project", font_style="Open Sans", font_size="28px", font_weight="bold",
                            color=BasicChipsState.project_color),
                    rx.dialog.close(
                        rx.icon_button(
                            rx.icon(
                                tag="check",
                                height="20px"
                            ),
                            bg="#191919",
                            on_click=BasicChipsState.create_project
                        ),
                    ),
                    justify="between",
                    height="50px",
                    width="100%",
                    display="flex",
                    align_items="center",
                    padding="10px"
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
                                    variant="ghost",
                                )
                            ), render_select_dialog(BasicChipsState.set_project_color)
                        ),
                        empty_filled_input("", "Название", BasicChipsState.set_project_name),
                        width="80%",
                        align_items="center"
                    ),
                    rx.vstack(
                        empty_text_area("", "Описание", BasicChipsState.set_project_desc),
                        width="80%",
                    ),
                    rx.vstack(
                        rx.text(
                            "Задачи",
                            font_style="Open Sans",
                            font_weight="bold",
                            font_size="24px",
                            color="white",
                        ),
                        rx.dialog.root(
                            rx.dialog.trigger(
                                rx.chakra.button(
                                    "Добавить задачу",
                                    font_style="Open Sans",
                                    font_weight="bold",
                                    font_size="18px",
                                    variant="ghost",
                                    color="white",
                                ),
                            ), rx.dialog.content(
                                rx.center(
                                    rx.vstack(
                                        rx.dialog.close(
                                            rx.icon_button(
                                                rx.icon(
                                                    tag="arrow-left",
                                                    height="30px",
                                                    width="30px",
                                                    color="white"
                                                ),
                                                variant="ghost",
                                                align="left",
                                                margin="10px"
                                            ),
                                        ),
                                        rx.scroll_area(
                                            rx.flex(
                                                rx.foreach(
                                                    BasicChipsState.project_available_tasks,
                                                    lambda i: render_task_line(i, "check",
                                                                               BasicChipsState.add_task_to_project(
                                                                                   i))
                                                ),
                                                direction="column",
                                                width="90vw",
                                                spacing="4",
                                                align_items="center",
                                            ),
                                            type="always",
                                            scrollbars="vertical",
                                            align_items="center",
                                        ),
                                        width="100%",
                                        height="100%",
                                    ),
                                    height="100%",
                                    margin="0px",
                                    bg="#191919",
                                ),
                                height="50vh",
                                padding="0px",
                                width=["100%", "100%", "55%", "50%", "25%"],
                            )
                        ),
                        rx.vstack(
                            rx.scroll_area(
                                rx.flex(
                                    rx.foreach(
                                        BasicChipsState.project_tasks,
                                        lambda i: render_task_line(i, "circle-x",
                                                                   BasicChipsState.remove_task_from_project(i))
                                    ),
                                    direction="column",
                                    width="90vw",
                                    spacing="4",
                                    align_items="center",
                                ),
                                type="always",
                                scrollbars="vertical",
                                border="2px solid #777777"
                            ),
                            width="100%",
                        ),
                        width="100%",
                        height="100%",
                        align_items="center"
                    ),
                    align_items="center",
                    width="100%",
                    height="100%",
                ),
                width="100%",
                height="100%",
            ),
            height="100%",
            margin="0px",
            bg="#191919",
        ),
        height="70vh",
        padding="0px",
        width=["100%", "100%", "55%", "50%", "25%"],
    )
