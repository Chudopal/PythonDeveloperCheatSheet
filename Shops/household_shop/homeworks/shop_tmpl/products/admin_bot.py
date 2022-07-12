import telebot
from uuid import uuid4
from django.conf import settings
from .models import Product, Manufacturer, Tag


TG_TOKEN = '5598216948:AAEfDGcb78ry64Gg-6CT2EmfUArL9RUxp04'

bot = telebot.TeleBot(TG_TOKEN, threaded=False)
b_get_products = "Current products"
b_set_product = "New product"
product_name = str()
description = str()
quantity = str()
price = str()
manufacturer = str()
tag = str()


def add_new_product():
    Product.objects.create(
        product_name=product_name,
        description=description,
        quantity=quantity,
        price=price,
        manufacturer=Manufacturer.objects.get(manufacturer=manufacturer),
        product_id=uuid4(),
        tag=Tag.objects.get(name=tag),
    ).save()


@bot.message_handler(commands=["start"])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton(b_get_products)
    item2 = telebot.types.KeyboardButton(b_set_product)
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id,
                     "Нажми: \n{} - Список продуктов\n{} - Создание нового продукта".format(b_get_products,
                                                                                            b_set_product),
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    answer = str()

    if message.text.strip() == b_get_products:
        products = Product.objects.select_related()
        for product in products:
            answer += f"{product.product_name}, {product.price}р.\n{product.description}\n\n"

        bot.send_message(message.chat.id, answer)

    elif message.text.strip() == b_set_product:
        bot.send_message(message.from_user.id, "Введите название продукта:");
        bot.register_next_step_handler(message, add_product_name);
        

def add_product_name(message):
    global product_name
    product_name = message.text
    bot.send_message(message.from_user.id, 'Введите описание продукта:');
    bot.register_next_step_handler(message, add_description);


def add_description(message):
    global description 
    description = message.text
    bot.send_message(message.from_user.id, 'Введите кол-во продукта:');
    bot.register_next_step_handler(message, add_quantity);


def add_quantity(message):
    global quantity
    quantity = message.text
    bot.send_message(message.from_user.id, 'Введите цену продукта:');
    bot.register_next_step_handler(message, add_price);


def add_price(message):
    global price
    price = int(message.text)
    bot.send_message(message.from_user.id, 'Введите производителя продукта:');
    bot.register_next_step_handler(message, add_manufacturer);


def add_manufacturer(message):
    global manufacturer
    manufacturer = message.text
    bot.send_message(message.from_user.id, 'Введите тег продукта:');
    bot.register_next_step_handler(message, add_tag);


def add_tag(message):
    global tag
    tag = message.text
    add_new_product()
    bot.send_message(message.from_user.id, 'Спасибо!');


bot.polling(none_stop=True)
