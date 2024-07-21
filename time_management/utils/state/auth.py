import reflex as rx
from sqlmodel import select

from .base import State, User


class AuthState(State):
    email: str
    username: str = "test"
    password: str
    confirm_password: str

    def signup(self):
        with rx.session() as session:
            if self.password != self.confirm_password:
                return rx.window_alert("Пароли не совпадают")

            if session.exec(select(User).where(User.email == self.email)).first():
                return rx.window_alert("Пользователь с таким email уже зарегистрирован")

            self.user = User(email=self.email, name=self.username, password=self.password)
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()

            return rx.redirect("/")

    def login(self):
        with rx.session() as session:
            origin_user = session.exec(
                select(User).where(User.email == self.email)
            ).first()

            if origin_user and origin_user.password == self.password:
                self.user = origin_user
                return rx.redirect("/")
            else:
                return rx.window_alert("Неправильный email или пароль")
