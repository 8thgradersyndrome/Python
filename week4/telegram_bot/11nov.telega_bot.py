"""
День 4. Неделя 4
Тема: Создание телеграмм бота
"""

# import telebot
# from my_tokin import token

# bot = telebot.TeleBot(token)

# # @bot.message_handler(commands = ['start','hello'])

# # def start_message(message):
# #     chat_id = message.chat.id
# #     bot.send_message(chat_id,"Hello! I'm python_test bot")

# # @bot.message_handler(content_types = ['stickers','text'])
# # def send_sticker(message):
# #     chat_id = message.chat.id
# #     if message.text.lower() == 'hello':
# #         bot.send_message(chat_id,'Hello, my dear friend')
# #     bot.send_sticker(chat_id,'CAACAgEAAxkBAAIv4WGMsF172RudZzx4LHG90SIJ5agYAALbCQACv4yQBIyHk4J79EIYIgQ')


# bot.polling()



"""
Создаем реального телеграмм бота для учёта
"""

from abc import get_cache_token
import telebot
import csv
from my_tokin import token
from telebot import types

#InlineKeyoardMarkup

bot = telebot.TeleBot(token)

entry = {}


inline_keyboard = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Доход',callback_data='income')
btn2 = types.InlineKeyboardButton('Расход',callback_data='costs')
inline_keyboard.add(btn1,btn2)




@bot.message_handler(commands = ['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,'Привет!\nСделайте выбор: ', reply_markup =inline_keyboard)


@bot.callback_query_handler(func = lambda c: True)
def inline(c): #message
    if c.data == 'income':
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard=True)
        k1 = types.KeyboardButton('Работа')
        k2 = types.KeyboardButton('Фриланс')
        k3 = types.KeyboardButton('Другое')
        income_keyboard.add(k1,k2,k3)
        msg = bot.send_message(chat_id, 'Выберите категорию', reply_markup=income_keyboard)
        bot.register_next_step_handler(msg, get_category_income)

    if c.data == 'costs':
        chat_id = c.message.chat.id
        costs_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        k1 = types.KeyboardButton('Еда')
        k2 = types.KeyboardButton('Одежда')
        k3 = types.KeyboardButton('Развлечения')
        costs_keyboard.add(k1,k2,k3)
        msg = bot.send_message(chat_id, 'Выберите категорию: ', reply_markup=costs_keyboard)
        bot.register_next_step_handler(msg,get_category_costs)


def get_category_income(message):
    chat_id = message.chat.id
    entry.update({'category': message.text}) # entry['category]==message.text
    msg =bot.send_message(chat_id, 'Укажите сумму :')
    bot.register_next_step_handler(msg,get_sum_income)
def get_category_costs(message):
    chat_id = message.chat.id
    entry.update({'category': message.text}) # entry['category]==message.text
    msg =bot.send_message(chat_id, 'Укажите сумму :')
    bot.register_next_step_handler(msg,get_sum_costs)

def get_sum_income(message):
    chat_id = message.chat.id
    entry.update({'sum':message.text})

    file_name = 'income.csv'

    with open(file_name,'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((entry['category'], entry['sum']))

    bot.send_message(chat_id,'Ваши доходы добавлены.',reply_markup=inline_keyboard)
    bot.send_sticker(chat_id,'CAACAgEAAxkBAAIv62GMvlt1JzPuC1v2-ksDlz5SHz5iAALsCQACv4yQBHT8UgZI2ZM3IgQ')


def get_sum_costs(message):
    chat_id = message.chat.id
    entry.update({'sum':message.text})

    file_name = 'costs.csv'

    with open(file_name,'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((entry['category'], entry['sum']))

    bot.send_message(chat_id,'Ваши расходы добавлены.',reply_markup=inline_keyboard)
    bot.send_sticker(chat_id,'CAACAgEAAxkBAAIv52GMvj-vIX1JIe-UNU8KN3EuQ_mUAALxCQACv4yQBNt3GhNqThnSIgQ')


bot.polling()

