import reflex as rx
from .beautiful_tag_selection import BasicChipsState
from ..database.models import Status


class SpeedDialMenu(rx.ComponentState):
    is_open: bool = False
    is_typing_new: bool = False

    def toggle(self, value: bool):
        self.is_open = value

    def toggle_typing(self, value: bool):
        self.is_typing_new = value

    @classmethod
    def get_component(cls, **props):
        def menu_item(status: Status) -> rx.Component:
            return rx.vstack(
                rx.hstack(
                    rx.box(
                        height="20px",
                        width="20px",
                        border_radius="1000px",
                        bg=status.color,
                    ),
                    rx.text(f"{status.name} ({status.urgency})",
                            font_style="Open Sans",
                            font_size="14px",
                            weight="bold",
                            color="white"),
                    align="center",
                    opacity="0.75",
                    cursor="pointer",
                    position="relative",
                    _hover={
                        "opacity": "1",
                    },
                    width="100%",
                    align_items="center",
                    on_click=cls.toggle(False)
                ),
                rx.divider(margin="0"),
                width="100%",
                align_items="center",
            )

        def menu() -> rx.Component:
            return rx.box(
                rx.card(
                    rx.cond(
                        cls.is_typing_new,
                        rx.input(placeholder="test", width="100%"),
                        rx.button(
                            rx.text("(+) Новый статус", font_style="Open Sans", font_weight="bold",
                                    font_size="14px",
                                    color="white"),
                            width="100%",
                            bg="#181818",
                            _hover={
                                "opacity": "1",
                            },
                            opacity="0.75",
                            cursor="pointer",
                            align_items="center",
                            on_click=cls.toggle_typing(True)
                        ),
                    ),
                    rx.divider(margin="0"),
                    rx.scroll_area(
                        rx.vstack(
                            rx.flex(
                                rx.foreach(
                                    BasicChipsState.statuses,
                                    menu_item
                                ),
                                direction="row",
                                bg="#181818",
                                align_items="center"
                            ),
                            width="100%",
                            bg="#181818",
                            margin="0px 3px"
                        ),
                        scrollbars="horizontal",
                        style={"width": 90},
                        height="100%",
                        padding="5px",
                        bg="#181818",
                        width="auto",
                        min_width="15vw",
                    ),
                    height="15vh",
                    variant="ghost",
                    box_shadow="0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)",
                    border="2px solid gray",
                    align_items="end",
                    justify_content="end",
                ),
                position="absolute",
                bottom="100%",
                right="0",
                padding_bottom="10px",
            )

        return rx.vstack(
            rx.hstack(
                rx.button(
                    "Статусы",
                    variant="solid",
                    bg="#181818",
                    color="#777777",
                    font_style="Open Sans",
                    font_size="16px",
                    font_weight="bold",
                    size="3",
                    cursor="pointer",
                    position="relative",
                    border="2px solid gray",
                    on_click=cls.toggle(~cls.is_open),
                ),
                rx.cond(
                    cls.is_open,
                    menu(),
                ),
                position="relative"
            ),
            style={"bottom": "15px", "right": "15px"},
            # z_index="50",
            **props,
        )
