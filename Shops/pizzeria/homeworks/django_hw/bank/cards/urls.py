from django.urls import path
from .views import cards_view, accounts_view

urlpatterns = [
    path('<str:user_uuid>/cards', cards_view),
    path('<str:user_uuid>/accounts', accounts_view),
]