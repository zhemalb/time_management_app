import reflex as rx


def render_footer():
    return rx.hstack(
        rx.button(
            rx.image(
                src="actual_tasks.png",
                height="60%",
            ),
            height="100%",
            bg="white",
            text_align="center",
        ),
        rx.button(
            rx.image(
                src="all_tasks.png",
                height="60%",
            ),
            height="100%",
            bg="white",
            text_align="center",
        ),
        rx.button(
            rx.image(
                src="add_new_task.png",
                height="60%",
            ),
            height="100%",
            bg="white",
            text_align="center",
        ),
        rx.button(
            rx.image(
                src="all_lists.png",
                height="60%",
            ),
            height="100%",
            bg="white",
            text_align="center",
        ),
        rx.button(
            rx.image(
                src="projects.png",
                height="60%",
            ),
            height="100%",
            bg="white",
            text_align="center",
        ),
        height="5%",
        justify="between",
        bg_color="white",
        border_radius="12px 12px 0px 0px",
        border_top="2px solid gray",
        width="100%",
        position="absolute",
        bottom="0",
        left="0"
    )
