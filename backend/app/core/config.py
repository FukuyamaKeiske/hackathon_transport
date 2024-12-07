from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    YANDEX_MAPS_API_KEY: str
    DGIS_API_KEY: str
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
