import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.image(
                    src="/add_new_task.png",
                    height="40px",
                    width="40px",
                ),
                rx.hstack(
                    rx.text("Hi,", font_style="Open Sans", font_weight="regular", font_size="20px", align="left",
                            color="white"),
                    rx.text("Username", font_style="Open Sans", font_weight="bold", font_size="20px", align="left",
                            color="white"),
                    align_items="left",
                    padding="0px",
                    margin="0px",
                    bg="#181818",
                ),
                align="center",
                bg="#181818"
            ),
            rx.image(
                src="/add_new_task.png",
                height="40px",
                width="40px",
            ),
            justify="between",
            width="100%",
            padding="10px",
            bg="#181818"
        ),
        width="100%",
        bg="#181818",
    )
