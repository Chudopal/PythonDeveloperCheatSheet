from django.urls import path
from .views import (
    EventCreateView,
    EventListView,
    EventDetailView,
    EventDeleteView,
    EventUpdateView,
    EventanalyticsView,
)

urlpatterns = [
    path("add/", view=EventCreateView.as_view(), name="event-add"),
    path("list/", view=EventListView.as_view(), name="event-list"),
    path("<str:pk>/", view=EventDetailView.as_view(), name="event-detail"),
    path("<str:pk>/delete", view=EventDeleteView.as_view(), name="event-delete"),
    path("<str:pk>/update", view=EventUpdateView.as_view(), name="event-update"),
    path("analytics/", view=EventanalyticsView.as_view(), name="event-analytics"),
]
