import telebot


bot = telebot.TeleBot("")


@bot.message_handler(commands=["start"])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=telebot.types.KeyboardButton("Получить список всех продуктов")
    item2=telebot.types.KeyboardButton("Внести новый продукт в базу")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'wefwef', reply_markup=markup)


@bot.message_handler(content_types=["text"])




@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Получить список всех продуктов':
        ...
    elif message.text.strip() == 'Внести новый продукт в базу':
            answer = random.choice(thinks)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
if 


bot.polling(none_stop=True)
