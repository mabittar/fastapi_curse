from datetime import datetime
from typing import List
from uuid import uuid4
from models import Location
from models import Report


__reports: List[Report] = []

def get_reports() -> List[Report]:
    
    return list(__reports)


def add_report(description) -> Report:
    now = datetime.now()
    uuid = str(uuid4())
    state = description.state if description.state is not None else None
    id = len(__reports) + 1
    report = Report(
        city=description.city,
        country=description.country,
        state=state, 
        description=description.description,
        created_at=now,
        uuid=uuid,
        id=id,
        )

    __reports.append(report)
    __reports.sort(key=lambda x: x.created_at, reverse=True)
    return report
