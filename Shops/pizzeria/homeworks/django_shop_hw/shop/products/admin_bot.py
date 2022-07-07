import logging
import telebot
from telebot import custom_filters, SimpleCustomFilter, types
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from telebot.callback_data import CallbackData
from django.conf import settings
from .models import Product, Tag, Manufacturer

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

state_storage = StateMemoryStorage()
callback_factory = CallbackData("item_pk", "storage_key", prefix='products')


def save_product(data):
    new_product = Product.objects.create(
        name=data['product_name'],
        description=data['description'],
        amount=data['amount'],
        price=data['price'],
        manufacturer=data['manufacturer']
    )
    new_product.tags.set(data['tags'])
    new_product.save()


def make_keyboard(queryset, storage_key):
    keyboard = types.InlineKeyboardMarkup()
    for item in queryset:
        keyboard.add(
            types.InlineKeyboardButton(text=str(item),
                                       callback_data=callback_factory.new(item_pk=item.pk, storage_key=storage_key))
        )
    return keyboard


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


class ProductAddStates(StatesGroup):
    product_name = State()
    manufacturer = State()
    description = State()
    amount = State()
    price = State()
    tags = State()


class IsNotEmptyMessageFilter(SimpleCustomFilter):
    """
    Filter to check whether the string is empty.
    """
    key = 'is_not_null'

    def check(self, message):
        return message.text != ""


class IsDigitFilter(SimpleCustomFilter):
    """
    Filter to check the given string is digit (float or int).
    """

    key = 'is_digit'

    def check(self, message):
        try:
            float(message.text)
            return True
        except ValueError:
            return False


bot = telebot.TeleBot(settings.BOT_TOKEN, state_storage=state_storage)

bot.set_update_listener(listener)
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(IsDigitFilter())
bot.add_custom_filter(IsNotEmptyMessageFilter())


@bot.message_handler(commands=["start"])
def start(message):
    user = message.from_user.first_name
    bot.send_message(message.chat.id, f'Hi {user}!')


@bot.message_handler(commands=["add_product"])
def add_product(message):
    """
    Start of cycle. State is clear.
    """
    bot.send_message(message.chat.id, 'OK, let`s start!')
    bot.send_message(message.chat.id, 'Which product would you like to add?')
    bot.set_state(message.from_user.id, ProductAddStates.product_name, message.chat.id)


@bot.message_handler(state="*", commands=["cancel"])
def clear_state(message):
    """
    Cancel product adding. Deleting state.
    """
    bot.send_message(message.chat.id, "Product adding was cancelled.")
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state=ProductAddStates.product_name, is_not_null=False)
def get_name_error(message):
    """
    State 1. Error handler. Will process when user sent an empty message at initial state.
    """
    bot.send_message(message.chat.id, 'Product name can`t be empty. Please try again.')


@bot.message_handler(state=ProductAddStates.product_name)
def get_name(message):
    """
    State 1. Will process when user's state is ProductAddStates.product_name.
    """
    with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as storage:
        storage['name'] = message.text

    manufacturers = Manufacturer.objects.all()
    keyboard = make_keyboard(queryset=manufacturers, storage_key='manufacturer')
    bot.send_message(chat_id=message.chat.id, text='OK. Now choose a manufacturer', reply_markup=keyboard)
    bot.set_state(message.from_user.id, ProductAddStates.manufacturer, message.chat.id)


@bot.message_handler(state=ProductAddStates.manufacturer)
def get_manufacturer(message):
    """
    State 2. Will process when user's state is ProductAddStates.manufacturer.
    """
    bot.send_message(message.chat.id, 'Great! Now please provide a short description of your product (if you want)')
    bot.set_state(message.from_user.id, ProductAddStates.description, message.chat.id)


@bot.message_handler(state=ProductAddStates.description)
def get_description(message):
    """
    State 3. Will process when user's state is ProductAddStates.description.
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as storage:
        storage['description'] = message.text

    bot.send_message(message.chat.id, 'Excellent! And how many products do you want to add?')
    bot.send_message(message.chat.id, 'Just send an empty message if you want to leave default value (default = 1)')
    bot.set_state(message.from_user.id, ProductAddStates.amount, message.chat.id)


@bot.message_handler(state=ProductAddStates.amount, is_digit=False)
def get_amount_error(message):
    """
    State 4. Error handler. Will process when user entered a string.
    """
    bot.send_message(message.chat.id, 'Looks like you are submitting a string. Please enter a number.')


@bot.message_handler(state=ProductAddStates.amount)
def get_amount(message):
    """
    State 4. Will process when user's state is ProductAddStates.amount.
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as storage:
        storage['amount'] = message.text

    bot.send_message(message.chat.id, 'Ok, good. What price do you want to sell it?')
    bot.set_state(message.from_user.id, ProductAddStates.price, message.chat.id)


@bot.message_handler(state=ProductAddStates.price)
def get_price(message):
    """
    State 5. Will process when user's state is ProductAddStates.price.
    """
    if IsDigitFilter().check(message) and IsNotEmptyMessageFilter().check(message):
        with bot.retrieve_data(message.from_user.id, message.chat.id) as storage:
            storage['price'] = message.text

        tags = Tag.objects.all()
        keyboard = make_keyboard(storage_key='tags', queryset=tags)
        bot.send_message(message.chat.id, 'And finally please select tags for your product', reply_markup=keyboard)
        bot.set_state(message.from_user.id, ProductAddStates.tags, message.chat.id)

    else:
        bot.send_message(message.chat.id, 'Something wrong! Please check your submit and enter correct product price.')
        return


@bot.message_handler(state=ProductAddStates.tags)
def get_tags(message):
    """
    State 6. Will process when user's state is ProductAddStates.tags.
    Final state of cycle
    """
    result = str()
    with bot.retrieve_data(message.from_user.id, message.chat.id) as storage:
        storage['tags'] = message.text
        result += (f'Your product:\n<b>'
                   f'Product: {storage["name"]}\n'
                   f'Manufacturer: {storage["manufacturer"]}\n'
                   f'Description: {storage["description"]}\n'
                   f'Amount: {storage["amount"]}\n'
                   f'Price: {storage["price"]}\n'
                   f'Tags: {storage["tags"]}</b>')

    bot.send_message(message.chat.id, 'Ready! Your product has been added!')
    bot.send_message(message.chat.id, result, parse_mode="html")
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    models = {
        'tags': Tag.objects.get,
        'manufacturer': Manufacturer.objects.get
    }

    callback_data: dict = callback_factory.parse(callback_data=call.data)
    storage_key = callback_data.get('storage_key')
    item_pk = callback_data.get('item_pk')

    data = models.get(storage_key)(pk=item_pk)
    with bot.retrieve_data(user_id=call.message.chat.id, chat_id=call.message.chat.id) as storage:
        storage[storage_key] = data
