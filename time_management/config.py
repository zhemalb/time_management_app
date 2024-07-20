from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

import os

load_dotenv()


class Settings(BaseSettings):
    DB_HOST: str = os.getenv("DB_HOST")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_PORT: int = os.getenv("DB_PORT")
    FIRST_SECRET: str = os.getenv("FIRST_SECRET")
    SECOND_SECRET: str = os.getenv("SECOND_SECRET")


settings = Settings()
