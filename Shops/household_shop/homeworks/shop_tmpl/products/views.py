from django.shortcuts import render, HttpResponse
from .models import Tag, Manufacturer, Product


# Create your views here.
def ger_all_products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products/products.html", context) 


def get_sort_products(request):
    
    test_dict = {key: value for key, value in dict(request.GET).items()}

    product = Product.objects.filter(**test_dict)
    context = {
        "products": product
    }
    return render(request, "products/products.html", context) 


def get_products(request):
    result = str()
    if not request.GET:
        result = ger_all_products(request)
    else:
        result = get_sort_products(request)
    return result


def get_product_by_id(request, product_id):
    product = Product.objects.filter(product_id=product_id)
    context = {
        "products": product
    }
    return render(request, "products/product_detail.html", context)
