import reflex as rx

from ..utils.state.tasks import TaskState
from ..database.models import Task, Tag
from .beautiful_tag_selection import items_selector

from .date_time_select import *


def get_badge(tag: Tag):
    return rx.badge(tag.name, color_scheme="green")


def make_header_input(title: str, placeholder: str, callback: callable, is_password: bool = False, width: str = "100%"):
    return rx.vstack(
        rx.text(title, color="black", font_size="14px", font_family="Open Sans", font_weight="bold"),
        rx.chakra.input(
            placeholder=placeholder,
            type_="text" if not is_password else "password",
            border="2px solid #202020",
            border_radius="20px",
            font_family="Open Sans",
            font_size="14px",
            font_weight="400",
            on_change=callback
        ),
        width=width,
        spacing="1"
    )


def make_text_area(title: str, placeholder: str, callback: callable):
    return rx.vstack(
        rx.text(title, color="black", font_size="14px", font_family="Open Sans", font_weight="bold"),
        rx.text_area(
            placeholder=placeholder,
            type="text",
            border="2px solid #202020",
            border_radius="20px",
            font_family="Open Sans",
            font_size="14px",
            font_weight="400",
            width="100%",
            on_change=callback,
        ),
        width="100%",
        spacing="1"
    )


def render_select_with_text(text: str, placeholder: str, collection: list, callback: callable, width="100%"):
    return rx.vstack(
        rx.text(text, color="black", font_size="14px", font_family="Open Sans", font_weight="bold"),
        rx.select(
            collection,
            placeholder=placeholder,
            on_change=callback,
            width="100%",
            radius="large",
            position="popper",
        ),
        spacing="1",
        width=width
    )


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


def render_dialog_header() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.hstack(
                rx.dialog.close(
                    rx.button(
                        rx.image(
                            src="/back_button.png",
                            height="110%",
                        ),
                        display="block",
                        bg_color="red",
                    ),
                ),
                rx.text("Create new task", font_size="6vw", font_weight="700", font_family="Open Sans", color="black"),
                rx.button(
                    rx.image(
                        src="/info_button.png",
                        height="110%",
                    ),
                    display="block",
                    bg_color="red",
                ),
                height="100%",
                width="100%",
                align_items="center",
                justify="between",
                margin="5px 5px",
            ),
            rx.text("You can create tasks here", font_size="14px", font_weight="500", font_family="Open Sans",
                    color="white"),
            width="100%",
            height="100%",
            align_items="center",
            spacing="1"
        ),
        rx.vstack(
            make_header_input("Task name", "Task name here", TaskState.set_new_task_title),
            rx.form.root(
                rx.hstack(
                    form_field(
                        "Date", "", "date", "event_date", width="75%", background="red"
                    ),
                    form_field(
                        "Time", "", "time", "event_time", width="20%", background="red"
                    ),
                    justify="between",
                    width="100%",
                ),
                width="100%",
            ),
            width="90%",
            height="100%",
            margin_bottom="10px",
            spacing="4",
        ),
        spacing="5",
        bg_color="red",
        width="100%",
        align_items="center",
        border_radius="0px 0px 12px 12px",
        border="2px solid #202020"
    )


def render_dialog_content() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            make_text_area("Description", "Enter task description here", TaskState.set_new_task_description),
            width="100%",
        ),
        rx.vstack(
            rx.hstack(
                render_select_with_text("Status", "Choose status", [], TaskState.set_new_task_categories,
                                        width="47.5%"),
                render_select_with_text("Project", "Choose project", [], TaskState.set_new_task_title,
                                        width="47.5%"),
                justify="between",
                width="100%",
            ),
            width="100%",
            align_items="center",
        ),
        rx.vstack(
            rx.text("Select tags", font_size="14px", font_weight="bold", font_family="Open Sans", color="black"),
            items_selector(),
            width="100%",
        ),
        width="90%",
        height="100%",
        bg_color="white",
        margin="0px",
        align_items="center"
    )


def tasks_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
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
            rx.foreach(
                TaskState.tasks,
                render_task
            ),
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        "+",
                        color_scheme="blue",
                        variant="solid",
                        border_radius="50%",
                        padding="1em",
                        position="fixed",
                        bottom="2em",
                        right="2em",
                        on_click=TaskState.set_add_task_modal_open(True)
                    ),
                ),
                rx.dialog.content(
                    rx.vstack(
                        render_dialog_header(),
                        rx.vstack(
                            render_dialog_content(),
                            width="100%",
                            align_items="center",
                        ),
                        width="100%",
                        height="100%",
                        magrin="0px",
                        padding="0px",
                    ),
                    height="70vh",
                    width="90vw",
                    padding="0px",
                ),
            ),
            width="100%",
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
