from datetime import datetime
from typing import List, Optional
from uuid import uuid4
from infrastructure.database import get_session

from sqlmodel import Session, select
from models import Report

class ReportService():
    def __init__(self, session = None):
        self.session = session if session is not None else get_session()

    def get_reports(
        self,
        page: Optional[int] = 0,
        page_size: Optional[int] = 10
        ) -> List[Report]:
        statement = select(Report).offset(page).limit(page_size)
        results = self.session.exec(select(Report).offset(page).limit(page_size)).all()
        return results

    async def get_report(
        self, 
        id: Optional[id] = None,
        city: Optional[str] = None,
        page: Optional[int] = 0,
        page_size: Optional[int] = 10,
        first_result: Optional[bool] = False,
    ):
        results = self.session.get(Report, id)

        return results


    def add_report(self, data) -> Report:
        now = datetime.now()
        uuid = str(uuid4())
        state = data.state if data.state is not None else None
        report = Report(
            city=data.city,
            country=data.country,
            state=state, 
            description=data.description,
            created_at=now,
            uuid=uuid
            )

        self.session.add(report)
        self.session.commit()
        self.session.refresh(report)
        return report
