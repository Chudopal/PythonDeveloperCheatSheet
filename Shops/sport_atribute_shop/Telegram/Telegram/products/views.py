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
