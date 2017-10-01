
# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import constants
import re


def call_handler(bot, update):
    query = update.callback_query
    msg_id = query.message.message_id
    user_id = query.from_user.id
    splited_query = query.data.split("_")
    type = splited_query[0]
    index = int(splited_query[1])
    service = constants.SERVICES[index]
    service_name = service["name"]
    service_description = service["description"]
    service_cost = service["cost"]

    if type == "service" :
            buttons = [
                (InlineKeyboardButton(text='cost', callback_data="cost_"+str(index))),
            ]
            keyboard = InlineKeyboardMarkup([buttons,
                                             [(InlineKeyboardButton(text='liste khadamat', callback_data="menu_1"))],
            ])
            bot.editMessageText(chat_id = user_id, message_id = msg_id, text = service_name +'\n'+service_description, reply_markup = keyboard)

    elif type == "cost" :
            buttons = [(InlineKeyboardButton(text='tozihat', callback_data="service_"+str(index)))]
            keyboard = InlineKeyboardMarkup([buttons,
                                             [(InlineKeyboardButton(text='liste khadamat', callback_data="menu_1"))]])
            bot.editMessageText(chat_id = user_id, message_id = msg_id, text = service_name +'\n'+service_cost, reply_markup = keyboard)

    elif type == "menu" :
        text = 'از خدمات زیر انتخاب کنید'
        buttons = [InlineKeyboardButton(text=x["name"], callback_data="service_"+str(index)) for index, x in enumerate(constants.SERVICES)]
        keyboard = InlineKeyboardMarkup([buttons])
        bot.editMessageText(chat_id = user_id, message_id = msg_id, text = text, reply_markup = keyboard)

    bot.answerCallbackQuery(query.id, text='loaded'+ service_name)
    return constants.STATE_MAIN

def enToPersianNumb(number):
    dic = {
        '0':'۰',
        '1':'۱',
        '2':'۲',
        '3':'۳',
        '4':'۴',
        '5':'۵',
        '6':'۶',
        '7':'۷',
        '8':'۸',
        '9':'۹',
        '.':'.',
    }
    return multiple_replace(dic, number)

def multiple_replace(dic, text):
    pattern = "|".join(map(re.escape, dic.keys()))
    return re.sub(pattern, lambda m: dic[m.group()], str(text))
