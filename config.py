from functools import lru_cache

from pydantic import ConfigDict, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI Blog"
    debug: bool = False
    static_dir: str = "static"
    templates_dir: str = "templates"
    default_post_date: str = "April 23, 2025"
    secret_key:SecretStr
    algorithm:str = "HS256"
    access_token_expire_minutes: int=30
    s3_bucket_name: str | None = None
    max_upload_size_bytes: int = 5 * 1024 * 1024
    posts_per_page:int = 10
    reset_token_expire_minutes: int = 60
    mail_server: str = "localhost"
    mail_port: int = 587
    mail_username: str = ""
    mail_password: SecretStr = SecretStr("")
    mail_from: str = "noreply@example.com"
    mail_use_tls: bool = True
    frontend_url: str = "http://localhost:8000"

    database_url: str
    
    # S3 Configuration. it's |none when inside aws ecosystem, otherwise it should be set in .env

    s3_region: str = "us-east-2"
    s3_access_key_id: SecretStr | None = None
    s3_secret_access_key: SecretStr | None = None
    s3_endpoint_url: str | None = None
    
    @field_validator("debug", mode="before")
    @classmethod
    def parse_debug(cls, value: object) -> object:
        if isinstance(value, str) and value.lower() in {"release", "prod", "production"}:
            return False
        return value

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()


# type: ignore[call-arg]
settings = get_settings()
