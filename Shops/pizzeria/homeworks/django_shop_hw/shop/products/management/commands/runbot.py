from django.core.management.base import BaseCommand
from ...admin_bot import bot


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot run command'

    def handle(self, *args, **kwargs):
        print('Bot starts polling...')
        bot.infinity_polling()
