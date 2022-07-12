from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.


def get_products(request):
    
    products = Product.objects.values('name', 'price')
    return HttpResponse(products)

def get_products_filter():

    pass