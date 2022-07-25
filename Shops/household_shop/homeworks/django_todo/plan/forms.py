from datetime import date, timedelta
from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'started_at', 'finished_at', 'title',
            'description', 'depends_on', 'status',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'finished_at': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'started_at': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
            'depends_on': forms.Select(attrs={
                'class': 'form-select',
            })
        }

    def clean_started_at(self):
        started_at = self.cleaned_data['started_at']
        
        if started_at < date.today():
            raise forms.ValidationError("Вы не можете создать событие, которое начась в прошлом!")
        
        return started_at

    def clean_finished_at(self):
        finished_at = self.cleaned_data['finished_at']
        started_at = self.cleaned_data['started_at']

        if finished_at < date.today() or finished_at < started_at:
            raise forms.ValidationError("Вы не можете создать событие, которое закончится в прошлом!")
        
        return finished_at
