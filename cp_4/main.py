from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import home, weather
import uvicorn

api = FastAPI(
    title="FastAPI Weather"
)
api.mount('/static', StaticFiles(directory='./cp_4/static'), name='static')
api.include_router(home.router)
api.include_router(weather.router)

if __name__ == '__main__':
    uvicorn.run(api, port=8000, host='127.0.0.1')
