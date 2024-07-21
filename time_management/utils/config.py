import reflex as rx


class LanguageConfig(rx.State):
    available_languages = [
        "english",
        "russian",
    ]

    lang: str = "english"

    def change_language(self, language: str):
        self.lang = language

    @rx.var
    def language(self) -> dict[str, dict[str, str]]:
        return language_data[self.lang]


language_data = {
    "english": {
        "common": {
            "back_button": "< Back",
        },
        "register": {
            "title": "Registration",
            "username_text": "Username",
            "username_placeholder": "Enter username",
            "email_text": "Email",
            "email_placeholder": "example@google.com",
            "password_text": "Password",
            "password_placeholder": "Enter your password",
            "repeat_password_text": "Repeat Password",
            "repeat_password_placeholder": "Repeat your password",
            "button_text": "Sign up",
            "already_registered": "Already registered?",
            "already_registered_action": "Sign in",
            "login_link": "Sing in",
            "vk_auth": "Sign up with VKontakte",
            "arrangement_rules": "I agree with",
            "rules_name": "User terms",
            "other_rules_name": "Conditions",
            "remember_me": "Remember me",
            "forgot_password": "Forgot password?",
        },
        "login": {
            "title": "Welcome back!",
            "vk_auth": "Sign in with VKontakte",
            "dont_have_account": "Don't have account?",
            "dont_have_account_action": "Sign up",
        }
    },
    "russian": {
        "register": {
            "title": "Создание аккаунта",
            "email_text": "Электронная почта",
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
