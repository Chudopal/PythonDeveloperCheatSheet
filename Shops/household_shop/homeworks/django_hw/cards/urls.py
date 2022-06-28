from .views import get_all_accounts, get_all_cards
from django.urls import path


urlpatterns = [
    path('<str:user_uuid>/cards', view=get_all_cards),
    path('<str:user_uuid>/accounts', view=get_all_accounts),
]
