from django.urls import path
from .views import get_products, filter_price


urlpatterns = [
    path('', view=get_products),
    path('filter/', view=filter_price)
]
