import reflex as rx
from typing import Optional

from time_management.database.models import User


class State(rx.State):
    user: Optional[User] = None
    settings: Optional[dict] = None

    def logout(self):
        self.user = None
        return rx.redirect("/")

    def check_login(self):
        if not self.logged_in:
            return rx.redirect("/login")

        return rx.redirect("/")

    @rx.var
    def logged_in(self) -> bool:
        return self.user is not None
