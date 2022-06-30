from django.shortcuts import render
from django.http import HttpResponse
from .models import Bank_score, Bank_cards

# Create your views here.
def get_all_cards(request, user_uuid):
    data = Bank_cards.objects.filter(iban=user_uuid)
    return HttpResponse(*data.values())


def get_all_account(request, user_uuid):
    data = Bank_score.objects.filter(iban=user_uuid)
    return HttpResponse(*data.values())


