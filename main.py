import telebot
from telebot import types

bot = telebot.TeleBot('7613639105:AAGz-03wZ-VKCJB9YRvm_39WyfSA1jo_DnQ')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go to the website', url='https://classroom.google.com/c/NzA0Njg1ODMyMDk3/a/NzE5NDM0MTI5ODA5/details')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete photo!', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Edit text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'What a cute photo!', reply_markup=markup)


bot.polling(none_stop=True)