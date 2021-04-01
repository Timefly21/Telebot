import telebot
bot = telebot.TeleBot('1763825074:AAFjFgtu_rFccqDKvAkWk5PCiCHYZF3qqbM')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Привет, {message.from_user.firstname} ,можешь спросить у меня про это:')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понял.')


bot.polling(none_stop=True)
