from django.db import models
from uuid import uuid4


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False)
    quantity = models.IntegerField(null=False)
    discount = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    amount = models.IntegerField(default=1)
    price = models.FloatField(null=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
