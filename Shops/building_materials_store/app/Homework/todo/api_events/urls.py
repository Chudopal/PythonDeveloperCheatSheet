from django.urls import path
from .views import EventListView, EventCreateView, EventDetailView

urlpatterns = [
    path("add/", view=EventCreateView.as_view()),
    path("list/", view=EventListView.as_view()),
    path("list/<str:pk>", view=EventDetailView.as_view()),
]
