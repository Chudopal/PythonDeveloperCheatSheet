from django.db import models

# Create your models here.


class Manufacturer(models.Model):

    name = models.CharField(max_length=128, null=False)


class Teg(models.Model):

    name = models.CharField(max_length=128, null=False)


class Product(models.Model):

    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    description = models.CharField(max_length=128, null=True)
    count = models.IntegerField(null=True, default=1)
    price = models.FloatField(null=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=False)
    teg = models.ForeignKey(Teg, on_delete=models.CASCADE, null=False)
    
#Product.objects.create(uuid=uuid.uuid4(), name='X5', description='car', count=2, price=30, manufacturer=p, teg=t)
#env\Scripts\activate 