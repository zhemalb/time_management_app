import reflex as rx


def empty_filled_input(value: str, placeholder: str, callback: callable):
    return rx.vstack(
        rx.chakra.input(
            placeholder=placeholder,
            value=value,
            on_change=callback,
            outline="none",
            variant="unstyled",
            width="90%",
            color="white"
        ),
        align_items="center",
        width="100%",
    )


def empty_filled_input_with_icon(value: str, placeholder: str, icon: str, type_: str, callback: callable):
    return rx.hstack(
        rx.icon(
            tag=icon,
            color="white"
        ),
        rx.input(
            value=value,
            placeholder=placeholder,
            type=type_,
            on_change=callback,
            size="2",
            outline="none",
            bg="#191919",
            width="100%",
            color="white"
        ),
        align_items="center",
        spacing="1",
        width="100%"
    )


def trigger_empty_filled_button_with_icon(value: str, icon: str):
    return rx.hstack(
        rx.icon(
            tag=icon,
            color="white",
            width="15%"
        ),
        rx.button(
            value,
            size="2",
            bg="#191919",
            width="85%",
            font_style="Open Sans",
            font_weight="bold",
            font_size="14px",
            color="white",
            opacity="0.75",
            _hover={
                "opacity": "1",
            }
        ),
        align_items="center",
        spacing="1",
    )


def empty_text_area(placeholder: str, callback: callable):
    return rx.chakra.text_area(
        placeholder=placeholder,
        on_change=callback,
        variant="unstyled",
        width="100%",
        color="white"
    )


def empty_selector(items: list, placeholder: str):
    return rx.chakra.select(
        items,
        placeholder=placeholder,
        outline="none",
        bg="#191919",
        width="100%",
        color="#777777",
        font_size="14px",
        font_style="Open Sans",
        border="none"
    )


def empty_checkbox_with_text(text: str, state: bool, callback: callable):
    return rx.chakra.hstack(
        rx.chakra.switch(
            is_checked=state,
            on_change=callback,
            color_scheme="green",
        ),
        rx.chakra.text(
            text,
            font_style="Open Sans",
            font_size="14px",
            font_weight="bold",
            color="#999999"
        ),
        spacing="1"
    )
