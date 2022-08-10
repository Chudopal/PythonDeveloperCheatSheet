from django.urls import path
from .views import EventListCreateAPIView, EventDetailAPIView

urlpatterns = [
    path('events/', EventListCreateAPIView.as_view()),
    path('events/<str:pk>', EventDetailAPIView.as_view()),
]
