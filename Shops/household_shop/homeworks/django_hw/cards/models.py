from django.db import models


class Customer(models.Model):

    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=35, null=False)
    age = models.IntegerField(null=False)


class Account(models.Model):

    iban = models.UUIDField(primary_key=True)
    amount = models.FloatField(max_length=35)


class BankCard(models.Model):

    card_number = models.IntegerField(primary_key=True)
    end_date = models.DateField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    cvv = models.IntegerField(null=False)
