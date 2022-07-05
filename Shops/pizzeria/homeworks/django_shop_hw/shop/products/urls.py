from django.urls import path
from .views import product_detail, products_view

urlpatterns = [
    path('', products_view),
    path('<str:product_uuid>/', product_detail),
]