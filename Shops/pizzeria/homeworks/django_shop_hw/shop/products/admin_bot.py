import os
import telebot
from .models import Product, Tag, Manufacturer

bot = telebot.TeleBot(os.environ.get('dj_shop_bot_token'))


@bot.message_handler(commands=["start"])
def start(m, res=False):
    template = 'Hi {user}!'
    bot.send_message(m.chat.id, template.format(user=m.from_user.first_name))


@bot.message_handler(commands=["add_product"])
def add_product(m, res=False):
    pass
