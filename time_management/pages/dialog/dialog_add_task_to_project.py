import reflex as rx

from ..beautiful_tag_selection import BasicChipsState

from time_management.database.models import Task


def task_select(task: Task) -> rx.Component:
    return rx.dialog.close(
        rx.button(
            rx.hstack(
                rx.text(task.name,
                        font_style="Open Sans",
                        font_size="14px",
                        weight="bold",
                        color="white"
                        ),
                align="center",
                position="relative",
                width="100%",
            ),
            width="100%",
            align_items="center",
            _hover={
                "opacity": "1",
            },
            opacity="0.75",
            cursor="pointer",
            bg="#191919",
            on_click=BasicChipsState.add_task_to_project(task)
        )
    )


def render_choose_menu() -> rx.Component:
    return rx.dialog.content(
        rx.center(
            rx.vstack(
                rx.scroll_area(
                    rx.vstack(
                        rx.flex(
                            rx.foreach(
                                BasicChipsState.project_available_tasks,
                                task_select
                            ),
                            direction="column",
                            bg="#181818",
                            align_items="center"
                        ),
                        width="90%",
                        bg="#181818",
                        margin="0px 3px"
                    ),
                    type="always",
                    scrollbars="vertical",
                    style={"height": 250},
                    padding="5px",
                    bg="#181818",
                    width="100%",
                ),
                align_items="center",
                bg="#191919",
                width="100%",
            ),
            height='100%',
            border="2px solid gray",
            bg="#191919",
            width="100%",
        ),
        padding="0px",
        width="90%",
    )
