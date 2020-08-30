from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html


import random






from telegram.ext import Updater, CommandHandler

Token = "1353108206:AAFUorULABdLOhh3tsxPmQAxQMs3vtmGemw"

RUN_STRINGS = ('hzhsh','nmk','hsjsj')

nmm = random.choice(RUN_STRINGS)

def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def hi(update, context):
    update.message.reply_text((random.choice(RUN_STRINGS)) .format(update.message.from_user.first_name))
        
        
        



updater = Updater(Token, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', hello))

updater.dispatcher.add_handler(CommandHandler('help', hi))


updater.start_polling()
updater.idle()
