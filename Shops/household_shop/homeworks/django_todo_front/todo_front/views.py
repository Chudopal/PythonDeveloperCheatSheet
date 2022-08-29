from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Event
from .request_service import ConnectService


def get_events_list(request):
    data = ConnectService(settings.SERVICE_URL).get_all_events()
    context = {'events': [Event(**item) for item in data]}
    return render(request, 'plan/event_list.html', context=context)


@csrf_exempt
def create_new_event(request):
    if request.method == "POST":
        event = Event(**request.POST)
        data = ConnectService(settings.SERVICE_URL).add_event(event.json())
        return render(request, 'plan/event_add.html')
    else:
        return render(request, 'plan/event_add.html')
    

def get_event_detail(request, event_id):
    data = ConnectService(settings.SERVICE_URL + event_id).get_event_detail()
    context =  {"object": Event(**data)}
    return render(request, 'plan/event_detail.html', context=context)
