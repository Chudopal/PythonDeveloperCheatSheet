from django.urls import path
from .views import (
    EventCreateView,
    EventListView,
    EventDetailView,
    EventDeleteView,
    EventUpdateView,
)

urlpatterns = [
    path("add/", view=EventCreateView.as_view(), name="event-add"),
    path("list/", view=EventListView.as_view(), name="event-list"),
    path("<str:pk>/", view=EventDetailView.as_view(), name="event-detail"),
    path("<str:pk>/delete", view=EventDeleteView.as_view(), name="event-delete"),
    path("<str:pk>/update", view=EventUpdateView.as_view(), name="event-update"),
]
