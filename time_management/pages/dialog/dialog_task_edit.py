import reflex as rx

from ..beautiful_tag_selection import BasicChipsState, items_selector
from ..date_time_select import form_field
from ..sign_system import box_with_text

from .dialog_select_status import select_content
from .dialog_select_project import select_project
from .dialog_choose import render_choose_menu

from time_management.components.test_inputs import *

from time_management.database.models import Task


def render_task_edit(task: Task) -> rx.Component:
    return rx.dialog.content(
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.icon(tag="arrow-left", height="46px", color="white"),
                    rx.text("Edit Task", font_style="Open Sans", font_size="28px", font_weight="bold", color="#777777"),
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.icon_button(
                                rx.icon(
                                    tag="trash",
                                    color="white",
                                    height="20px",
                                    width="20px",
                                ),
                                variant="ghost",
                            ),
                        ), render_choose_menu("Вы действительно хотите удалить задачу?", "Да", "Нет",
                                              BasicChipsState.remove_task(task))
                    ),
                    justify="between",
                    height="50px",
                    width="100%",
                    display="flex",
                    align_items="center",
                    padding="10px"
                ),
                rx.vstack(
                    empty_filled_input(BasicChipsState.task_name, "Название задачи", BasicChipsState.set_task_name),
                    rx.grid(
                        rx.dialog.root(
                            rx.dialog.trigger(
                                trigger_empty_filled_button_with_icon(BasicChipsState.get_status_line,
                                                                      'flag-triangle-right'),
                            ), select_content(),
                        ),
                        rx.dialog.root(
                            rx.dialog.trigger(
                                trigger_empty_filled_button_with_icon(BasicChipsState.get_project_line,
                                                                      'folder-kanban'),
                            ), select_project()
                        ),
                        width="90%",
                        columns="2",
                        spacing="4",
                    ),
                    rx.vstack(
                        empty_filled_input_with_icon(BasicChipsState.task_date, "Дедлайн", "calendar-clock", "date",
                                                     BasicChipsState.set_task_date),
                        width="90%",
                    ),
                    width="100%",
                    display="flex",
                    margin_top="10px",
                    align_items="center",
                ),
                rx.vstack(
                    rx.hstack(
                        empty_checkbox_with_text("Делегируемая?", BasicChipsState.is_deligable,
                                                 BasicChipsState.set_is_deligable),
                        empty_checkbox_with_text("Сложная?", BasicChipsState.is_complex,
                                                 BasicChipsState.set_is_complex),
                        width="90%",
                        justify="between"
                    ),
                    width="100%",
                    display="flex",
                    align_items="center",
                ),
                rx.vstack(
                    rx.vstack(
                        empty_text_area(BasicChipsState.task_desc, "Описание", BasicChipsState.set_task_desc),
                        width="90%",
                    ),
                    align_items="center",
                    width="100%",
                    display="flex",
                ),
                rx.vstack(
                    items_selector(),
                    width="100%",
                    align_items="center"
                ),
                width="100%",
                height="100%"
            ),
            rx.vstack(
                rx.grid(
                    rx.dialog.close(
                        rx.chakra.button(
                            "Сохранить",
                            width="100%",
                            font_size="16px",
                            font_style="Open Sans",
                            font_weight="bold",
                            color="white",
                            variant="ghost",
                            on_click=BasicChipsState.update_task(task)
                        )
                    ),
                    rx.cond(
                        BasicChipsState.is_archive,
                        rx.dialog.root(
                            rx.dialog.trigger(
                                rx.chakra.button(
                                    "Убрать из архива",
                                    width="100%",
                                    font_size="16px",
                                    font_style="Open Sans",
                                    font_weight="bold",
                                    color="white",
                                    variant="ghost",
                                ),
                            ), render_choose_menu("Убрать из архива эту задачу?", "Да", "Нет",
                                                  BasicChipsState.remove_from_archive(task))
                        ),
                        rx.dialog.root(
                            rx.dialog.trigger(
                                rx.chakra.button(
                                    "Архивировать",
                                    width="100%",
                                    font_size="16px",
                                    font_style="Open Sans",
                                    font_weight="bold",
                                    color="white",
                                    variant="ghost",
                                ),
                            ), render_choose_menu("Добавить эту задачу в архив?", "Да", "Нет",
                                                  BasicChipsState.add_to_archive(task))
                        ),
                    ),
                    columns="2",
                    width="100%",
                    spacing="2"
                ),
                position="absolute",
                bottom="0",
                left="0",
                width="100%"
            ),
            height="100%",
            margin="0px",
            bg="#191919",
        ),
        height="80vh",
        padding="0px",
        width=["100%", "100%", "55%", "50%", "25%"],
    )
