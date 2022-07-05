from django.contrib import admin
from .models import Tag, Manufacturer, Product


# Register your models here.
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ('name', 'quantity', 'discount')
    ordering = ('name',)


class ManufacturerAdmin(admin.ModelAdmin):
    model = Manufacturer


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'manufacturer', 'amount', 'price')


admin.site.register(Tag, TagAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Product, ProductAdmin)
