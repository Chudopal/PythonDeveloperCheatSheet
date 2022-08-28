from django.urls import path
from .views import events_list_view, events_detail_view, events_create_view

urlpatterns = [
    path('', events_list_view),
    path('<str:event_pk>', events_detail_view),
    path('add/', events_create_view),
]
