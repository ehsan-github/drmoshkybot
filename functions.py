
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
    if len(splited_query) > 2:
        service = constants.SERVICES[index]["children"][int(splited_query[2])]
    else:
        service = constants.SERVICES[index]
    service_name = service["name"]
    service_description = service["description"]
    service_cost = service["cost"]

    if type == "service" :
        if "children" in service:
            service_children = service["children"]
            text = 'از خدمات '+service_name+' زیر انتخاب کنید'
            buttons = [InlineKeyboardButton(text=x["name"], callback_data="service_"+str(index)+"_"+str(idx)) for idx, x in enumerate(service_children)]
            keyboard = InlineKeyboardMarkup([
                buttons[0:1],
                buttons[1:2],
                buttons[2:3],
                buttons[3:4],
                buttons[4:5],
                buttons[5:6],
                buttons[6:7],
                buttons[7:8],
                buttons[8:9],
                buttons[9:10],
                buttons[10:11],
                [InlineKeyboardButton(text="<-", callback_data="menu_1")]
            ])
            bot.editMessageText(chat_id = user_id, message_id = msg_id, text = text, reply_markup = keyboard)

        elif len(splited_query) > 2:
            childIndex = int(splited_query[2])
            buttons = [
                (InlineKeyboardButton(text='هزینه', callback_data="cost_"+str(index)+"_"+str(childIndex))),
            ]
            keyboard = InlineKeyboardMarkup([buttons,
                                             [(InlineKeyboardButton(text='<-', callback_data="service_"+str(index)))],
            ])
            bot.editMessageText(chat_id = user_id, message_id = msg_id, text = service["name"] +'\n'+service["description"], reply_markup = keyboard)
        else:
            buttons = [
                (InlineKeyboardButton(text='هزینه', callback_data="cost_"+str(index))),
            ]
            keyboard = InlineKeyboardMarkup([buttons,
                                             [(InlineKeyboardButton(text='<-', callback_data="menu_1"))],
            ])
            bot.editMessageText(chat_id = user_id, message_id = msg_id, text = service_name +'\n'+service_description, reply_markup = keyboard)


    elif type == "cost" :
        if len(splited_query) > 2:
            childIndex = int(splited_query[2])
            buttons = [
                (InlineKeyboardButton(text='توضیحات', callback_data="service_"+str(index)+"_"+str(childIndex))),
            ]
            keyboard = InlineKeyboardMarkup([buttons,
                                             [(InlineKeyboardButton(text='<-', callback_data="service_"+str(index)))],
            ])
            bot.editMessageText(chat_id = user_id, message_id = msg_id, text = service["name"] +'\n'+service["cost"], reply_markup = keyboard)
        else:
            buttons = [(InlineKeyboardButton(text='توضیحات', callback_data="service_"+str(index)))]
            keyboard = InlineKeyboardMarkup([buttons,
                                             [(InlineKeyboardButton(text='<-', callback_data="menu_1"))]])
            bot.editMessageText(chat_id = user_id, message_id = msg_id, text = service_name +'\n'+service_cost, reply_markup = keyboard)

    elif type == "menu" :
        text = 'از خدمات زیر انتخاب کنید'
        buttons = [InlineKeyboardButton(text=x["name"], callback_data="service_"+str(index)) for index, x in enumerate(constants.SERVICES)]
        keyboard = InlineKeyboardMarkup([buttons[0:2],buttons[2:4],buttons[4:6], buttons[6:8], buttons[8:10], buttons[10:12], buttons[12:14], buttons[14:16]])
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
