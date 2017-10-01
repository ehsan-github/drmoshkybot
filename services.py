
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Services
"""
"""
from telegram.ext import ConversationHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import constants


def select_service(mybot, user_id):
    text = 'از خدمات زیر انتخاب کنید'

    buttons = [InlineKeyboardButton(text=x["name"], callback_data="service_"+str(index)) for index, x in enumerate(constants.SERVICES)]

    keyboard = InlineKeyboardMarkup([buttons[0:2],buttons[2:4],buttons[4:6], buttons[6:8],buttons[8:10], buttons[10:12], buttons[12:14], buttons[14:16]])
    mybot.sendMessage(user_id, text = text, reply_markup = keyboard)
