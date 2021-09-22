
from fastapi import APIRouter, responses
from jinja2.environment import Template
from starlette.requests import Request
from starlette.templating import Jinja2Templates


templates = Jinja2Templates('templates')
router = APIRouter(tags=["home"],)


@router.get('/')
def index(request: Request):
    return Template.TemplateResponse('index.html', {'request': request})


@router.get('/favicon.ico')
def favicon():
    return responses.RedirectResponse(urls='cp_4/static/img/favicon.ico')
