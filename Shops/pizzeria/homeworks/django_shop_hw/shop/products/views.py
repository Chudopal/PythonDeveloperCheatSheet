from django.shortcuts import render
from .models import Manufacturer, Tag, Product


# Create your views here.

def format_args(request_args):
    return {key: value.replace(' ', '').strip().split(",") for key, value in request_args.items()}


products_filters = {
    'price_lte': lambda product, value: product.filter(price__lte=float(value)),
    'price_gte': lambda product, value: product.filter(price__gte=float(value)),
    'price_lt': lambda product, value: product.filter(price__lt=float(value)),
    'price_gt': lambda product, value: product.filter(price__gt=float(value)),
    'tags': lambda product, value: product.filter(tags__name=value)
}


def filter_products(request_get):
    args = format_args(request_get)
    products = Product.objects.all()
    for arg, values in args.items():
        for value in values:
            query_filter = products_filters.get(arg, None)
            if query_filter:
                products = query_filter(products, value)
    return products


def product_detail(request, product_uuid):
    product = Product.objects.select_related('manufacturer').prefetch_related('tags').get(uuid=product_uuid)
    tags = product.tags.all()
    return render(request=request, template_name='products/product_detail.html', context={'product': product, 'tags':tags})


def products_view(request):
    products = filter_products(request.GET.dict())
    return render(request=request, template_name='products/products_list.html', context={'products': products})
