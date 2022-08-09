from django.urls import path
from .views import EventListView, EventDetailView


urlpatterns = [
    path('api/books', EventListView.as_view()),
    path('api/books/<str:pk>/', EventDetailView.as_view()),
]
