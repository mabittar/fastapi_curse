from sqlmodel import Field, SQLModel
from typing import Optional

class Location(SQLModel):
    city: str
    state: Optional[str]
    country: Optional[str] = Field(default="US")
