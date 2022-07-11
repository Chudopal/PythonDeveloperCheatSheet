from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Manufacturer, Teg


# Create your views here.

def get_all_products(request):
    all_product = Product.objects.all()
    return render(request, 'landing/list.html', {"all_product": all_product})


def get_filter_products1(request):
    all_product = Product.objects.filter(cost__gt=20, cost__lt=50)
    return render(request, 'landing/list.html', {"all_product": all_product})


def get_filter_products2(request):
    all_product = Product.objects.filter(cost__gte=20, cost__lte=50)
    return render(request, 'landing/list.html', {"all_product": all_product})


def get_product_info(request, product_name):
    all_product = Product.objects.filter(name_product=product_name)
    return render(request, 'landing/list_info.html', {"all_product": all_product})