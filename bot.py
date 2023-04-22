import telebot
from telebot import types
API = "6238394380:AAG3WwGvOBnWVoNj3b7YBM28I7yxORjzpAo"
bot = telebot.TeleBot(API)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton('Чонгук')
    item2=types.KeyboardButton('Техён')
    item3=types.KeyboardButton('Чимин')
    markup.add(item1,item2,item3)
    bot.send_message(message.chat.id,"Pruvet! Choose what character's photo you need",reply_markup=markup)

@bot.message_handler(content_types='text')
def reply_message(message):
    Jungkook = "https://www.yesasia.ru/wp-content/uploads/2023/03/IMG_20230328_141654_267-700x875.jpg"
    Taehyung = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/V_on_the_Billboard_Music_Awards_red_carpet%2C_1_May_2019_02.jpg/640px-V_on_the_Billboard_Music_Awards_red_carpet%2C_1_May_2019_02.jpg"
    Jimin = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Park_Ji-min_at_Music_Bank_in_Singapore_01.jpg/200px-Park_Ji-min_at_Music_Bank_in_Singapore_01.jpg"
    if message.text == "Чонгук":
        bot.send_photo(message.chat.id, Jungkook)
    elif message.text == "Техён":
        bot.send_photo(message.chat.id, Taehyung)
    elif message.text == "Чимин":
        bot.send_photo(message.chat.id, Jimin)

bot.infinity_polling()
