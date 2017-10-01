#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
import logging
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, NetworkError)
import constants
import functions
import services

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger('drMoshky')

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    from_user = update.message.chat
    bot.sendMessage(update.message.chat_id,\
                    text ="سلام {} به ربات مطب دکتر مشکی خوش‌آمدید\n.".format(from_user.first_name), reply_markup = constants.KEYBOARD_MAIN)
    return constants.STATE_MAIN

def stop_this_fucking_bot(bot, update):
    return ConversationHandler.END

def main_menue_handler(bot, update):
    message = update.message.text
    if (message == 'آدرس مطب'):
        bot.sendMessage(update.message.chat_id,
                        text = 'آدرس مطب : کرج مهرشهر بلوارشهرداری فاز دو بین خیابان 206 و 208 جنب بانک ملی بالای شیرینی بیسکوتی . طبقه دوم . واحد چهارم .\n026-33419204\n Instagram : dr_moshky', reply_markup=constants.KEYBOARD_MAIN)

        return constants.STATE_MAIN
    elif (message == 'لیست خدمات'):
        services.select_service(bot, update.message.chat_id)
        return constants.STATE_MAIN
    else:
        bot.sendMessage(update.message.chat_id, text = 'لطفا از منوی زیر انتخاب کنید', reply_markup=constants.KEYBOARD_MAIN)

def wrong_call_handler(bot, update):
    query = update.callback_query
    bot.answerCallbackQuery(query.id,text= 'این دکمه ها کار نمیکنن تا زمانی که برگردی به منوی اصلی')

def skip(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='برگشتید به منوی اصلی', reply_markup = constants.KEYBOARD_MAIN)
    return constants.STATE_MAIN

def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        print('Unauthorized')
    except BadRequest:
        print('BadRequest')
    except TimedOut:
        print('TimedOut')
    except NetworkError:
        print('NetworkError')
    except TelegramError:
        print('TelegramError')

def show_how_to_work_with_bot(bot, u_id):
    bot.sendMessage(chat_id=u_id, text= constants.HOW_TO_WORK_WITH_BOT)

def main():
    print(constants.TOKEN)
    updater = Updater(constants.TOKEN)
    main_conversationhandler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                      MessageHandler([Filters.text], main_menue_handler),
                      CallbackQueryHandler(functions.call_handler)],
        states={
            constants.STATE_MAIN: [MessageHandler([Filters.text], main_menue_handler),
                                   CallbackQueryHandler(functions.call_handler)],

            constants.STATE_SERVICES:  [MessageHandler([Filters.text], services.select_service),
                                   CallbackQueryHandler(wrong_call_handler)],
        },
        fallbacks=[CommandHandler('stop', stop_this_fucking_bot)])

    dp = updater.dispatcher

    # add conversation handler
    dp.add_handler(main_conversationhandler)
    # log all errors
    dp.add_error_handler(error_callback)

    # Start the Bot
    updater.start_polling()

    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
