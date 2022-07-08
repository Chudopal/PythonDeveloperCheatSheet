from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

class Teg(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200)
    amount = models.PositiveIntegerField(default=1)
    cost = models.PositiveIntegerField(null=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=False)
    id = models.UUIDField(primary_key=True)
    teg = models.ForeignKey(Teg, on_delete=models.CASCADE, null=False)

