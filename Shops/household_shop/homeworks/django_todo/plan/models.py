from django.db import models
from datetime import date
from enum import Enum
from uuid import uuid4


class Status(Enum):
    IS_WAITING = "is waiting"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"
    EXPIRED = "expired"
    BLOCKED = "blocked"
    
    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateField(default=date.today)
    started_at = models.DateField(default=date.today)
    finished_at = models.DateField(default=date.today)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    depends_on = models.ForeignKey('Event', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices(), default=Status.IN_PROGRESS)

    class Meta:
        db_table = "events"

    def  __str__(self) -> str:
        return f"{self.title}"
