import json
from .models import Event
from .forms import EventForm
from django.conf import settings
from django.shortcuts import render
from .request_service import ConnectService


def get_events_list(request):
    data = ConnectService(settings.SERVICE_URL).get_all_events()
    context = {'events': [Event(**item) for item in data]}
    return render(request, 'plan/event_list.html', context=context)


def create_new_event(request):
    template_name = 'plan/event_add.html'
    form = EventForm
    context = {"form": form}
    
    if request.method == "POST":
        event = json.dumps(request.POST)
        ConnectService(settings.SERVICE_URL).add_event(event)        

    return render(request, template_name, context=context)


def get_event_detail(request, event_id):
    data = ConnectService(settings.SERVICE_URL + event_id).get_event_detail()
    context =  {"object": Event(**data)}
    return render(request, 'plan/event_detail.html', context=context)
