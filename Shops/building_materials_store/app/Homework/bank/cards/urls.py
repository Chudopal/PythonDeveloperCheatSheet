from django.urls import path
from .views import get_all_cards, get_all_account

urlpatterns = [
    path('users/<str:user_uuid>/cards', view=get_all_cards),
    path('users/<str:user_uuid>/accounts', view=get_all_account),
]
