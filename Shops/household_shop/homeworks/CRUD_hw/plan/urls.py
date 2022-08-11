from django.urls import path
from .views import EventListView, EventDetailView


urlpatterns = [
    path('api/events', EventListView.as_view()),
    path('api/events/<str:pk>/', EventDetailView.as_view()),
]
