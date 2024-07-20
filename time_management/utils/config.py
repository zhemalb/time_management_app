import reflex as rx


class LanguageConfig(rx.State):
    available_languages = [
        "english",
        "russian",
    ]

    lang: str = "russian"

    def change_language(self, language: str):
        self.lang = language

    @rx.var
    def language(self) -> dict[str, dict[str, str]]:
        return language_data[self.lang]


language_data = {
    "english": {
        "register": {
            "title": "Create an account",
            "email_text": "Email address",
            "email_placeholder": "example@google.com",
            "password_text": "Password",
            "password_placeholder": "Enter your password",
            "repeat_password_text": "Repeat Password",
            "repeat_password_placeholder": "Repeat your password",
            "confirm_with_rules": "Agree to Terms and Conditions",
            "button_text": "Sign up",
            "already_registered": "Already registered?",
            "login_link": "Sing in",
        }
    },
    "russian": {
        "register": {
            "title": "Создание аккаунта",
            "email_text": "Адрес электронной почты",
            "email_placeholder": "example@google.com",
            "password_text": "Пароль",
            "password_placeholder": "Введите ваш пароль",
            "repeat_password_text": "Повторите пароль",
            "repeat_password_placeholder": "Введите ваш пароль снова",
            "confirm_with_rules": "Я согласен с лицензионным соглашением и правилами",
            "button_text": "Зарегистрироваться",
            "already_registered": "Уже зарегистрирован?",
            "login_link": "Войти",
        }
    }
}
