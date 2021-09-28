from models.locations_model import Location
from typing import List
from fastapi import APIRouter
from models.report_model import Report, ReportPost
from services import report_service


router = APIRouter(
    tags=["report"]
)

@router.get('/api/reports', name="all reports")
async def reports_get() -> List[Report]:
    return await report_service.get_reports()


@router.get(
    '/api/reports', 
    name="all reports",
    status_code=201,
    )
async def reports_post(report: ReportPost, location: Location) -> Report:
    d = report.description
    loc = location
    return await report_service.add_report(d, loc)
