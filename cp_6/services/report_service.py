from datetime import datetime
from typing import List
from uuid import uuid4

from sqlmodel import select
from models import Report

class ReportService():
    def __init__(self, session):
        self.session = session

    def get_reports(self) -> List[Report]:
        statement = select(Report)
        results = self.session.exec(statement).all()
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
