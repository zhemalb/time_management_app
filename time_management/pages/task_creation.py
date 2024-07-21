import reflex as rx

from ..utils.state.tasks import TaskState
from ..database.models import Task, Tag
from .beautiful_tag_selection import *


def get_badge(tag: Tag):
    return rx.badge(tag.name, color_scheme="green")


def render_task(task: Task):
    return rx.box(
        rx.text(task.name, font_size="18px", font_weight="bold", font_family="Montserrat"),
        rx.text(task.desc, font_size="14px", color="black", font_family="Montserrat"),
        rx.hstack(
            rx.foreach(
                task.tags,
                get_badge
            ),
            spacing="1",
        ),
        rx.text(str(task.deadline), font_size="12px", color="black", font_family="Montserrat"),
        rx.text(task.status.urgency, font_size="12px", color="black", font_family="Montserrat"),
        border="1px solid lightgray",
        border_radius="5px",
        padding="1em",
        margin_bottom="1em"
    )


def tasks_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                # # rx.avatar(src=State.user.avatar_url, size="md"),
                # rx.text(f"Привет, {TaskState.user.username}!", font_weight="bold", font_family="Montserrat",
                #         color_scheme="red"),
                rx.icon(name="bell", tag="air_vent"),
                justify_content="space-between",
                align_items="center",
                padding="1em",
                width="100%",
            ),
            rx.box(
                rx.text("Текущие задачи",
                        font_size="24px", font_weight="bold",
                        font_family="Montserrat", color_scheme="red"),
                rx.text("Список всех ваших задач здесь", font_size="16px", color="black", font_family="Montserrat"),
                width="100%",
                padding="1em",
                border_bottom="1px lightgray"
            ),
            # items_selector(),
            rx.foreach(
                TaskState.tasks,
                render_task
            ),
            rx.button(
                "+",
                color_scheme="blue",
                variant="solid",
                size="lg",
                border_radius="50%",
                padding="1em",
                position="fixed",
                bottom="2em",
                right="2em",
                on_click=TaskState.set_add_task_modal_open(True)
            ),
            rx.cond(
                TaskState.add_task_modal_open,
                rx.chakra.modal(
                    rx.chakra.modal_overlay(
                        rx.chakra.modal_content(
                            rx.chakra.modal_header("Добавить задачу"),
                            rx.chakra.modal_body(
                                rx.vstack(
                                    items_selector(),
                                    rx.input(
                                        placeholder="Заголовок",
                                        on_change=TaskState.set_new_task_title()
                                    ),
                                    rx.input(
                                        placeholder="Описание",
                                        on_change=TaskState.set_new_task_description()
                                    ),
                                    rx.input(
                                        placeholder="Дата",
                                        on_change=TaskState.set_new_task_date()
                                    ),
                                    rx.input(
                                        placeholder="Срочность",
                                        on_change=TaskState.set_new_task_urgency()
                                    ),
                                    rx.button("Добавить задачу", on_click=TaskState.add_task),
                                )
                            ),
                            rx.chakra.modal_footer(
                                rx.button("Закрыть", on_click=TaskState.set_add_task_modal_open(False))
                            )
                        )
                    ),
                    id="add_task_modal",
                    is_open=TaskState.add_task_modal_open
                )
            ),
            width="100%",
            padding="2em",
            bg="white",
            border_radius="10px",
        ),
        width=["100%", "100%", "65%", "50%", "35%"],
        margin="auto",
        bg="#f0f0f0",
        border="0.75px solid #e0e0e0",
        border_radius="10px",
        box_shadow="0px 8px 16px 6px rgba(0, 0, 0, 0.25)"
    )
