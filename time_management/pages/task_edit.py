import reflex as rx
from time_management.database.models import Task

from .beautiful_tag_selection import BasicChipsState


def task_edit_buttons(task: Task):
    return rx.vstack(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    rx.text("Edit", font_size="16", font_weight="bold", font_style="Open Sans", color="black"),
                    background_color="white",
                    on_click=BasicChipsState.initialize_state(task)
                ),
            ),
            rx.vstack(),  # заглушка
            display="flex"
        ),
        rx.button(
            rx.text("Delete", font_size="16", font_weight="bold", font_style="Open Sans", color="black"),
            background_color="white",
        ),
        rx.button(
            rx.text("Archive", font_size="16", font_weight="bold", font_style="Open Sans", color="black"),
            background_color="white",
        ),
    )
