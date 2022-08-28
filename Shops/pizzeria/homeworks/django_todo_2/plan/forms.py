from datetime import date, timedelta
from enum import Enum
from django import forms
from .models import Event


class Status(Enum):
    IS_WAITING = "is waiting"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"
    EXPIRED = "expired"
    BLOCKED = "blocked"

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class EventForm(forms.Form):
    started_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    finished_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    depends_on = forms.MultipleChoiceField(widget=forms.Select(attrs={'class': 'form-select'}))
    status = forms.MultipleChoiceField(
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=Status.choices()
    )
