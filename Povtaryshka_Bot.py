import telebot

token = '8753083541:AAHDhWNO4BTvbSEukJ6E1LHsIDH5i25Fk'
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я твой новый бот. Напиши мне что-нибудь!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты сказал: {message.text}")

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, 'Какое красивое фото!')

print("Бот запущен и ждет сообщений...")
bot.infinity_polling()