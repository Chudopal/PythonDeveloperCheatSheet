from django.shortcuts import render
from .models import Tag, Manufacturer, Product

# Create your views here.
def get_all_products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products/products.html", context)
