from django.db import models
import uuid

# Create your models here.

class Manufacturer(models.Model):
    brand = models.CharField(null=False, max_length=50)


class Teg(models.Model):
    name = models.CharField(null=False, max_length=50)


class Product(models.Model):
    name_product = models.CharField(null=False, max_length=100)
    description = models.CharField(max_length=250)
    weight = models.FloatField(default=1)
    cost = models.FloatField(null=False)
    made_product = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    tag = models.ForeignKey(Teg, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_product} - {self.cost}"
