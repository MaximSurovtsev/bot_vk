import telebot

bot = telebot.TeleBot('776916341:AAHSc2BAGKHguLsfOoguAfN0Ogiz4bliv_0')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Дарова')

@bot.message_handler(func=lambda meesage: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
