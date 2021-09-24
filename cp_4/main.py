from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import router_list
import uvicorn


def configure():
    configure_routing()

api = FastAPI(
    title="FastAPI Weather"
)


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    for i in router_list:
        api.include_router(i)


if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1',)
else:
    configure()
