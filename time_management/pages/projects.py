import reflex as rx

from ..components.header import header
from ..database.models import Project

from .footer import render_footer
from .beautiful_tag_selection import BasicChipsState


def render_project_badge(project: Project) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(
                project.name,
                font_style="Open Sans",
                font_weight="bold",
                font_size="24px",
                color="white",
                on_click=BasicChipsState.choose_project(project)
            ),
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.icon_button(
                        rx.icon(
                            tag="x",
                            height="24px",
                            color="white"
                        ),
                        variant="ghost",
                    ),
                ),
                rx.dialog.content(
                    rx.center(
                        rx.vstack(
                            rx.text(
                                "Вы действительно хотите удалить этот проект?",
                                font_style="Open Sans",
                                font_weight="bold",
                                font_size="20px",
                                color="white",
                                align="center"
                            ),
                            rx.grid(
                                rx.dialog.close(
                                    rx.chakra.button(
                                        "Нет",
                                        variant="ghost",
                                        font_style="Open Sans",
                                        font_size="18px",
                                        color="white"
                                    ),
                                    rx.chakra.button(
                                        "Да",
                                        variant="ghost",
                                        on_click=BasicChipsState.delete_project(project),
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
            ),
            width="100%",
            justify="between",
            height="100%"
        ),
        rx.vstack(
            rx.scroll_area(
                rx.flex(
                    rx.text(
                        project.desc,
                        color="#777777",
                        font_style="Open Sans",
                        font_weight="regular",
                        font_size="14px",
                        trim="both"
                    ),
                    direction="column",
                    spacing="4",
                    width="90vw",
                ),
                type="always",
                scrollbars="vertical",
                style={"height": 50},
            ),
            width="100%",
            on_click=BasicChipsState.choose_project(project)
        ),
        rx.hstack(
            rx.text(
                f"Задач: {BasicChipsState.tasks_count_of_projects[project.id.to_int()]}",
                font_style="Open Sans",
                font_weight="bold",
                font_size="15px",
                color="white"
            ),
            rx.text(
                "Нажми для подробностей",
                font_style="Open Sans",
                font_weight="bold",
                font_size="15px",
                color="white"
            ),
            width="100%",
            heigght="100%",
            justify="between",
            on_click=BasicChipsState.choose_project(project)
        ),
        bg="#191919",
        border_radius="12px",
        border="2px solid",
        border_color=project.color,
        width="100%",
        height="100%",
        padding="8px",
    )


def render_projects_page():
    return rx.vstack(
        rx.vstack(
            header(),
            min_height="50px",
            width="100%",
            position="fixed",
            top="0",
        ),
        rx.vstack(
            rx.vstack(
                rx.text("Projects", font_size="28px", font_style="Open Sans", font_weight="900",
                        color="white"),
                rx.text("Tasks grouped by projects", font_size="16px", font_style="Open Sans", font_weight="400",
                        color="#777777"),
                align_items="left",
                spacing="0",
                padding="0px",
                width="90%",
                height="100%"
            ),
            rx.vstack(
                rx.scroll_area(
                    rx.flex(
                        rx.foreach(
                            BasicChipsState.projects,
                            render_project_badge
                        ),
                        direction="column",
                        width="90vw",
                        spacing="4",
                    ),
                    type="always",
                    scrollbars="vertical",
                    width="90vw",
                    min_height="65vh",
                ),
                height="100%",
                width="90%"
            ),
            width="100%",
            height="100%",
            align_items="center"
        ),
        rx.vstack(
            render_footer("project"),
            position="absolute",
            bottom="0",
            width="100%",
            min_height="50px",
        ),
        width=["100%", "100%", "55%", "50%", "35%"],
        bg="#191919",
        padding="0px",
        box_shadow="0px 8px 16px 6px rgba(0, 0, 0, 0.25)"
    )
