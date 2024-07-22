import random
import reflex as rx
from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)
from ..utils.state.tasks import TaskState
from ..database.models import Task, Tag

chip_props = {
    "radius": "full",
    "variant": "surface",
    "size": "3",
    "cursor": "pointer",
    "style": {"_hover": {"opacity": 0.75}},
}

skills = [
    "Data Management",
    "Networking",
    "Security",
    "Cloud",
    "DevOps",
    "Data Science",
    "AI",
    "ML",
    "Robotics",
    "Cybersecurity",
    "+"
]


class BasicChipsState(rx.State):
    show_select: bool = False

    actions: list[str] = ["+"]

    def add_selected(self, item: str):
        self.show_select = False
        TaskState.task_tags.append(item)

    def remove_selected(self, item: str):
        TaskState.task_tags.remove(item)


def selected_item_chip(item: str) -> rx.Component:
    return rx.cond(
        BasicChipsState.actions.contains(item),
        rx.badge(
            item,
            color_scheme="gray",
            **chip_props,
            border_radius="12px",
            padding="0.5em",
            margin="0.2em",
            on_click=BasicChipsState.set_show_select(True),
        ),
        rx.badge(
            item,
            rx.icon("circle-x", size=18),
            color_scheme="gray",
            **chip_props,
            border_radius="12px",
            padding="0.5em",
            margin="0.2em",
            on_click=BasicChipsState.remove_selected(item),
        ),
    )


def items_selector() -> rx.Component:
    return rx.vstack(
        rx.cond(
            BasicChipsState.show_select,
            rx.select(
                TaskState.get_available_tags,
                on_change=BasicChipsState.add_selected,
                width="100%"
            ),
            rx.flex(
                rx.foreach(
                    TaskState.task_tags,
                    selected_item_chip,
                ),
                wrap="wrap",
                spacing="2",
                justify_content="start",
            )
        ),
        width="100%",
    )
