from typing import Optional
from sqlmodel import Field, SQLModel
from models import Location
from datetime import datetime


class Report(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str = Field(
        description="Natural Event to be Reported", min_length=1, max_length=226)
    city: str = Field(description="Enter the city name to get weather now")
    state: Optional[str] = Field(
        min_length=2, max_length=2, description="State must be Alpha-2 code")
    country: Optional[str] = Field(
        default="BR", min_length=2, max_length=2, description="Country must be Alpha-2 code")
    created_at: Optional[datetime] = None

