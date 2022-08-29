from django.urls import path
from .views import get_events_list, create_new_event, get_event_detail


urlpatterns = [
    path('front/', get_events_list),
    path('front/add', create_new_event),
    path('front/<str:event_id>/', get_event_detail),
]
