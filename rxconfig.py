import reflex as rx
from time_management.config import settings

config = rx.Config(
    app_name="time_management",
    db_url=settings.get_connection_line
)
