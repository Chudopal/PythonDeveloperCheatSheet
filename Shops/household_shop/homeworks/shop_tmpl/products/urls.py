from .views import get_products, get_product_by_id
from django.urls import path

    
urlpatterns = [
    path('', view=get_products),
    path('<str:product_id>', view=get_product_by_id),
]
