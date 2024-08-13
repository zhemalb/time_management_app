import reflex as rx
from .beautiful_tag_selection import BasicChipsState
from .footer import render_footer

from time_management.components.header import header


def make_info_button(title: str, desc: str, format_line: str, param, callback: callable, icon_tag: str):
    return rx.button(
        rx.vstack(
            rx.hstack(
                rx.icon(tag=icon_tag, color="white"),
                width="100%",
                height="100%"
            ),
            rx.vstack(
                rx.text(title, font_style="Open Sans", font_weight="bold", font_size="20px",
                        color="white"),
                rx.text(desc, font_style="Open Sans", font_size="14px",
                        color="white", align="left"),
                rx.text(format_line.format(param),
                        font_style="Open Sans", font_size="12px", color="red"),
                width="100%",
                height="100%",
                padding="0px",
                spacing="1"
            ),
            width="100%",
            height="100%"
        ),
        padding="5px",
        background_color="#181818",
        border_radius="12px",
        border="3px solid #777777",
        width="100%",
        height="100%",
        # box_shadow="5px 3px 15px white",
        on_click=callback,
    ),


def render_settings() -> rx.Component:
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
                rx.vstack(
                    rx.vstack(
                        rx.text("Settings", font_size="28px", font_style="Open Sans", font_weight="900", color="white"),
                        rx.text("Customize it for yourself", font_size="16px", font_style="Open Sans",
                                font_weight="400",
                                color="white"),
                        align_items="left",
                        spacing="0",
                        padding="0px",
                        margin_left="5%"
                    ),
                    width="100%",
                    height="100%",
                ),
                width="100%",
                height="100%",
                bg="#191919",
            ),
            rx.vstack(
                rx.grid(
                    make_info_button("Statuses", "Can help assess the load of task",
                                     "You already have {0} statuses",
                                     BasicChipsState.statuses.length(), rx.redirect("/statuses"),
                                     "table-properties"),
                    make_info_button("Projects", "You can store tasks in projects", "You already have {0} projects",
                                     BasicChipsState.projects.length(), rx.redirect("/projects"), "folder-git-2"),
                    columns="2",
                    spacing="5",
                    width="90%",
                    bg="#191919",
                ),
                width="100%",
                height="60vh",
                align_items="center",
                bg="#191919",
            ),
            width="100%",
            height="100%",
        ),
        rx.vstack(
            render_footer(),
            position="absolute",
            bottom="0",
            width="100%",
            min_height="50px",
        ),
        width=["100%", "100%", "55%", "50%", "35%"],
        bg="#181818",
        padding="0px",
        box_shadow="0px 8px 16px 6px rgba(0, 0, 0, 0.25)"
    )


def render_projects_page() -> rx.Component:
    return rx.vstack(
        rx.text("Projects", font_size="28px", font_style="Open Sans", font_weight="900"),
        rx.foreach(BasicChipsState.projects, lambda tag: rx.text(tag)),
        rx.button("Back to Settings", on_click=rx.redirect("/settings")),
        render_footer()
    )
