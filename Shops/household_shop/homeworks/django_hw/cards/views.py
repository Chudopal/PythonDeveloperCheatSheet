from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Account, BankCard

# Create your views here.
def get_all_accounts(request, user_uuid):
    out_data = Account.objects.filter(iban=user_uuid)
    return HttpResponse(*out_data.values())


def get_all_cards(requset, user_uuid):
    return HttpResponse("get_all_cards")
