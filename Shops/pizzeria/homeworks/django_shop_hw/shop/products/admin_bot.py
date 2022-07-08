import telebot
from telebot import custom_filters, SimpleCustomFilter, types
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from telebot.callback_data import CallbackData
from django.conf import settings
from .models import Product, Tag, Manufacturer
from .shop_service import ProductsService

state_storage = StateMemoryStorage()
callback_factory = CallbackData("model_name", "item_pk", "user_id", "chat_id", prefix="products")
product_service = ProductsService()


def make_keyboard(queryset, user_id, chat_id):
    keyboard = types.InlineKeyboardMarkup()
    model_name = queryset.model.__name__
    for item in queryset:
        callback_data = callback_factory.new(model_name=model_name, item_pk=item.pk, user_id=user_id, chat_id=chat_id)
        keyboard.add(types.InlineKeyboardButton(text=str(item), callback_data=callback_data))
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


class IsFloatDigitFilter(SimpleCustomFilter):
    """
    Filter to check the given string is digit (float or int).
    """

    key = 'is_float_digit'

    def check(self, message):
        try:
            float(message.text)
            return True
        except ValueError:
            return False


bot = telebot.TeleBot(settings.BOT_TOKEN, state_storage=state_storage)

bot.set_update_listener(listener)
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
bot.add_custom_filter(IsFloatDigitFilter())


@bot.message_handler(commands=["start"])
def start(message):
    user = message.from_user.first_name
    bot.send_message(message.chat.id, f'Hi {user}!')


@bot.message_handler(commands=["add_product"])
def add_new_product(message):
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


@bot.message_handler(state=ProductAddStates.product_name)
def add_manufacturer(message):
    """
    State 1. Will process when user's state is ProductAddStates.product_name.
    """
    with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as storage:
        storage['name'] = message.text

    manufacturers = Manufacturer.objects.all()
    keyboard = make_keyboard(queryset=manufacturers, chat_id=message.chat.id, user_id=message.from_user.id)
    bot.send_message(chat_id=message.chat.id, text='OK. Now choose a manufacturer', reply_markup=keyboard)
    bot.set_state(chat_id=message.chat.id, state=ProductAddStates.manufacturer, user_id=message.from_user.id)


def add_description(chat_id, user_id):
    """
    State 2. Will process when user's state is ProductAddStates.manufacturer.
    """
    bot.set_state(chat_id=chat_id, state=ProductAddStates.description, user_id=user_id)
    bot.send_message(chat_id=chat_id, text='Great! Now please provide a short description of your product')


@bot.message_handler(state=ProductAddStates.description)
def add_amount(message):
    """
    State 3. Will process when user's state is ProductAddStates.description.
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as storage:
        storage['description'] = message.text

    bot.send_message(message.chat.id, 'Excellent! And how many products do you want to add?')
    bot.set_state(message.from_user.id, ProductAddStates.amount, message.chat.id)


@bot.message_handler(state=ProductAddStates.amount, is_digit=False)
def add_amount_error(message):
    """
    Error handler. Will process when user entered a string or float number.
    """
    bot.send_message(message.chat.id, 'Something wrong! Please check your submit and enter correct product price.')


@bot.message_handler(state=ProductAddStates.amount)
def add_price(message):
    """
    State 4. Will process when user's state is ProductAddStates.amount.
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as storage:
        storage['amount'] = message.text

    bot.send_message(message.chat.id, 'Ok, good. What price do you want to sell it?')
    bot.set_state(message.from_user.id, ProductAddStates.price, message.chat.id)


@bot.message_handler(state=ProductAddStates.price, is_float_digit=False)
def add_price_error(message):
    """
    Error handler. Will process when user entered a string.
    """
    bot.send_message(message.chat.id, 'Looks like you are submitting a string. Please enter a number.')


@bot.message_handler(state=ProductAddStates.price)
def add_tags(message):
    """
    State 5. Will process when user's state is ProductAddStates.price.
    """
    if IsFloatDigitFilter().check(message):
        with bot.retrieve_data(message.from_user.id, message.chat.id) as storage:
            storage['price'] = message.text

        tags = Tag.objects.all()
        keyboard = make_keyboard(queryset=tags, user_id=message.from_user.id, chat_id=message.chat.id)
        bot.send_message(message.chat.id, 'And finally please select tags for your product', reply_markup=keyboard)
        bot.set_state(message.from_user.id, ProductAddStates.tags, message.chat.id)


def add_another_tag(chat_id, user_id):
    tags = Tag.objects.all()
    text = 'Wanna add another one tag? Or type /enough_tags to go to the next step.'
    keyboard = make_keyboard(queryset=tags, user_id=user_id, chat_id=chat_id)
    bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard)


@bot.message_handler(state=ProductAddStates.tags, commands=["enough_tags"])
def show_result(message):
    """
    State 6. Will process when user's state is ProductAddStates.tags.
    Final state of cycle
    """
    result = str()
    with bot.retrieve_data(user_id=message.chat.id, chat_id=message.chat.id) as storage:
        result += (f'<b>Your product:\n</b>'
                   f'<b>Product:</b> <em>{storage["name"]}</em>\n'
                   f'<b>Manufacturer:</b> <em>{storage["manufacturer"]}</em>\n'
                   f'<b>Description:</b> <em>{storage["description"]}</em>\n'
                   f'<b>Amount:</b> <em>{storage["amount"]}</em>\n'
                   f'<b>Price:</b> <em>{storage["price"]}</em>\n'
                   f'<b>Tags:</b> <em>{[str(tag) for tag in storage["tags"]]}</em>')

        product_service.add_product(**storage)
    bot.send_message(chat_id=message.chat.id, text='Ready! Your product has been added!')
    bot.send_message(chat_id=message.chat.id, text=result, parse_mode="html")
    bot.delete_state(user_id=message.chat.id, chat_id=message.chat.id)


def process_tags(data: dict):
    chat_id = int(data.get('chat_id'))
    user_id = int(data.get('user_id'))
    item_pk = data.get('item_pk')

    tag = Tag.objects.get(pk=item_pk)

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as storage:
        tags = storage.get('tags', set())
        tags.add(tag)
        storage['tags'] = tags

    add_another_tag(chat_id=chat_id, user_id=user_id)


def process_manufacturer(data: dict):
    chat_id = int(data.get('chat_id'))
    user_id = int(data.get('user_id'))
    item_pk = data.get('item_pk')

    manufacturer = Manufacturer.objects.get(pk=item_pk)

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as storage:
        storage['manufacturer'] = manufacturer

    add_description(chat_id=chat_id, user_id=user_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    models = {
        'Manufacturer': process_manufacturer,
        'Tag': process_tags
    }

    callback_data = callback_factory.parse(callback_data=call.data)
    model_name = callback_data.get('model_name')
    models.get(model_name)(callback_data)
    bot.answer_callback_query(call.id)
