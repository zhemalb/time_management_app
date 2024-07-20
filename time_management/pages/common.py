import reflex as rx


def make_input_with_icon(text, placeholder, icon: rx.icon, callback):
    return rx.vstack(
        rx.text(
            text,
            size="3",
            weight="medium",
            text_align="left",
            width="100%",
        ),
        rx.input(
            rx.input.slot(icon),
            placeholder=placeholder,
            type="email",
            size="3",
            width="100%",
            on_change=callback,
        ),
        justify="start",
        spacing="2",
        width="100%",
    )


def box_with_text(text, default: bool = False):
    return rx.box(
        rx.checkbox(
            text,
            default_checked=default,
            spacing="2",
        ),
        width="100%",
    ),
