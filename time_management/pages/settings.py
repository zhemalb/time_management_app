import reflex as rx
from .beautiful_tag_selection import BasicChipsState
from .footer import render_footer


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
                    rx.button(
                        rx.text("Task", font_style="Open Sans", font_size="16px", font_weight="bold", color="black"),
                        padding="25% 0px",
                        background_color="white",
                        border_radius="12px",
                        border="2px solid #202020",
                    ),
                    rx.button(
                        rx.text("Project", font_style="Open Sans", font_size="16px", font_weight="bold", color="black"),
                        padding="25% 0px",
                        background_color="white",
                        border_radius="12px",
                        border="2px solid #202020",
                    ),
                    rx.button(
                        rx.text("Status", font_style="Open Sans", font_size="16px", font_weight="bold", color="black"),
                        padding="25% 0px",
                        background_color="white",
                        border_radius="12px",
                        border="2px solid #202020",
                    ),
                    rx.button(
                        rx.text("Other", font_style="Open Sans", font_size="16px", font_weight="bold", color="black"),
                        padding="25% 0px",
                        background_color="white",
                        border_radius="12px",
                        border="2px solid #202020",
                    ),
                    columns="2",
                    spacing="4",
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
