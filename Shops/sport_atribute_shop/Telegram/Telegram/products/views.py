from math import prod
from django.shortcuts import render
from .models import Product
from .models import Manufacturer
from .models import Teg
# Create your views here.

def get_products(request):
    products = Product.objects.all() 
    return render(request, "products/products_detail.html", {
        "products": products
    })
                

def get_teg(product):
    product = list(Product.objects.all())
    for i in range():
        temp_product = [product.pop(0) for i in range(10)]
        teg = Teg.objects.create(name=f"Teg{i+1}")
        teg.product.set(temp_product)
        teg.save()

def get_teg():
    products = Product.objects.all()
    tegs = list(Teg.objects.all())
    for product in products:
        product.teg.set(tegs)
        product.save()

def filter_price(request):
    all_price = Product.objects.filter(cost)
    return render(request, "products/products_detail.html", {
        "products": all_price
    })