import telebot

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
    text_msg=f'/siteITStep - перехід на сайт ITStep \n/ - погода в Рівному'
    bot.send_message(message.chat.id, text_msg)

@bot.message_handler(commands=['siteITStep'])
def send_infoUrlITStep(message):
    urlStep="https://itstep.dp.ua/ru"
    text=f'Сайт академії'
    bot.send_message(message.chat.id,text,parse_mode='html')

@bot.message_handler(commands=['pogoda'])
def send_infoPog(message):
    pogoda="https://www.gismeteo.ua/ua/weather-rivne-4940/ "
    text_pog=f'Погода в рівному'
    bot.send_message(message.chat.id, text_pog)


bot.polling()