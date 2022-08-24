from django.urls import path
from .views import get_front_view

urlpatterns = [
    path('front/', get_front_view),
]
