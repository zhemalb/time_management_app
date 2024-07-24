import reflex as rx

from ..beautiful_tag_selection import BasicChipsState, items_selector
from ..date_time_select import form_field
from ..common import box_with_text


def make_header_input(title: str, placeholder: str, callback: callable, is_password: bool = False, width: str = "100%",
                      default=""):
    return rx.vstack(
        rx.text(title, color="black", font_size="14px", font_family="Open Sans", font_weight="bold"),
        rx.chakra.input(
            placeholder=placeholder,
            type_="text" if not is_password else "password",
            border="2px solid #202020",
            border_radius="20px",
            font_family="Open Sans",
            font_size="14px",
            font_weight="bold",
            color="white",
            default_value=default,
            on_change=callback
        ),
        width=width,
        spacing="1"
    )


def make_text_area(title: str, placeholder: str, callback: callable, default=""):
    return rx.vstack(
        rx.text(title, color="black", font_size="14px", font_family="Open Sans", font_weight="bold"),
        rx.text_area(
            placeholder=placeholder,
            type="text",
            border="2px solid #202020",
            border_radius="20px",
            font_family="Open Sans",
            font_size="14px",
            font_weight="bold",
            width="100%",
            value=default,
            color="black",
            on_change=callback,
        ),
        width="100%",
        spacing="1"
    )


def render_action_button(text: str, callback: callable):
    return rx.button(
        text,
        color_scheme="red",
        variant="solid",
        font_size="18px",
        width="100%",
        size="3",
        font_weight="bold",
        border_radius="20px",
        padding="1em 0em",
        on_click=callback,
        font_family="Open Sans"
    )


def render_select_with_text(text: str, placeholder: str, collection: list, callback: callable, width="100%",
                            default=""):
    return rx.vstack(
        rx.text(text, color="black", font_size="14px", font_family="Open Sans", font_weight="bold"),
        rx.select(
            collection,
            placeholder=placeholder,
            on_change=callback,
            width="100%",
            radius="large",
            default_value=default,
            position="popper",
        ),
        spacing="1",
        width=width
    )


def render_dialog_header() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.hstack(
                rx.dialog.close(
                    rx.button(
                        rx.image(
                            src="/back_button.png",
                            height="110%",
                        ),
                        display="block",
                        bg_color="red",
                        on_click=BasicChipsState.remove_selection
                    ),
                ),
                rx.text("Create new task", font_size="6vw", font_weight="700", font_family="Open Sans", color="black"),
                rx.button(
                    rx.image(
                        src="/info_button.png",
                        height="110%",
                    ),
                    display="block",
                    bg_color="red",
                ),
                height="100%",
                width="100%",
                align_items="center",
                justify="between",
                margin="5px 5px",
            ),
            rx.text("You can create tasks here", font_size="14px", font_weight="500", font_family="Open Sans",
                    color="white"),
            width="100%",
            height="100%",
            align_items="center",
            spacing="1"
        ),
        rx.vstack(
            make_header_input("Task name", "Task name here", BasicChipsState.set_task_name),
            rx.form.root(
                rx.hstack(
                    form_field(
                        "Date", "", "date", "event_date", BasicChipsState.set_task_date, width="75%", background="red"
                    ),
                    form_field(
                        "Time", "", "time", "event_time", BasicChipsState.set_task_time, width="20%", background="red"
                    ),
                    justify="between",
                    width="100%",
                ),
                width="100%",
            ),
            width="90%",
            height="100%",
            margin_bottom="10px",
            spacing="4",
        ),
        spacing="5",
        bg_color="red",
        width="100%",
        align_items="center",
        border_radius="0px 0px 12px 12px"
    )


def render_dialog_content() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            make_text_area("Description", "Enter task description here", BasicChipsState.set_task_desc),
            width="100%",
        ),
        rx.hstack(
            rx.vstack(
                render_select_with_text("Status", "Choose status", BasicChipsState.statuses,
                                        BasicChipsState.select_status),
                box_with_text("Note", BasicChipsState.set_is_info),
                box_with_text("Delegable", BasicChipsState.set_is_deligable),
            ),
            rx.vstack(
                render_select_with_text("Project", "Choose project", BasicChipsState.projects,
                                        BasicChipsState.select_project),
                box_with_text("Complex task", BasicChipsState.set_is_complex),
            ),
            width="100%",
            justify="between"
        ),
        rx.vstack(
            rx.text("Select tags", font_size="14px", font_weight="bold", font_family="Open Sans", color="black"),
            items_selector(),
            width="100%",
            margin_bottom="15px",
            spacing="1",
        ),
        width="90%",
        height="100%",
        bg_color="white",
        margin="0px",
        align_items="center"
    )


def render_footer() -> rx.Component:
    return render_action_button("Create task", BasicChipsState.create_task)


def make_dialog_content() -> rx.Component:
    return rx.dialog.content(
        rx.center(
            rx.vstack(
                rx.vstack(
                    render_dialog_header(),
                    rx.vstack(
                        render_dialog_content(),
                        width="100%",
                        align_items="center",
                    ),
                    width="100%",
                    height="100%",
                    magrin="0px",
                    padding="0px",
                ),
                rx.vstack(
                    render_footer(),
                    width="100%",
                    height="7%",
                    padding="0px",
                    margin="0px"
                ),
                width="100%",
                height="100%",
            ),
            width="100%",
            height="100%",
            margin="0px"
        ),
        height="80vh",
        width="94vw",
        padding="0px",
        align_items="center"
    )
