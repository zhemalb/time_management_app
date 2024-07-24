import reflex as rx

from .dialog_tasks import make_header_input, make_text_area, render_action_button, render_select_with_text

from ..date_time_select import form_field
from ..beautiful_tag_selection import BasicChipsState, items_selector
from ..register import box_with_text

from time_management.database.models import Task, Tag, Status


def render_dialog_header(task: Task) -> rx.Component:
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
                        on_click=BasicChipsState.remove_selection
                    ),
                ),
                rx.text("Update task", font_size="6vw", font_weight="700", font_family="Open Sans", color="black"),
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
            rx.text("You can update chosen task", font_size="14px", font_weight="500", font_family="Open Sans",
                    color="white"),
            width="100%",
            height="100%",
            align_items="center",
            spacing="1"
        ),
        rx.vstack(
            make_header_input("Task name", "Task name here", BasicChipsState.set_task_name, default=task.name),
            rx.form.root(
                rx.hstack(
                    form_field(
                        "Date", "", "date", "event_date", BasicChipsState.set_task_date, width="75%", background="red"
                    ),
                    form_field(
                        "Time", "", "time", "event_time", BasicChipsState.set_task_time, width="20%", background="red"
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
        border_radius="0px 0px 12px 12px"
    )


def render_dialog_content(task: Task) -> rx.Component:
    return rx.vstack(
        rx.vstack(
            make_text_area("Description", "Enter task description here",
                           BasicChipsState.set_task_desc, task.desc),
            width="100%",
        ),
        rx.hstack(
            rx.vstack(
                render_select_with_text("Status", "Choose status", BasicChipsState.statuses,
                                        BasicChipsState.select_status, default=task.status.name),
                box_with_text("Note", BasicChipsState.set_is_info, default=task.is_info),
                box_with_text("Delegable", BasicChipsState.set_is_deligable, default=task.is_degibile),
            ),
            rx.vstack(
                render_select_with_text("Project", "Choose project", BasicChipsState.projects,
                                        BasicChipsState.select_project, default=task.project.name),
                box_with_text("Complex task", BasicChipsState.set_is_complex, default=task.is_complex),
            ),
            width="100%",
            justify="between"
        ),
        rx.vstack(
            rx.text("Select tags", font_size="14px", font_weight="bold", font_family="Open Sans", color="black"),
            items_selector(),
            width="100%",
            margin_bottom="15px",
            spacing="1",
        ),
        width="90%",
        height="100%",
        bg_color="white",
        margin="0px",
        align_items="center"
    )


def render_footer(task: Task) -> rx.Component:
    return render_action_button("Update Task", BasicChipsState.update_task(task))


def make_dialog_content(task: Task) -> rx.Component:
    return rx.dialog.content(
        rx.center(
            rx.vstack(
                rx.vstack(
                    render_dialog_header(task),
                    rx.vstack(
                        render_dialog_content(task),
                        width="100%",
                        align_items="center",
                    ),
                    width="100%",
                    height="100%",
                    magrin="0px",
                    padding="0px",
                ),
                rx.vstack(
                    render_footer(task),
                    width="100%",
                    height="7%",
                    padding="0px",
                    margin="0px"
                ),
                width="100%",
                height="100%",
            ),
            width="100%",
            height="100%",
            margin="0px"
        ),
        height="80vh",
        width="94vw",
        padding="0px",
        align_items="center"
    )
