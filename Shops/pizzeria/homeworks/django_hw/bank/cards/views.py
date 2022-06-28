from django.shortcuts import render, HttpResponse
from .models import BankAccount, BankCard, BankCustomer


# Create your views here.

def cards_view(request, user_uuid):
    data = BankCard.objects.filter(customer=user_uuid).values()
    return render(request=request, template_name='cards/cards.html', context={'cards': data})


def accounts_view(request, user_uuid):
    data = [card.account for card in BankCard.objects.filter(customer=user_uuid)]
    return render(request=request, template_name='cards/accounts.html', context={'accounts': data})
