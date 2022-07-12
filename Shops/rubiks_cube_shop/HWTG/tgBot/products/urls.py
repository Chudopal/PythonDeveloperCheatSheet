from urllib import request
from django.urls import path
from .views import get_products

urlpatterns = [
    path('', view=get_products),
    #path('cars/<int:car_id>', view=get_car_detail, name="car_detail"),
]

from .admin_bot import *
