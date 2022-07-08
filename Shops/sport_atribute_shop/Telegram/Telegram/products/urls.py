from django.urls import path
from .views import add_product


urlpatterns = [
    path('', view=add_product)
]
