from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta
from uuid import uuid4


class BankAccount(models.Model):
    iban = models.UUIDField(default=uuid4(), primary_key=True)
    amount = models.PositiveIntegerField(default=0)


class BankCustomer(models.Model):
    uuid = models.UUIDField(default=uuid4(), primary_key=True)
    name = models.CharField(max_length=255, null=False)
    age = models.SmallIntegerField(max_length=150, null=False)


class BankCard(models.Model):
    card_number = models.PositiveBigIntegerField(max_length=16, null=False, primary_key=True)
    exp_date = models.DateField(default=(date.today() + relativedelta(years=4)))
    cvv_code = models.PositiveSmallIntegerField(null=False)
    customer = models.ForeignKey(BankCustomer, on_delete=models.CASCADE)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
