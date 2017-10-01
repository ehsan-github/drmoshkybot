#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Constants
"""
"""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.environ['TELEGRAM_TOKEN_DR_MOSHKY']

STATE_MAIN = 0
STATE_SERVICES = 1


KEYBOARD_MAIN = ReplyKeyboardMarkup([
    [KeyboardButton(text='آدرس مطب'),KeyboardButton(text='لیست خدمات')],
], resize_keyboard = True)

KEYBOARD_READ = ReplyKeyboardMarkup([
    [KeyboardButton(text='متفرقه'), KeyboardButton(text='چجو')],
    [KeyboardButton(text='⬅️')]
], resize_keyboard =True)

SERVICES = [
    {
        "name": "هایفو",
        "description": "haifo chize khubie",
        "cost": "1000$"
    },
    {
        "name": "بوتاکس",
        "description": "botax chize khubie",
        "cost": "2000$"
    },
    {
        "name": "تزریق چربی",
        "description": "tazriqe charbi chize khubie",
        "cost": "1000$"
    }
]
