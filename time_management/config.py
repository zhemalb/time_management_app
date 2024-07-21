from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: int
    FIRST_SECRET: str
    SECOND_SECRET: str

    @property
    def get_connection_line(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
