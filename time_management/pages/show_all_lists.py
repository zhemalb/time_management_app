import reflex as rx

from .beautiful_tag_selection import BasicChipsState
from .footer import render_footer


def render_list_button(callback: callable, icon_tag: str, title: str, desc: str, format_line: str,
                       param):
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
            height="100%",
        ),
        padding="5px",
        background_color="white",
        border_radius="12px",
        border="2px solid #202020",
        width="100%",
        height="100%",
        on_click=callback
    )


def render_all_lists():
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
                    rx.text("All lists", font_size="28px", font_style="Open Sans", font_weight="900"),
                    rx.text("Grouped tasks for all your purposes", font_size="16px", font_style="Open Sans",
                            font_weight="400",
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
                    render_list_button(BasicChipsState.initialize, "shopping-basket", "Basket",
                                       "Storage of all your tasks",
                                       "{0} tasks in your bucket", 13),
                    render_list_button(BasicChipsState.initialize, "tag", "Long Term Tasks",
                                       "You can think about they later",
                                       "You have {0} long term tasks", 13),
                    render_list_button(BasicChipsState.initialize, "users", "Delegable Tasks",
                                       "Someone else will make it for you",
                                       "You have {0} delegable tasks", 13),
                    render_list_button(BasicChipsState.initialize, "clock-5", "Postponed Tasks",
                                       "Someday then definitely...",
                                       "You have {0} postponed tasks", 13),
                    columns="1",
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
    ),
