from django.shortcuts import render
from django.http import HttpRequest
from .request_service import ConnectService
from .models import Event


def get_front_view(request):
    template_name = 'plan/event_list.html'
    data = ConnectService('http://127.0.0.1:5000/api/events/').get_data()

    context = {'events': [Event(**item) for item in data]}
    render(request, template_name, context=context)


def post_front_view(request):
    data = ConnectService(url='http://127.0.0.1:5000/api/events/')
    return HttpRequest(data.post_data())
