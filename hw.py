import telebot
import requests
from bs4 import BeautifulSoup

tocken="5942961078:AAECwHEwhqqVrYVv1M5Kr9TKl86jeHVHAnA"

bot=telebot.TeleBot(tocken)
'''
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message,"Welcome to talk")
'''
@bot.message_handler(commands=['start'])
def send_welcome(message):
    #print(message)
    #print(message.chat.id)
    bot.send_message(message.chat.id,"Welcome to talk")

@bot.message_handler(commands=['help'])
def send_infoHelp(message):
    text_msg=f'/siteITStep - перехід на сайт ITStep'
    bot.send_message(message.chat.id, text_msg)

@bot.message_handler(commands=['ownerBot'])
def send_owner_info(message):
    bot.send_message(message.chat.id, 'Розробник: Яна Прізвище: Коптюх\nЗахоплення: малювання')


def get_usd_rate():
    url = 'https://bank.gov.ua/ua/markets/exchangerates?date='
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='exchange-rate-table')
    rows = table.find_all('tr')
    usd_row = None
    for row in rows:
        if 'Долар США' in row.text:
            usd_row = row
            break

    usd_rate = None
    if usd_row:
        cols = usd_row.find_all('td')
        usd_rate = cols[2].text.strip()

    return usd_rate

@bot.message_handler(commands=['usd'])
def usd_rate_handler(message):
    usd_rate = get_usd_rate()
    if usd_rate:
        response_text = f"Поточний курс долара: {usd_rate} грн/дол"
    else:
        response_text = "На жаль, не вдалося отримати курс долара на сьогодні"
    bot.reply_to(message, response_text)








bot.polling()