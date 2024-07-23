import reflex as rx


def form_field(
        label: str, placeholder: str, type: str, name: str, callback: callable, width: str = "100%",
        background: str = "white"
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.text(label, font_size="14px", font_weight="bold", font_family="Open Sans", color="black"),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    type=type,
                    border_radius="10px",
                    background_color=background,
                    border="1px solid #202020",
                    color="white",
                    font_family="Open Sans",
                    font_size="14px",
                    font_weight="bold",
                    on_change=callback
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width=width,
    )


def event_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="calendar-plus", size=32),
                    color_scheme="mint",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Create an event",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Fill the form to create a custom event",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    form_field(
                        "Event Name",
                        "Event Name",
                        "text",
                        "event_name",
                    ),
                    rx.flex(
                        form_field(
                            "Date", "", "date", "event_date"
                        ),
                        form_field(
                            "Time", "", "time", "event_time"
                        ),
                        spacing="3",
                        flex_direction="row",
                    ),
                    form_field(
                        "Description",
                        "Optional",
                        "text",
                        "description",
                    ),
                    direction="column",
                    spacing="2",
                ),
                rx.form.submit(
                    rx.button("Create"),
                    as_child=True,
                    width="100%",
                ),
                on_submit=lambda form_data: rx.window_alert(
                    form_data.to_string()
                ),
                reset_on_submit=False,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )
