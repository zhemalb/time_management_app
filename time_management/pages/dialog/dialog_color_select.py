import reflex as rx

from ..beautiful_tag_selection import BasicChipsState


def close_color_button(color: str, callback: callable):
    return rx.button(
        bg=color,
        width="20px",
        height="20px",
        border_radius="1000px",
        on_click=callback,
    )


COLORS_TABLE = [
    "#1abc9c", "#2ecc71", "#3498db", "#9b59b6", "#34495e",
    "#f1c40f", "#e67e22", "#e74c3c", "#ecf0f1", "#95a5a6",
    "#786fa6", "#c44569"
]


def render_select_dialog(callback: callable) -> rx.Component:
    return rx.dialog.content(
        rx.scroll_area(
            rx.grid(
                rx.foreach(
                    COLORS_TABLE,
                    lambda i: rx.dialog.close(close_color_button(i, callback(i))),
                ),
                columns="4",
                spacing="3",
                width="100%"
            ),
            scroll="always",
            scrollbars="vertical",
            width="100%",
        ),
        style={"width": 150, "height": 80},
        align="center",
        padding="2px 0px 2px 2px",
        side="right"
    )
