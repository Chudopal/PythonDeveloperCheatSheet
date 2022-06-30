from django.db import models
import uuid

# Create your models here.

class Bank_score(models.Model):
    iban = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sum = models.FloatField()


class Users(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=124)
    age = models.IntegerField()


class Bank_cards(models.Model):
    number = models.CharField(primary_key=True, max_length=16, null=False)
    exp_date = models.DateField(auto_now=True)
    user_card = models.ForeignKey(Users, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(Bank_score, on_delete=models.CASCADE)
    cvv = models.CharField(max_length=3, null=False)




