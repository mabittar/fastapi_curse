from datetime import datetime
from typing import List
from uuid import uuid4
from models import Location
from models import Report


__reports: List[Report] = []

def get_reports() -> List[Report]:
    
    return list(__reports)


def add_report(description: str, location: Location) -> Report:
    now = datetime.datetime.now()
    uuid = str(uuid4())
    state = location.state if location.state is not None else None
    report = Report(
        city=location.city,
        country=location.country,
        state=state, 
        description=description, 
        created_at=now,
        uuid=uuid,
        )

    __reports.append(report)
    __reports.sort(key=lambda x: x.created_at, reverse=True)
    return report
