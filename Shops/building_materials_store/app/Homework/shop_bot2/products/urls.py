from django.urls import path
from .views import get_all_products, get_filter_products1, get_filter_products2, get_product_info


urlpatterns = [
    path('', view=get_all_products),
    path('price_gt=20&price_lt=50/', view=get_filter_products1),
    path('price_gte=20&price_lte=50/', view=get_filter_products2),
    path('info/<str:product_name>', view=get_product_info),
]

