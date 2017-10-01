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
        "description": "از امواج صوت بدون آسیب به سطح پوست و به صورت متمرکز برای برای لیفت صورت و گردن استفاده می شود و هر جلسه یک و نیم ساعت است",
        "cost": "یک و نیم تا دو میلیون تومان"
    },
    {
        "name": "بوتاکس",
        "description": "",
        "cost": "از دویست و هشتاد هزار تومان تا چهارصد و هشتاد هزار تومان",
        "children": [
            {
                "name": "بوتاکس پیشانی و دور چشم",
                "cost": "از دویست هزار تومان تا چهار صد و پنجاه هزار تومان",
                "description": "",
            },
            {
                "name": "بوتاکس ضد تعریق زیر بغل",
                "cost": "پانصد هزار تومان",
                "description": "",
            },
        ]
    },
    {
        "name": "تزریق چربی",
        "description": "",
        "cost": "یک میلیون و دویست تا دو و نیم میلیون تومان"
    },
    {
        "name": "لیفت با نخ",
        "description": "",
        "cost": "یک میلیون و دویست تا دو میلیون تومان",
        "children" :[
            {
                "name": "لیفت بینی با نخ",
                "description": "",
                "cost": "یک میلیون و دویست تا دو میلیون تومان"
            },
            {
                "name": "لیفت ابرو با نخ",
                "description": "",
                "cost": "از یک میلیون تا یک میلیون و چهارصد هزار تومان"
            },
            {
                "name": "لیفت کل صورت با نخ",
                "description": "",
                "cost": "یک و نیم تا دو میلیون تومان"
            }],
    },
    {
        "name": "جراحی",
        "description": "بنا به اندازه و جای ضایعه",
        "cost": "",
        "children" :[
            {
                "name": "خال",
                "description": "",
                "cost": "از هشتاد هزار تومان تا پانصد هزار تومان"
            },
            {
                "name": "کیست",
                "description": "",
                "cost": "از هشتاد هزار تومان تا پانصد هزار تومان"
            },
            {
                "name": "لیپوم",
                "description": "",
                "cost": "از هشتاد هزار تومان تا پانصد هزار تومان"
            }
        ]
    },
    {
        "name": "لیزرهای درمانی",
        "description": "",
        "cost": "",
        "children": [
            {
                "name": "ضد جوش",
                "description": "",
                "cost": "دویست تا سیصد هزار تومان"
            },
            {
                "name": "درماتیت سبورییک",
                "description": "",
                "cost": "دویست تا سیصد هزار تومان"
            },
            {
                "name": "ضد قارچ",
                "description": "",
                "cost": "دویست تا سیصد هزار تومان"
            },
            {
                "name": "ضد لک",
                "description": "",
                "cost": "دویست تا سیصد هزار تومان"
            },
            {
                "name": "عروق",
                "description": "",
                "cost": "دویست تا سیصد هزار تومان"
            },
            {
                "name": "ضد زگیل",
                "description": "",
                "cost": "دویست تا سیصد هزار تومان"
            },
            {
                "name": "لیفت صورت",
                "description": "",
                "cost": "دویست تا سیصد هزار تومان"
            },
            {
                "name": "ضد اسکار",
                "description": "",
                "cost": "دویست تا سیصد هزار تومان"
            },
            {
                "name": "لیفت سینه",
                "description": "",
                "cost": "دویست تا سیصد هزار تومان"
            }
        ]
    },
    {
        "name": "میکرونیدلینگ",
        "description": "برای لیفت صورت و از بین بردن جای جوش و خطوط حاملگی استفاده می شود",
        "cost": "دویست تا سیصد و پنجاه هزار تومان"
    },
    {
        "name": "ژل یا فیلر",
        "description": "از ژل برای برجسته سازی لب ،گونه ،چانه ،خط خنده و زاویه سازی صورت استفاده می شود",
        "cost": "از یک سی‌سی سیصد و پنجاه هزار تا هفتصد و پنجاه هزار تومان",
    },
    {
        "name": "مزوتراپی",
        "description": "از مزوتراپی برای لاغری موضعی ، لیفت صورت ،آبرسانی و ویتامینه پوست ، ریزش مو و برای ضد لک استفاده می شود .",
        "cost": "از یکصد و هشتاد هزار تا دویست و پنجاه هزار تومان"
    },
    {
        "name": "سابسیژن",
        "description": "از ساب سیژن برای باز کردن جای جوش از لایه های زیرین استفاده می شود",
        "cost": "سیصد و پنجاه هزار تا پانصد هزار تومان"
    },
    {
        "name": "پی آر پی",
        "description": "",
        "cost": "",
        "children": [
            {
                "name": "زیر چشم",
                "description": "",
                "cost": "سیصد و پنجاه هزار تومان"
            },
            {
                "name": "صورت",
                "description": "",
                "cost": "هفتصد و پنجاه هزار تومان"
            },
            {
                "name": "صورت و گردن",
                "description": "",
                "cost": "نهصد و پنجاه هزار تومان"
            },
            {
                "name": "ریزش موی سر",
                "description": "",
                "cost": "نهصد و پنجاه هزار تومان"
            },
            {
                "name": "جای جوش",
                "description": "",
                "cost": "هفتصد و پنجاه هزار تومان"
            },
            {
                "name": "پشت دست",
                "description": "",
                "cost": "هفتصد و پنجاه هزار تومان"
            }
        ]
    },
    {
        "name": "لاغری موضعی",
        "description": "",
        "cost": "",
        "children":[
            {
                "name": "با مزوتراپی",
                "description": "",
                "cost": "جلسه ای یکصد و هشتاد هزار تومان"
            },
            {
                "name": "با کویتیشن Cavitation",
                "description": "",
                "cost": "جلسه ای یکصد و پنجاه هزار تومان"
            }
        ]
    },
    {
        "name": "طب سوزنی",
        "description": "جلسات طب سوزنی حداقل هفته ای یک بار است",
        "cost": "هفتصد و پنجاه هزار تومان",
        "children":[
            {
                "name": "لیفت صورت",
                "description": "",
                "cost": "جلسه ای یکصد و چهل هزار تومان"
            },
            {
                "name": "لیفت سینه",
                "description": "",
                "cost": "جلسه ای یکصد و چهل هزار تومان"
            },
            ]
    },
    {
        "name": "لیزر موی زاید",
        "description": ":star:قیمت ها در حال حاضر با تخفیفات ویژه می باشد",
        "cost": "",
        "children": [
            {
                "name": "کامل صورت",
                "description": "",
                "cost": "۶۰.۰۰۰"
            },
            {
                "name": "پیشانی",
                "description": "",
                "cost": "۴۰.۰۰۰"
            },
            {
                "name": "چانه",
                "description": "",
                "cost": "۴۰.۰۰۰"
            },
            {
                "name": "خط ریش",
                "description": "",
                "cost": "۶۰.۰۰۰"
            },
            {
                "name": "پشت لب",
                "description": "",
                "cost": "۳۵.۰۰۰"
            },
            {
                "name": "دست ها",
                "description": "",
                "cost": "۱۳۰.۰۰۰"
            },
            {
                "name": "بازوها",
                "description": "",
                "cost": "۶۵.۰۰۰"
            },
            {
                "name": "ساعدها",
                "description": "",
                "cost": "۶۵.۰۰۰"
            },
            {
                "name": "پاها",
                "description": "",
                "cost": "۲۵۰.۰۰۰"
            },
            {
                "name": "ران ها",
                "description": "",
                "cost": "۱۴۰.۰۰۰"
            },
            {
                "name": "ساق ها",
                "description": "",
                "cost": "۱۴۰.۰۰۰"
            },
            {
                "name": "باسن",
                "description": "",
                "cost": "۶۵.۰۰۰"
            },
            {
                "name": "بیکینی",
                "description": "",
                "cost": "۱۰۰.۰۰۰"
            },
            {
                "name": "شکم (زیر ناف)",
                "description": "",
                "cost": "۳۵.۰۰۰"
            },
            {
                "name": "زیر بغل",
                "description": "",
                "cost": "۴۵.۰۰۰"
            },
            {
                "name": "نیم تنه جلو در خانم ها",
                "description": "",
                "cost": "۱۴۰.۰۰۰"
            },
            {
                "name": "نیم تنه پشت در خانم ها",
                "description": "",
                "cost": "۱۴۰.۰۰۰"
            },
            {
                "name": "کامل بدن",
                "description": "",
                "cost": "۵۰۰.۰۰۰"
            },
        ]
    },
]
