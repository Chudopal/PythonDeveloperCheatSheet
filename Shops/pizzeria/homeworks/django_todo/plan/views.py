import json
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView,
    TemplateView,
)
from django.urls import reverse

from .forms import EventFromCreate, EventFormUpdate
from .models import Event, Status


class EventCreateView(CreateView):
    template_name: str = "plan/event_add.html"
    form_class: type = EventFromCreate

    def get_success_url(self):
        return reverse('event-list')


class EventListView(ListView):
    template_name: str = "plan/event_list.html"
    model: type = Event
    buttons_context: dict = None

    def set_buttons_style(self, **filters):
        buttons_bootstrap_styles = {
            'is_waiting': 'btn-outline-primary',
            'in_progress': 'btn-outline-primary',
            'finished': 'btn-outline-primary',
            'expired': 'btn-outline-primary',
            'blocked': 'btn-outline-primary',
            'all': 'btn-outline-primary',
        }
        status = filters.get('status', 'all').replace(" ", "_")
        buttons_bootstrap_styles[status] = 'btn-primary'
        self.buttons_context = buttons_bootstrap_styles

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        request_params = dict(self.request.GET.items())
        self.set_buttons_style(**request_params)
        return qs.filter(**request_params)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.buttons_context)
        return context


class EventDetailView(DetailView):
    template_name: str = "plan/event_detail.html"
    model: type = Event


class EventDeleteView(DeleteView):
    template_name: str = "plan/event_delete.html"
    model: type = Event
    success_url: str = "#"

    def get_success_url(self):
        return reverse('event-list')


class EventUpdateView(UpdateView):
    template_name: str = "plan/event_update.html"
    form_class: type = EventFormUpdate
    model = Event

    def get_success_url(self):
        return reverse('event-list')


class EventAnalyticsView(TemplateView):
    template_name: str = "plan/analytics.html"

    def count_event_percentage(self, events_num, total_events):
        return events_num / total_events * 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Event.objects.all()
        events_count = len(events)
        chart_data = [
            {'id': status.name,
             'nested': {'value': self.count_event_percentage(events.filter(status=status.value).count(), events_count)}
             }
            for status in Status
        ]
        context['chart_data'] = json.dumps(chart_data)
        return context
