from .views import get_all_products
from django.urls import path

    
urlpatterns = [
    path('', view=get_all_products)
]