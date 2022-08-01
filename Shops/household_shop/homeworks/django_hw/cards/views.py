from django.shortcuts import render
from .models import BankCard

# Create your views here.
def get_all_cards(request, user_uuid):
    out_data = BankCard.objects.filter(customer=user_uuid).values()
    return render(request=request, template_name='cards/cards.html', context={'cards': out_data})


def get_all_accounts(request, user_uuid):
    out_data = [card.account for card in BankCard.objects.filter(customer=user_uuid)]
    return render(request=request, template_name='cards/accounts.html', context={'accounts': out_data})
