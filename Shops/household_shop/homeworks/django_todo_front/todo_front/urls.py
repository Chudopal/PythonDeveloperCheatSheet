from django.urls import path
from .views import get_events_list, create_new_event, get_event_detail


urlpatterns = [
    path('front/', get_events_list, name='event-list'),
    path('front/add', create_new_event, name='event-add'),
    path('front/<str:event_id>/', get_event_detail, name='event-detail'),
]
