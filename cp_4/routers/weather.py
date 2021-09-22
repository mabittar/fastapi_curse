from fastapi import APIRouter

router = APIRouter(
    prefix="/api/weather",
    tags=["weather"]
)


@router.get('/')
def weather():
    return "Some report"
