from django.shortcuts import render, HttpResponse
from .models import Manufacturer, Tag, Product


# Create your views here.


def price_lte(query_set, value):
    return query_set.filter(price__lte=float(value))


def price_gte(query_set, value):
    return query_set.filter(price__gte=float(value))


def price_lt(query_set, value):
    return query_set.filter(price__lt=float(value))


def price_gt(query_set, value):
    return query_set.filter(price__gt=float(value))


price_filters = {
    'price_lte': price_lte,
    'price_gte': price_gte,
    'price_lt': price_lt,
    'price_gt': price_gt
}


def filter_products(**kwargs):
    products = Product.objects.all()
    if kwargs:
        for arg, val in kwargs.items():
            products = price_filters.get(arg)(products, val)
    return products


def product_detail(request, product_uuid):
    product = Product.objects.get(uuid=product_uuid)
    return render(request=request, template_name='products/product_detail.html', context={'product': product})


def products_view(request):
    products = filter_products(**request.GET.dict())
    return render(request=request, template_name='products/products_list.html', context={'products': products})
