from django.db import models
from uuid import uuid4
from datetime import date
from dateutil.relativedelta import relativedelta

# Create your models here.
class Card(models.Model):
    number = models.PositiveBigIntegerField(null=False)
    expiration_date = models.DateField(default=(date.today() + relativedelta(years=3)))
    user_name = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    account = models.ForeignKey('Account', on_delete=models.CASCADE, null=False)
    cvv = models.IntegerField(null=False)

    class Meta:
        db_table = 'cards'


class Account(models.Model):
    iban = models.UUIDField(primary_key=True, default=uuid4())
    sum = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'accounts'


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    age = models.IntegerField(null=False)
    uuid = models.UUIDField(default=uuid4(), primary_key=True)

    class Meta:
        db_table = 'users'