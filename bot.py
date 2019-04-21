import telebot
import requests
import time

bot = telebot.TeleBot('776916341:AAHSc2BAGKHguLsfOoguAfN0Ogiz4bliv_0')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Дарова')
    
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval = 0, timeout = 20) 
        except Exception as err:
            print("MAIN ", err)
            time.sleep(1)
