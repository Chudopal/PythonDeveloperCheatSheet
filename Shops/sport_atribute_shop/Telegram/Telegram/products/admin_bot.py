import telebot


# Создаем экземпляр бота
bot = telebot.TeleBot('5534490508:AAFzDe0bzRBjE-PYZ1W1wdNqRp0XCwZxOEM')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(massage):
    bot.send_message(massage.chat.id, 'Привет, какие продукты ты хочешь добавить?')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    
# Запускаем бота
bot.polling(none_stop=True, interval=0)