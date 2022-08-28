from pydantic import BaseModel
from typing import Optional


class Event(BaseModel):
    id: str
    created_at: str
    started_at: str
    finished_at: str
    title: str
    description: str
    depends_on: Optional[str]
    status: str
