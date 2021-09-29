from typing import List
from fastapi import APIRouter
from models.report_model import Report, ReportPost
from services import report_service
from sqlmodel import Session
from infrastructure.database import engine
from services.report_service import ReportService


router = APIRouter(
    tags=["report"]
)

@router.get('/api/reports', name="all reports")
async def reports_get() -> List[Report]:
    with Session(engine) as session:
        report_service = ReportService(session)
        return report_service.get_reports()


@router.post(
    '/api/reports', 
    name="all reports",
    status_code=201,
    )
async def reports_post(report: ReportPost) -> Report:
    with Session(engine) as session:
        report_service = ReportService(session)
        return report_service.add_report(report)
