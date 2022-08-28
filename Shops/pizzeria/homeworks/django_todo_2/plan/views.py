from django.shortcuts import render
import json
from .models import Event
from .events_service import EventsService
from .forms import EventForm


def events_list_view(request):
    template = "plan/events_list.html"
    host = 'http://127.0.0.1'
    port = '8000'

    data = EventsService.get_all_events(host, port)
    context = {'events': [Event(**item) for item in data.json()]}
    return render(request=request, template_name=template, context=context)


def events_detail_view(request, event_uuid):
    template = "plan/event_detail.html"
    host = 'http://127.0.0.1'
    port = '8000'

    data = EventsService.get_event_details(host, port, event_uuid)
    context = {"object": Event(**data.json())}
    return render(request=request, template_name=template, context=context)


def events_create_view(request):
    template = "plan/event_add.html"
    host = 'http://127.0.0.1'
    port = '8000'

    if request.method == 'POST':
        form = EventForm
        context = {'form': form}
        data = json.dumps(request.POST)
        EventsService.add_event(host, port, data=data)
        return render(request=request, template_name=template, context=context)
    elif request.method == 'GET':
        form = EventForm
        context = {'form': form}
        return render(request=request, template_name=template, context=context)
