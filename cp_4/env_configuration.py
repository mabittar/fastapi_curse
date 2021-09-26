from pydantic import BaseSettings, Field, fields
import os
from dotenv.main import load_dotenv


class Settings(BaseSettings):
    service_root = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.abspath(os.path.join(service_root, os.pardir))

    project_name: str = Field(default="fastapi_starter", env="PROJECT_NAME")
    api_key: str = Field(default=None, env="API_KEY")
    openweather_timeout: int = Field(default=360, env="OPENWEATHER_TIMEOUT")

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
print(f"starting: {settings.project_name}")
