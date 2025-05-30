from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",            # 配置文件路径
        case_sensitive=True,        # 大小写是否敏感
        extra="allow",              # 是否允许额外的输入
        validate_default=False,     # 是否校验配置
    )

    # FastApi
    SECRET_KEY: str = Field(env="SECRET_KEY")
    API_TITLE: str = Field(env="API_TITLE")
    API_DESCRIPTION: str = Field(env="API_DESCRIPTION")
    API_SUMMARY: str = Field(env="API_SUMMARY")
    API_VERSION: str = Field(env="API_VERSION")
    API_PREFIX: str = Field(env="API_PREFIX")
    API_CONTACT_NAME: str = Field(env="API_CONTACT_NAME")
    API_CONTACT_URL: str = Field(env="API_CONTACT_URL")
    API_CONTACT_EMAIL: str = Field(env="API_CONTACT_EMAIL")
    API_LICENSE_NAME: str = Field(env="API_LICENSE_NAME")
    API_LICENSE_URL: str = Field(env="API_LICENSE_URL")
    API_LICENSE_IDENTIFIER: str = Field(env="API_LICENSE_IDENTIFIER")
    BACKEND_CORS_ORIGINS: str = Field(env="BACKEND_CORS_ORIGINS")
    PROJECT_NAME: str = Field(env="PROJECT_NAME")


@lru_cache()
def get_settings():
    return Settings()
