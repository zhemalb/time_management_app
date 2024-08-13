import reflex as rx
from typing import Optional

from sqlmodel import select

from time_management.database.models import User
from time_management.database.database import sql_execute


class State(rx.State):
    user: Optional[User] = rx.session().exec(select(User).where(User.id == 1)).one()

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
