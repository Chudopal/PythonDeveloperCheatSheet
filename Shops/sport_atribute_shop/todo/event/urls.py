from django.urls import path
from event.views import EventListCreateAPIView, EventDetailAPIView


urlpatterns = [
    path('event/', view=EventListCreateAPIView.as_view()),
    path('event/<str:id>', view=EventDetailAPIView.as_view())
]
