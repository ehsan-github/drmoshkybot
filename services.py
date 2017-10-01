
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

    keyboard = InlineKeyboardMarkup([buttons])
    mybot.sendMessage(user_id, text = text, reply_markup = keyboard)
