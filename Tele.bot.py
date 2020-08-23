
# # pip install pyTelegramBotAPI==3.7.2
# import telebot

# bot = telebot.TeleBot('1104474861:AAEe7_kXP84eEpiK3gNmqOQPjPnUclgkpeI')

# keyboard1 = telebot.types.ReplyKeyboardMarkup()
# keyboard1.row('Привет', 'Пока')

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет, мой создатель')
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')
#     elif message.text.lower() == 'хай':
#         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDFV8_wMJ--2k7VjLIWOWB5Q12ne4xAAKBEQACPLPFB0bAzHDYX3P9GwQ')

# @bot.message_handler(content_types=['sticker'])
# def sticker_id(message):
#     print(message)

# bot.polling()