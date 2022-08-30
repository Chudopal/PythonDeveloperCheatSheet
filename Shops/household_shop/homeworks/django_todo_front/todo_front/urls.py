from django.urls import path
from .views import get_events_list, create_new_event, get_event_detail, delete_event, update_event


urlpatterns = [
    path('list/', get_events_list, name='event-list'),
    path('add/', create_new_event, name='event-add'),
    path('<str:pk>/', get_event_detail, name='event-detail'),
    path('<str:pk>/delete/', delete_event, name='event-delete'),
    path('<str:pk>/update/', update_event, name='event-update'),
]
