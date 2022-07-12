from django.urls import path
from .views import get_products


urlpatterns = [
    path('', view=get_products)
]
