# from django.db import models

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Event(BaseModel):
    created_at: str
    started_at: str
    finished_at: str
    title: str
    description: str
    depends_on: Optional[str]
    status: str
