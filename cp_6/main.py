
import models
from infrastructure.database import create_db_and_tables
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import router_list
import uvicorn
from env_configuration import Settings


def configure():
    get_settings()
    create_db_and_tables()
    configure_routing()


def get_settings():
    return Settings()

api = FastAPI(
    title="FastAPI Weather"
)


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    for i in router_list:
        api.include_router(i)


if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=Settings.local_port, host=Settings.local_host,)
else:
    configure()
