from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ValidationError
from .models import Product
from .shop_service import ProductsService

products_service = ProductsService()


def product_detail(request, product_uuid):
    try:
        product = products_service.get_product_by_uuid(product_uuid)
        tags = product.tags.all()
        return render(request=request, template_name='products/product_detail.html',
                      context={'product': product, 'tags': tags})
    except Product.DoesNotExist:
        raise Http404
    except ValidationError:
        raise Http404


def products_view(request):
    products = products_service.filter_products(request.GET.dict())
    return render(request=request, template_name='products/products_list.html', context={'products': products})
