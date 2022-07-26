from datetime import date, timedelta

from django import forms

from .models import Event, Status


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


class EventFromCreate(EventForm):
    def clean_started_at(self):
        started_at = self.cleaned_data['started_at']

        if started_at < date.today():
            raise forms.ValidationError("Вы не можете создать событие, которое начась в прошлом!")

        return started_at

    def clean_finished_at(self):
        finished_at = self.cleaned_data['finished_at']
        started_at = date.fromisoformat(self.data['started_at'])

        if finished_at < started_at:
            raise forms.ValidationError("Дедлайн не может быть раньше начала события!")
        elif finished_at > started_at + timedelta(days=14):
            raise forms.ValidationError("Дедлайн не может быть дальше чем через две недели от начала события!")

        return finished_at


class EventFormUpdate(EventForm):
    def clean_status(self):
        status = self.cleaned_data['status']
        depends_on = self.cleaned_data['depends_on']

        if depends_on and (status == Status.FINISHED.value) and (depends_on.status != Status.FINISHED.value):
            raise forms.ValidationError("Нельзя завершить событие если не завершено связанное!")

        return status
