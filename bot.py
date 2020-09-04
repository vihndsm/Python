import telebot
from telebot import types
import mysql.connector

bot = telebot.TeleBot('1104474861:AAEe7_kXP84eEpiK3gNmqOQPjPnUclgkpeI')

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_menu = types.KeyboardButton('Меню')
btn_Basket = types.KeyboardButton('Корзина')
btn_instruction = types.KeyboardButton('Мои данные')
btn_message = types.KeyboardButton('Помощь')
markup_menu.add(btn_menu, btn_Basket, btn_instruction, btn_message)

markup_name = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
btn_name = types.KeyboardButton('Изменить имя')
btn_address = types.KeyboardButton('Изменить адресс')
btn_number = types.KeyboardButton('Изменить номер')
btn_back = types.KeyboardButton('Вернуться в меню')
markup_name.add(btn_back)
markup_name.add(btn_name, btn_address)
markup_name.add(btn_number)

markup_country = types.InlineKeyboardMarkup(row_width=1)
btn_it = types.InlineKeyboardButton('Итальянская', callback_data='IT')
btn_kt = types.InlineKeyboardButton('Китайская', callback_data='QT')
markup_country.add(btn_it, btn_kt)

markup_eat = types.InlineKeyboardMarkup(row_width=2)
btn_cold = types.InlineKeyboardButton('Холодные блюда', callback_data='cold')
btn_hot = types.InlineKeyboardButton('Горячие блюда', callback_data='hot')
btn_Barbecue = types.InlineKeyboardButton('Шашлык', callback_data='Barbecue')
btn_Salads = types.InlineKeyboardButton('Салаты', callback_data='Salads')
btn_Garnishes = types.InlineKeyboardButton('Гарниры', callback_data='Garnishes')
btn_drinks = types.InlineKeyboardButton('Напитки', callback_data='drinks')
markup_eat.add(btn_cold, btn_hot, btn_Barbecue, btn_Salads, btn_Garnishes, btn_drinks)

markup_eat1 = types.InlineKeyboardMarkup(row_width=2)
btn_cold1 = types.InlineKeyboardButton('Холодные блюда', callback_data='cold1')
btn_hot1 = types.InlineKeyboardButton('Горячие блюда', callback_data='hot1')
btn_Barbecue1 = types.InlineKeyboardButton('Шашлык', callback_data='Barbecue1')
btn_Salads1 = types.InlineKeyboardButton('Салаты', callback_data='Salads1')
btn_Garnishes1 = types.InlineKeyboardButton('Гарниры', callback_data='Garnishes1')
btn_drinks1 = types.InlineKeyboardButton('Напитки', callback_data='drinks1')
markup_eat1.add(btn_cold1, btn_hot1, btn_Barbecue1, btn_Salads1, btn_Garnishes1, btn_drinks1)

def requestdb(ID, user):
    bot.send_message(ID, 'Добро пожаловать, *'+user+'*!',
                     parse_mode='Markdown', reply_markup=markup_menu)
    conn = mysql.connector.connect(host='localhost', database='TG', user='aito', password='aitoFull1@')
    c = conn.cursor()
    c.execute("SELECT ID FROM aito WHERE ID = {}".format(ID))
    result = c.fetchone()
    if result == None:
        add_SQL1 = "INSERT INTO aito (ID, do) VALUES (%s, %s)"
        P_sql1 = (ID, 0)
        c.execute(add_SQL1, P_sql1)
        conn.commit()
        conn.close()
    else:
        c.execute("UPDATE aito SET do=%s WHERE id=%s", (0, ID))
        conn.commit()
        conn.close()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    requestdb(message.chat.id, message.chat.first_name)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    conn = mysql.connector.connect(host='localhost', database='TG', user='aito', password='aitoFull1@')
    c = conn.cursor()
    c.execute("SELECT * FROM aito WHERE ID = {}".format(message.chat.id))
    result = c.fetchone()

    if result == None:
        requestdb(message.chat.id, message.chat.first_name)

    if message.text == "Меню":
        bot.send_message(message.chat.id, text="Выберите раздел, чтобы вывести список блюд", reply_markup=markup_country)

    elif message.text == "Мои данные":
        bot.send_message(message.chat.id, '*Ваши данные*:'
                                          '\n\nИмя: '+str(result[1])+
                                          '\nАдресс: '+str(result[2])+
                                          '\nНомер:'+str(result[3]), parse_mode='Markdown', reply_markup=markup_name)
    elif message.text == "Вернуться в меню":
        requestdb(message.chat.id, message.chat.fetchonefirst_name)

    elif message.text == "Изменить имя":
        bot.send_message(message.chat.id, text="Введите ваше имя")
        conn = mysql.connector.connect(host='localhost', database='TG', user='aito', password='aitoFull1@')
        c = conn.cursor()
        c.execute("UPDATE aito SET do=%s WHERE id=%s", (1, message.chat.id))
        conn.commit()
        conn.close()

    elif message.text == "Изменить адресс":
        bot.send_message(message.chat.id, text="Введите ваш адресс")
        conn = mysql.connector.connect(host='localhost', database='TG', user='aito', password='aitoFull1@')
        c = conn.cursor()
        c.execute("UPDATE aito SET do=%s WHERE id=%s", (2, message.chat.id))
        conn.commit()
        conn.close()

    elif message.text == "Изменить номер":
        bot.send_message(message.chat.id, text="Введите ваш номер")
        conn = mysql.connector.connect(host='localhost', database='TG', user='aito', password='aitoFull1@')
        c = conn.cursor()
        c.execute("UPDATE aito SET do=%s WHERE id=%s", (3, message.chat.id))
        conn.commit()
        conn.close()

    elif result[4] == 1:
        conn = mysql.connector.connect(host='localhost', database='TG', user='aito', password='aitoFull1@')
        c = conn.cursor()
        c.execute("UPDATE aito SET name=%s, do=%s WHERE id=%s", (message.text, 0, message.chat.id))
        conn.commit()
        conn.close()
        bot.send_message(message.chat.id, text="Имя успешно измененно", reply_markup=markup_name)

    elif result[4] == 2:
        conn = mysql.connector.connect(host='localhost', database='TG', user='aito', password='aitoFull1@')
        c = conn.cursor()
        c.execute("UPDATE aito SET address=%s, do=%s WHERE id=%s", (message.text, 0, message.chat.id))
        conn.commit()
        conn.close()
        bot.send_message(message.chat.id, text="Адресс успешно изменён", reply_markup=markup_name)

    elif result[4] == 3:
        conn = mysql.connector.connect(host='localhost', database='TG', user='aito', password='aitoFull1@')
        c = conn.cursor()
        c.execute("UPDATE aito SET namber=%s, do=%s WHERE id=%s", (message.text, 0, int(message.chat.id)))
        conn.commit()
        conn.close()
        bot.send_message(message.chat.id, text="Номер успешно изменён", reply_markup=markup_name)

@bot.callback_query_handler(func=lambda call:True)
def call_back_baton(call):
    if call.data == 'IT':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Итальянская: ", reply_markup=markup_eat)
    elif call.data == 'QT':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Китайская: ", reply_markup=markup_eat1)
    #кнопки разделы блюд, даделай по аналогии
    elif call.data == 'cold':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Итальянская кухня, холодные блюда: ")

bot.polling()