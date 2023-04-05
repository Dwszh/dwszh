import telebot
bot=telebot.TeleBot('token')
@bot.message_handler(commands=['start'])
def s(message):
    bot.send_message(message.chat.id, "Привет!")
bot.infinity_polling() 
