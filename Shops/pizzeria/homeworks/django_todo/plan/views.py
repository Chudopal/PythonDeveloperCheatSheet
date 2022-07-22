from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView,
    TemplateView,
)
from django.urls import reverse

from .forms import EventForm
from .models import Event


class EventCreateView(CreateView):
    template_name: str = "plan/event_add.html"
    form_class: type = EventForm

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
    form_class: type = EventForm
    model = Event

    def get_success_url(self):
        return reverse('event-list')


class EventAnalyticsView(TemplateView):
    template_name: str = "plan/analytics.html"
