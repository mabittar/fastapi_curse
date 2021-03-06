from typing import Optional
from fastapi import APIRouter
from models.locations_model import Location
from fastapi import Depends
from services.location_service import LocationService

router = APIRouter(
    tags=["weather"]
)


@router.get('/api/weather/{city}')
async def weather(
    loc: Location = Depends(),
    unit: Optional[str] = "metric"
    ) -> dict:

    report = await LocationService.get_report_async(
        city=loc.city,
        state=loc.state,
        country=loc.country,
        unit=unit
    )

    return report
