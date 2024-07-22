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
    selected_items: list[str] = ["+"]
    left_items: list[str] = skills[:len(skills) - 1]
    show_select: bool = False

    actions: list[str] = ["+"]

    def add_selected(self, item: str):
        self.show_select = False
        self.selected_items.append(item)
        self.left_items.remove(item)

    def remove_selected(self, item: str):
        self.selected_items.remove(item)
        self.left_items.append(item)


def action_button(
        icon: str,
        label: str,
        on_click: callable,
        color_scheme: LiteralAccentColor,
) -> rx.Component:
    return rx.button(
        rx.icon(icon, size=16),
        label,
        variant="soft",
        size="2",
        on_click=on_click,
        color_scheme=color_scheme,
        cursor="pointer",
        border_radius="12px",
        padding="0.5em",
        margin="0.2em",
    )


def selected_item_chip(item: str) -> rx.Component:
    return rx.cond(
        BasicChipsState.actions.contains(item),
        rx.badge(
            item,
            color_scheme="green",
            **chip_props,
            border_radius="12px",
            padding="0.5em",
            margin="0.2em",
            on_click=BasicChipsState.set_show_select(True),
        ),
        rx.badge(
            item,
            rx.icon("circle-x", size=18),
            color_scheme="green",
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
                BasicChipsState.left_items,
                on_change=BasicChipsState.add_selected
            ),
            rx.flex(
                rx.foreach(
                    BasicChipsState.selected_items,
                    selected_item_chip,
                ),
                wrap="wrap",
                spacing="2",
                justify_content="start",
            ),
        )
    )
