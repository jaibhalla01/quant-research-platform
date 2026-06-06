from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, PostgresDsn, Field

from typing import Annotated
from src.core.enums import Environment, LogLevel


class Settings(BaseSettings):

    # Application metadata
    app_name: str = "Quant Research Platform"
    app_version: str = "0.1.0"

    # Set up environment as a class to avoid typos and maintain type-safety
    environment: Environment = Environment.DEVELOPMENT

    log_level: LogLevel = LogLevel.INFO

    # Secret string hides the api_key in the logs/repr output
    alpaca_api_key: SecretStr
    alpaca_secret_key: SecretStr

    # repr=False prevents the url from showing in the terminal
    database_url: PostgresDsn = Field(repr=False)

    port: Annotated[int, Field(ge=1, le=65535)] = 8000

    # Get machine specific variables from .env file
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

