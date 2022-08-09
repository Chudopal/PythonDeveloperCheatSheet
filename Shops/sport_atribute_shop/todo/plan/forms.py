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
            raise forms.ValidationError("Вы не можете создать событие, которое началось в прошлом!")
        
        return started_at

    def clean_finished_at(self):
        started_at = self.cleaned_data['started_at']
        finished_at = self.cleaned_data['finished_at']

        if finished_at < date.today() or finished_at < started_at:
            raise forms.ValidationError("Вы не можете создать событие, которое закончилось в прошлом!")

        started_at = timedelta(days=14)
        if finished_at > started_at + date.today():
            raise forms.ValidationError("Вы не можете задать дедлайн, больше 14 дней!")
            
        return finished_at