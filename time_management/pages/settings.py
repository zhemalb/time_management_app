import reflex as rx
from .beautiful_tag_selection import BasicChipsState
from .footer import render_footer


def make_info_button(title: str, desc: str, format_line: str, param, callback: callable, icon_tag: str):
    return rx.button(
        rx.vstack(
            rx.hstack(
                rx.icon(tag=icon_tag, color="black"),
                width="100%",
                height="100%"
            ),
            rx.vstack(
                rx.text(title, font_style="Open Sans", font_weight="bold", font_size="20px",
                        color="black"),
                rx.text(desc, font_style="Open Sans", font_size="14px",
                        color="black", align="left"),
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
        background_color="white",
        border_radius="12px",
        border="2px solid #202020",
        width="100%",
        height="100%",
        box_shadow="5px 3px 10px black",
        on_click=callback
    ),


def render_settings():
    return rx.vstack(
        rx.vstack(
            rx.hstack(
                rx.icon(name="bell", tag="air_vent"),
                justify_content="space-between",
                align_items="center",
                padding="1em",
                width="100%",
            ),
            rx.vstack(
                rx.vstack(
                    rx.text("Settings", font_size="28px", font_style="Open Sans", font_weight="900"),
                    rx.text("Customize it for yourself", font_size="16px", font_style="Open Sans", font_weight="400",
                            color="gray"),
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
        ),
        rx.vstack(
            rx.center(
                rx.grid(
                    make_info_button("Tags", "Tags can help you with task classified", "You already have {0} tasks",
                                     BasicChipsState.tags.length(), BasicChipsState.initialize, "tag"),
                    make_info_button("Statuses", "Can help assess the load of task", "You already have {0} statuses",
                                     BasicChipsState.statuses.length(), BasicChipsState.initialize,
                                     "table-properties"),
                    make_info_button("Projects", "You can store tasks in projects", "You already have {0} projects",
                                     BasicChipsState.projects.length(), BasicChipsState.initialize, "folder-git-2"),
                    make_info_button("Lists", "You can create new or update old lists", "Work in {0}",
                                     "progress", BasicChipsState.initialize, "settings"),
                    columns="2",
                    spacing="5",
                    width="90%",
                    height="100%",
                ),
                width="100%",
                height="100%"
            ),
            width="100%",
            height="100%"
        ),
        render_footer(),
        width="100%",
        height="100%"
    )
