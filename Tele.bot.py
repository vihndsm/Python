
# # pip install pyTelegramBotAPI==3.7.2
# import telebot

# bot = telebot.TeleBot('1104474861:AAEe7_kXP84eEpiK3gNmqOQPjPnUclgkpeI')

# keyboard1 = telebot.types.ReplyKeyboardMarkup()
# keyboard1.row('привет', 'как дела', 'пока')

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет, мой создатель')
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')
#     elif message.text.lower() == 'как дела':
#         bot.send_message(message.chat.id, 'отлично, создатель')
#     elif message.text.lower() == 'хай':
#         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIEP19DQpae5NVLBD5wEbhyrcQ3y8CBAAL3AAP3AsgP0JfeP4rRPA4bBA')
#     else:
#         bot.send_message(message.chat.id, 'я не понимаю Вас, создатель')

# # @bot.message_handler(content_types=['sticker'])
# # def sticker_id(message):
# #     print(message)

# bot.polling()