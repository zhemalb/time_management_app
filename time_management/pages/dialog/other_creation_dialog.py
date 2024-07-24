import reflex as rx
from .dialog_tasks import make_header_input, make_text_area, render_action_button
from ..beautiful_tag_selection import BasicChipsState


class PropCondState(rx.State):
    value: list[int] = [50]

    def set_end(self, value: int):
        self.value = [value]


def cond_prop():
    return rx.slider(
        min_value=0,
        max_value=9,
        step=1,
        default_value=[50],
        on_value_commit=PropCondState.set_end,
        color_scheme=rx.cond(
            PropCondState.value[0] > 5, "green", "pink"
        ),
        width="100%",
    )


def render_status_creation_dialog() -> rx.Component:
    return rx.dialog.content(
        rx.center(
            rx.vstack(
                rx.text(
                    "Create New Status",
                    font_size="6vw",
                    font_weight="700",
                    font_family="Open Sans",
                    color="black"
                ),
                make_header_input("Status Name", "Enter status name", BasicChipsState.set_status_name),
                make_text_area("Description", "Enter description", BasicChipsState.set_status_desc),
                cond_prop(),
                render_action_button("Create Status", BasicChipsState.create_status()),
                width="90%",
                height="100%",
                margin_bottom="10px",
                spacing="4",
            ),
            width="100%",
            height="100%",
            margin="0px"
        ),
        height="50vh",
        width="60vw",
        padding="0px",
        align_items="center"
    )


def render_tag_creation_dialog() -> rx.Component:
    return rx.dialog.content(
        rx.center(
            rx.vstack(
                rx.text("Create New Tag", font_size="6vw", font_weight="700", font_family="Open Sans", color="black"),
                make_header_input("Tag Name", "Enter tag name", BasicChipsState.set_tag_name),
                make_text_area("Description", "Enter description", BasicChipsState.set_tag_desc),
                render_action_button("Create Tag", BasicChipsState.create_tag()),
                width="90%",
                height="100%",
                margin_bottom="10px",
                spacing="4",
            ),
            width="100%",
            height="100%",
            margin="0px"
        ),
        height="50vh",
        width="60vw",
        padding="0px",
        align_items="center"
    )
