import json
from django.conf import settings
from django.shortcuts import render
from .models import Event
from .events_service import EventsService
from .forms import EventForm

events_service = EventsService(host=settings.API_SERVICE_HOST, port=settings.API_SERVICE_PORT)


def events_list_view(request):
    template = "plan/events_list.html"
    data = events_service.get_all_events()
    context = {'events': [Event(**item) for item in data.json()]}
    return render(request=request, template_name=template, context=context)


def events_detail_view(request, event_uuid):
    template = "plan/event_detail.html"
    data = events_service.get_event_details(event_uuid=event_uuid)
    context = {"object": Event(**data.json())}
    return render(request=request, template_name=template, context=context)


def events_create_view(request):
    template = "plan/event_add.html"
    form = EventForm
    context = {'form': form}

    if request.method == 'POST':
        data = json.dumps(request.POST)
        events_service.add_event(data=data)
        return render(request=request, template_name=template, context=context)
    elif request.method == 'GET':
        return render(request=request, template_name=template, context=context)
