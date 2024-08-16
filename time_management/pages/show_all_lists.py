from typing import List

import reflex as rx

from ..components.header import header
from ..database.models import Project

from .footer import render_footer
from .beautiful_tag_selection import BasicChipsState


def render_list_badge(icon: str, name: str, desc: str, redirect: str) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(
                tag=icon,
                color="white",
                height="25px",
                width="25px",
            ),
            rx.text(
                name,
                font_style="Open Sans",
                color="white",
                font_weight="bold",
                font_size="20px",
            ),
            width="100%",
            align_items="center",
        ),
        rx.vstack(
            rx.text(
                desc,
                font_style="Open Sans",
                color="#777777",
                font_weight="regular",
                font_size="15px",
            )
        ),
        width="100%",
        bg="#191919",
        border_radius="12px",
        border="2px solid #777777",
        on_click=rx.redirect(redirect),
        padding="10px"
    )


def render_all_lists():
    return rx.vstack(
        rx.vstack(
            header(),
            min_height="50px",
            width="100%",
            position="fixed",
            top="0",
        ),
        rx.vstack(
            rx.vstack(
                rx.text("Списки", font_size="28px", font_style="Open Sans", font_weight="900",
                        color="white"),
                rx.text("Сгруппированные задачи", font_size="16px", font_style="Open Sans", font_weight="400",
                        color="#777777"),
                align_items="left",
                spacing="0",
                padding="0px",
                width="90%",
                height="100%"
            ),
            rx.vstack(
                rx.scroll_area(
                    rx.flex(
                        render_list_badge("hourglass", "Долгосрочные задачи", "О их дедлайне можно не переживать",
                                          "/long_term"),
                        render_list_badge("users", "Делегированные задачи", "Не забудьте написать исполнителю",
                                          "/delegable"),
                        render_list_badge("calendar-off", "Отложенные задачи", "Вернитесь к рассмотрению потом",
                                          "/postponed"),
                        render_list_badge("shapes", "Комплексные задачи", "Если над ними нужно поломать голову",
                                          "/complex"),
                        render_list_badge("archive", "Архив", "Если нужно просмотреть старые задачи", "/archive"),
                        direction="column",
                        width="90vw",
                        spacing="4",
                        align_items="center"
                    ),
                    type="always",
                    scrollbars="vertical",
                    width="90vw",
                    min_height="65vh",
                    max_height="65vh",
                ),
                height="100%",
                width="90%"
            ),
            width="100%",
            height="100%",
            align_items="center"
        ),
        rx.vstack(
            render_footer("project"),
            position="absolute",
            bottom="0",
            width="100%",
            min_height="50px",
        ),
        width=["100%", "100%", "55%", "50%", "35%"],
        bg="#191919",
        padding="0px",
        box_shadow="0px 8px 16px 6px rgba(0, 0, 0, 0.25)"
    )
