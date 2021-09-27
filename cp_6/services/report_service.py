from datetime import datetime
from typing import List
from models import Location
from models import Report


__reports: List[Report] = []

def get_reports() -> List[Report]:
    
    return list(__reports)


def add_report(description: str, location: Location) -> Report:
    now = datetime.datetime.now()
    report = Report(location=location, description=description, created_at=now)

    __reports.append(report)
    __reports.sort(key=lambda x: x.created_at, reverse=True)
    return report