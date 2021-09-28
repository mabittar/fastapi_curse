from pydantic import BaseSettings, Field, fields
import os
from dotenv.main import load_dotenv


class Settings(BaseSettings):
    service_root = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.abspath(os.path.join(service_root, os.pardir))
    path = os.getcwd()
    project_name: str = Field(default="fastapi_starter", env="PROJECT_NAME")
    api_key: str = Field(default=None, env="API_KEY")
    openweather_timeout: int = Field(default=360, env="OPENWEATHER_TIMEOUT")
    lifetime_in_hours: int = Field(
        default=1.0, ge=0, le=24, env="LIFETIME_CACHE_HOURS")
    database_file_name: str = Field(default="database.db", env="DB_FILE")
    local_host: str = Field(default='http://127.0.0.1', env="LOCAL_HOST")
    local_port: int = Field(default=8000, env="LOCAL_PORT")
    url: str = f'{local_host}:{local_port}'
    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
print(f"starting: {settings.project_name} on {settings.url}")
