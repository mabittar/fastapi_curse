from typing import Optional
import fastapi
import uvicorn
from fastapi.exceptions import HTTPException

api = fastapi.FastAPI()

@api.get('/calculate', 
description="This endpoint calculate (x + y) op z.", 
response_description="Successful Response", 
status_code=200
)
def calculate(
    x: int, 
    y: int, 
    z: Optional[int] = None, 
    op: Optional[str] = None,
    ):

    if z == 0:
        return fastapi.responses.JSONResponse(
            content={"error": "ERROR: Z cannot be zero."},
            status_code=400
        )
    if (op is None and z is not None) or (op is not None and z is None):
        return fastapi.responses.JSONResponse(
            content={"error": "ERROR: if Z or op is used, an operator or z must be sent."},
            status_code=400
        )


    value = (x + y)
    if op == "+":
        value = value + z
    elif op == "-":
        value = value - z
    elif op == "*":
        value = value * z
    elif op == "/":
        value = value / z
    elif op is None:
        value = (x + y)
    else:
        return fastapi.responses.JSONResponse(
            content={"error": "Operator: not implanted yet. Try only +. -, *, /."},
            status_code=400
        )



    result = dict(
        value=value
    )
    return result

uvicorn.run(api, port=8000, host='127.0.0.1')
