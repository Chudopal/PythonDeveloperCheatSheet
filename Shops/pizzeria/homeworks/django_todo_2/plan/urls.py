from django.urls import path
from .views import events_list_view, events_detail_view, events_create_view

urlpatterns = [
    path('', events_list_view, name="event-list"),
    path('add/', events_create_view, name="event-add"),
    path('<str:event_uuid>/', events_detail_view, name="event-detail"),
]
