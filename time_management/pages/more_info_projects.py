import reflex as rx

from sqlmodel import select

from .beautiful_tag_selection import BasicChipsState

from time_management.components.test_inputs import empty_text_area, empty_filled_input
from time_management.database.models import Task

from .dialog.dialog_add_task_to_project import render_choose_menu

from .task_creation import get_badge


def render_removable_task(task: Task):
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
                        rx.text("15/07/2024 - 15:15", color="white", font_style="Open Sans", font_size="16px",
                                font_weight="bold"),
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
                rx.icon_button(
                    rx.icon(
                        tag="circle-x",
                        height="20px",
                        color="white"
                    ),
                    variant="ghost",
                    on_click=BasicChipsState.remove_task_from_project(task)
                )
            ),
            padding_right="10px",
            width="100%",
        ),
        border_radius="12px",
        border=f"2px solid",
        border_color=task.status.color,
        width="100%"
    )


def render_more_info_projects():
    return rx.vstack(
        rx.vstack(
            rx.hstack(
                rx.icon_button(
                    rx.icon(
                        tag="arrow-left",
                        color="white",
                        height="40px",
                        width="40px",
                    ),
                    on_click=rx.redirect("/projects"),
                    variant="ghost"
                ),
                rx.chakra.input(
                    placeholder="Название",
                    value=BasicChipsState.project_name,
                    on_change=BasicChipsState.set_project_name,
                    outline="none",
                    variant="unstyled",
                    color="#777777",
                    font_style="Open Sans",
                    font_size="20px",
                    width="70%",
                    font_weight="bold",
                    text_align="center"
                ),
                rx.box(height="40px", width="40px", bg="#191919"),
                width="100%",
                justify="between"
            ),
            rx.vstack(
                rx.text("Описание", font_style="Open Sans", font_weight="bold", font_size="20px", color="white"),
                rx.chakra.text_area(
                    value=BasicChipsState.project_desc,
                    placeholder="Описание",
                    on_change=BasicChipsState.set_project_desc,
                    variant="unstyled",
                    width="90%",
                    color="#777777",
                    font_style="Open Sans",
                    font_size="16px",
                    font_weight="bold",
                    text_align="center",
                    padding_bottom="0px"
                ),
                width="100%",
                display="flex",
                align_items="center",
            ),
            rx.vstack(
                rx.text("Задачи", font_style="Open Sans", font_weight="bold", font_size="20px", color="white"),
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.chakra.button(
                            "Добавить задачу",
                            font_style="Open Sans",
                            font_weight="bold",
                            font_size="20px",
                            color="white",
                            variant="ghost",
                            border="2px solid #777777"
                        ),
                    ), render_choose_menu()
                ),
                rx.vstack(
                    rx.scroll_area(
                        rx.flex(
                            rx.foreach(
                                BasicChipsState.project_tasks,
                                render_removable_task
                            ),
                            direction="column",
                            width="90vw",
                            spacing="4",
                        ),
                        type="always",
                        scrollbars="vertical",
                    ),
                    width="90%",
                ),
                width="100%",
                height="100%",
                align_items="center"
            ),
            width="100%",
            height="100%",
            align_items="center"
        ),
        rx.vstack(
            rx.chakra.button(
                "Сохранить",
                width="100%",
                font_size="16px",
                font_style="Open Sans",
                font_weight="bold",
                color="white",
                variant="ghost",
                on_click=BasicChipsState.update_project
            ),
            position="absolute",
            bottom="0",
            left="0",
            width="100%"
        ),
        width=["100%", "100%", "55%", "50%", "25%"],
        height="100%",
    )
