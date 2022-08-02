from tgBot.settings import TOKEN_TG
import telebot
from telebot import types
from .models import Teg, Manufacturer

bot = telebot.TeleBot(TOKEN_TG)
global NAME
global PRICE
global DESCRIPTION
global COUNT


@bot.message_handler(commands=["start"])
def start(m, res=False):
    menu(m)

def teg_create():
    @bot.message_handler(content_types=["text"])
    def get_name(message):
        try:
            Teg.objects.create(name = message.text)
            bot.send_message(message.chat.id, 'Тег "' + message.text + '"был добавлен!')
        except:
            bot.send_message(message.chat.id, 'Что-то пошло не так(')
        stop(message)

    
def manufacturer_create():
    @bot.message_handler(content_types=["text"])
    def get_name(message):
        try:
            Manufacturer.objects.create(name = message.text)
            bot.send_message(message.chat.id, 'Производитель "' + message.text + '"был добавлен!')
        except:
            bot.send_message(message.chat.id, 'Что-то пошло не так(')
        stop(message)        


def product_create():
    @bot.message_handler(content_types=["text"])
    def get_name(message):
        NAME = message.text
        bot.send_message(message.chat.id, "Введите описанние продукта:")
        bot.register_next_step_handler(message, get_description)


    def get_description(message):
        DESCRIPTION = message.text
        bot.send_message(message.chat.id, "Введите количество:")
        bot.register_next_step_handler(message, get_count)


    def get_count(message):
        try:
            COUNT = int(message.text)
        except:
            COUNT = 1
        bot.send_message(message.chat.id, "Введите цену:")
        bot.register_next_step_handler(message, get_price)
        

    @bot.message_handler(commands=['stop'])
    def get_price(message):
        try:
            PRICE = int(message.text)
        except:
            PRICE = 0
        get_teg(message)
        bot.register_next_step_handler(message, get_teg)


    def get_teg(message):
        keyboard = types.InlineKeyboardMarkup()
        for name in Teg.objects.all():
            button = types.InlineKeyboardButton(text=name.name, callback_data=name.name)
            keyboard.add(button)
        question = 'Your chose?'
        bot.register_next_step_handler(message, get_manufacturer)
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


    def get_manufacturer(message):
        keyboard = types.InlineKeyboardMarkup()
        for name in Manufacturer.objects.all():
            button = types.InlineKeyboardButton(text=name.name, callback_data=name.name)
            keyboard.add(button)
        question = 'Your chose?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
        stop(message)        


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "teg":
        bot.send_message(call.from_user.id, "Введите название продукта: ")
        teg_create()
    elif call.data == "manufacturer":
        bot.send_message(call.from_user.id, "Введите название продукта: ")
        manufacturer_create()
    elif call.data == "product":
        bot.send_message(call.from_user.id, "Введите название продукта: ")
        product_create()
    else:
        stop(call)        
        

def menu(message):
    keyboard = types.InlineKeyboardMarkup()
    teg_button = types.InlineKeyboardButton(text='Создать тег', callback_data='teg')
    keyboard.add(teg_button)
    manufacturer_button = types.InlineKeyboardButton(text='Создать производителя', callback_data='manufacturer')
    keyboard.add(manufacturer_button)
    product_button = types.InlineKeyboardButton(text='Создать продукт', callback_data='product')
    keyboard.add(product_button)
    question = 'Your chose?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.message_handler(commands=['stop'])
def stop(message):
    menu(message)

# Запускаем бота
bot.polling(none_stop=True, interval=0)