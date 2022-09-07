import json
from .models import Event
from .forms import EventForm
from django.conf import settings
from django.shortcuts import render
from .request_service import ConnectService


def get_events_list(request):
    template_name = 'plan/event_list.html'
    data = ConnectService(settings.SERVICE_URL).get_list_events()
    context = {'events': [Event(**item) for item in data]}
    
    return render(request=request, template_name=template_name, context=context)


def create_new_event(request):
    template_name = 'plan/event_add.html'
    context = {"form": EventForm}
    
    if request.method == "POST":
        event = json.dumps(request.POST)
        ConnectService(settings.SERVICE_URL).add_event(event)        

    return render(request=request, template_name=template_name, context=context)


def get_event_detail(request, pk):
    template_name = 'plan/event_detail.html'
    data = ConnectService(settings.SERVICE_URL + pk).get_event_detail()
    context =  {"object": Event(**data)}
    
    return render(request=request, template_name=template_name, context=context)


def delete_event(request, pk):
    template_name = 'plan/event_delete.html'
    ConnectService(settings.SERVICE_URL + pk).delete_event()
    
    return render(request=request, template_name=template_name)


def update_event(request, pk):
    template_name = 'plan/event_update.html'
    context = {"form": EventForm}
    event = json.dumps(request.POST)
    ConnectService(settings.SERVICE_URL + pk).update_event(event)

    return render(request=request, template_name=template_name, context=context)
