from django.shortcuts import render
from django.http import HttpResponse
from .models import Account, Card


# Create your views here.
def get_all_cards(request, user_uuid):
    data = Card.objects.filter(iban=user_uuid)
    return HttpResponse(*data.values())


def get_all_account(request, user_uuid):
    data = Account.objects.filter(iban=user_uuid)
    return HttpResponse(*data.values())