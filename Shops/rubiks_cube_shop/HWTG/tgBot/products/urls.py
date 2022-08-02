from urllib import request
from django.urls import path
from .views import get_products

urlpatterns = [
    path('', view=get_products),
]

from .admin_bot import *
