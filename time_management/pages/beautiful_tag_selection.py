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
]

class BasicChipsState(rx.State):
    selected_items: list[str] = skills[:3]

    def add_selected(self, item: str):
        self.selected_items.append(item)

    def remove_selected(self, item: str):
        self.selected_items.remove(item)

    def add_all_selected(self):
        self.selected_items = list(skills)

    def clear_selected(self):
        self.selected_items.clear()

    def random_selected(self):
        self.selected_items = random.sample(
            skills, k=random.randint(1, len(skills))
        )


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
        border_radius="50%",
        padding="0.5em",
        margin="0.2em",
    )


def selected_item_chip(item: str) -> rx.Component:
    return rx.badge(
        item,
        rx.icon("circle-x", size=18),
        color_scheme="green",
        **chip_props,
        border_radius="50%",  # Makes the badge round
        padding="0.5em",  # Adjust padding for round appearance
        margin="0.2em",  # Adjust margin to reduce space between badges
        on_click=BasicChipsState.remove_selected(item),
    )


def unselected_item_chip(item: str) -> rx.Component:
    return rx.cond(
        BasicChipsState.selected_items.contains(item),
        rx.fragment(),
        rx.badge(
            item,
            rx.icon("circle-plus", size=18),
            color_scheme="gray",
            **chip_props,
            border_radius="50%",  # Makes the badge round
            padding="0.5em",  # Adjust padding for round appearance
            margin="0.2em",  # Adjust margin to reduce space between badges
            on_click=BasicChipsState.add_selected(item),
        ),
    )


def items_selector() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.hstack(
                rx.icon("lightbulb", size=20),
                rx.heading(
                    "Skills"
                    + f" ({BasicChipsState.selected_items.length()})",
                    size="4",
                ),
                spacing="1",
                align="center",
                width="100%",
                justify_content=["end", "start"],
            ),
            rx.hstack(
                action_button(
                    "plus",
                    "Add All",
                    BasicChipsState.add_all_selected,
                    "green",
                ),
                action_button(
                    "trash",
                    "Clear All",
                    BasicChipsState.clear_selected,
                    "tomato",
                ),
                action_button(
                    "shuffle",
                    "",
                    BasicChipsState.random_selected,
                    "gray",
                ),
                spacing="0.5",  # Reduce spacing between buttons
                justify="end",
                width="100%",
            ),
            justify="between",
            flex_direction=["column", "row"],
            align="center",
            spacing="2",
            margin_bottom="10px",
            width="100%",
        ),
        # Selected Items
        rx.flex(
            rx.foreach(
                BasicChipsState.selected_items,
                selected_item_chip,
            ),
            wrap="wrap",
            spacing="2",
            justify_content="start",
        ),
        rx.divider(),
        # Unselected Items
        rx.flex(
            rx.foreach(skills, unselected_item_chip),
            wrap="wrap",
            spacing="2",
            justify_content="start",
        ),
        justify_content="start",
        align_items="start",
        width="100%",
    )
