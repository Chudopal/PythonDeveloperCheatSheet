from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView,
    TemplateView,
)
from django.urls import reverse

from plan.forms import EventForm
from plan.models import Event, Status


class EventCreateView(CreateView):
    template_name: str = "plan/event_add.html"
    form_class: type = EventForm

    def get_success_url(self):
        return reverse('event-list')


class EventListView(ListView):
    template_name: str = "plan/event_list.html"
    model: type = Event

    def get_queryset(self):
        status = self.request.GET.get("status")
        result = Event.objects.all()
        if status:
            result = Event.objects.filter(status=status) 
        
        return result


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
    template_name: str = "plan/event_analytics.html"
    
    def get_context_data(self, **kwargs):
        all_events = Event.objects.all()
        cnt_all_events = len(all_events)
        out_dict = dict()

        for status in Status:
            cnt_events = len(Event.objects.filter(status=status.value))
            percentage = cnt_events * 100 / cnt_all_events

            out_dict[status.value] = round(percentage, 2)

        context = {
            "events": out_dict,
        }

        return context
