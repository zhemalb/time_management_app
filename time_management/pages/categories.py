import reflex as rx

from ..database.core import *
from typing import List


def count_categories(tasks: List[Task]):
    category_counts = {}
    for task in tasks:
        for category in task.categories:
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1
    return category_counts


def render_category_buttons(category_counts: dict):
    return [
        rx.button(
            f"{category} ({count})",
            color_scheme="teal",
            variant="outline",
            size="4",
            border_radius="md",
            padding="0.5em 1em"
        )
        for category, count in category_counts.items()
    ]


def render_task(task: Task):
    return rx.box(
        rx.text(task.title, font_size="18px", font_weight="bold", font_family="Montserrat"),
        rx.text(task.description, font_size="14px", color="black", font_family="Montserrat"),
        rx.hstack(
            rx.foreach(
                task.categories,
                lambda category: rx.badge(category, color_scheme="green")
            ),
            spacing="1"
        ),
        rx.text(task.date, font_size="12px", color="black", font_family="Montserrat"),
        rx.text(task.urgency, font_size="12px", color="black", font_family="Montserrat"),
        border="1px solid lightgray",
        border_radius="5px",
        padding="1em",
        margin_bottom="1em"
    )
