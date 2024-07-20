import reflex as rx


def render_footer():
    return rx.hstack(
        rx.center(
            rx.button(
                rx.icon(tag="heart")
            ),
            bg_color="red",
        ),
        rx.center(
            rx.button(
                rx.icon(tag="heart"),
                size="3",
                width="10%",
            ),
            rx.button(
                rx.icon(tag="heart"),
                size="3",
                width="10%",
            ),
            rx.button(
                rx.icon(tag="heart"),
                size="3",
                width="10%",
            ),
            width="100%",
            spacing="3",
            bg_color="cyan",
        ),
        rx.center(
            rx.button(
                rx.icon(tag="heart")
            ),
            bg_color="green",
        ),
        bg_color="#696969",
        width="100%"
    )
