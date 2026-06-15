import telebot

bot = telebot.TeleBot('8753083541:AAHDhWNO4BTvbSEukJ6E1LHsIDO6H5i25Fk')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет! Рад нашему знакомству!</b>', parse_mode='HTML')

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}")

@bot.message_handler(commands=['site'])
def site(message):
    bot.send_message(message.chat.id, 'Открыть браузер: https://yandex.ru')

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, 'Превосходное фото!')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет' or message.text.lower() == 'Привет' or message.text.lower() == 'Hello' or message.text.lower() == 'hello' or message.text.lower() == 'hi' or message.text.lower() == 'Hi':
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}")
    elif message.text.lower() == 'id' or message.text.lower() == 'ID' or message.text.lower() == 'Id':
        bot.send_message(message.chat.id, f"ID: {message.from_user.id}")

bot.polling(none_stop=True)