import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/calculate')
def calculate():
    value = 2 + 2
    result = dict(
        value=value
    )
    return result

uvicorn.run(api, port=8000, host='127.0.0.1')