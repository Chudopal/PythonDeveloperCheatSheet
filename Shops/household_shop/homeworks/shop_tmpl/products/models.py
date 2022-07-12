from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=100, null=False, primary_key=True)

    class Meta:
        db_table = 'manufacturers'


class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, primary_key=True)
    quantity = models.IntegerField()
    discount = models.FloatField(max_length=3)

    class Meta:
        db_table = 'tags'


class Product(models.Model):
    product_name = models.CharField(max_length=55, null=False)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(max_length=35, null=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=False)
    product_id = models.UUIDField(primary_key=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'products'
