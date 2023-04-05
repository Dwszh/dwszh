import telebot
bot=telebot.TeleBot('6238394380:AAG3WwGvOBnWVoNj3b7YBM28I7yxORjzpAo')
@bot.message_handler(commands=['start'])
def s(message):
    bot.send_message(message.chat.id, "Привет!")
bot.infinity_polling() 
