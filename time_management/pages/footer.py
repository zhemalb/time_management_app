import reflex as rx

from .dialog.dialog_tasks import BasicChipsState, make_dialog_content
from .dialog.dialog_project_creation import render_project_creation_dialog


def render_footer(using_dialog="tasks"):
    return rx.hstack(
        rx.button(
            rx.image(
                src="/actual_tasks.png",
                height="36px",
            ),
            height="100%",
            bg="#7f7f7f",
            text_align="center",
            on_click=rx.redirect("/tasks")
        ),
        rx.button(
            rx.image(
                src="/all_tasks.png",
                height="36px",
            ),
            height="100%",
            bg="#7f7f7f",
            text_align="center",
        ),
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    rx.image(
                        src="/add_new_task.png",
                        height="36px",
                        on_click=BasicChipsState.set_add_task_modal_open(True)
                    ),
                    height="100%",
                    bg="#7f7f7f",
                    align_items="center",
                ),
            ),
            rx.cond(
                using_dialog == "tasks",
                make_dialog_content(),
                render_project_creation_dialog()
            ),
            on_open_change=lambda i: BasicChipsState.initialize_project()
        ),
        rx.button(
            rx.image(
                src="/all_lists.png",
                height="36px",
            ),
            height="100%",
            bg="#7f7f7f",
            text_align="center",
            on_click=rx.redirect("/lists")
        ),
        rx.button(
            rx.image(
                src="/projects.png",
                height="36px",
            ),
            height="100%",
            bg="#7f7f7f",
            text_align="center",
            on_click=rx.redirect("/projects")
        ),
        justify="between",
        bg_color="#7f7f7f",
        width="100%",
        padding="10px 0px"
    )
