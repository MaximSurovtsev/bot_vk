import telebot
import requests
import time
from bs4 import BeautifulSoup
bot = telebot.TeleBot('776916341:AAHSc2BAGKHguLsfOoguAfN0Ogiz4bliv_0')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Я жив!')

@bot.message_handler(commands=['posts'])
def send_posts(message):
    req = requests.get('https://habr.com/ru/')
    soup = BeautifulSoup(req.text, 'html.parser')
    links = soup.find_all('a', {'class':'post__title_link'})
    titles = soup.find_all('h2', {'class':'post__title'})
    bot.send_message(message.chat.id, '\n'.join([title.get_text().strip()+'\n'+link['href']+'\n' for title,link in zip(titles, links)]))
   
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval = 0, timeout = 20) 
        except Exception as err:
            print("MAIN ", err)
            time.sleep(1)
