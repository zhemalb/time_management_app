import reflex as rx
from .base import State, User
from time_management.database.core import get_user_with_email, add_new_user


class AuthState(State):
    email: str
    username: str = "hello"
    password: str
    confirm_password: str

    def signup(self):
        if self.password != self.confirm_password:
            return rx.window_alert("Пароли не совпадают")

        if get_user_with_email(self.email):
            return rx.window_alert("Пользователь с таким email уже зарегистрирован")

        self.user = User(remail=self.email, username=self.username, password=self.password)
        add_new_user(self.user)

        return rx.redirect("/")
