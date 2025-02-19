from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_host: str = Field(..., env='DB_HOST')
    db_port: str = Field(..., env='DB_PORT')
    db_name: str = Field(..., env='DB_NAME')
    db_user: str = Field(..., env='DB_USER')
    db_password: str = Field(..., env='DB_PASSWORD')

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

settings = Settings()