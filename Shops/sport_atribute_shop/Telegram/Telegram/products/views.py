from django.shortcuts import render
from .models import Product
# Create your views here.

def add_product(request):
    products = Product.objects.all()
    description = {
        "products": products
    }
    return render(request, "products/products.html", description)
