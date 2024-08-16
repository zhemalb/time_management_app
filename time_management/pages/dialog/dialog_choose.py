import reflex as rx


def render_choose_menu(text: str, accept_text: str, denied_text: str, callback: callable):
    return rx.dialog.content(
        rx.center(
            rx.vstack(
                rx.text(
                    text,
                    font_style="Open Sans",
                    font_weight="bold",
                    font_size="20px",
                    color="white",
                    align="center"
                ),
                rx.grid(
                    rx.dialog.close(
                        rx.chakra.button(
                            denied_text,
                            variant="ghost",
                            font_style="Open Sans",
                            font_size="18px",
                            color="white"
                        ),
                        rx.chakra.button(
                            accept_text,
                            variant="ghost",
                            on_click=callback,
                            font_style="Open Sans",
                            font_size="18px",
                            color="white"
                        )
                    )
                ),
                width="100%",
                height="100%",
                align_items="center"
            ),
            width="100%",
            bg="#191919",
        ),
        padding="0",
        bg="#191919"
    )
