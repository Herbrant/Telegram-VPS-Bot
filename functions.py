# -*- coding: utf-8 -*-

# Telegram
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler, CallbackQueryHandler, RegexHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)

# System libraries
import os
import psutil
# Token
tokenconf = open('config/token.conf', 'r').read()
tokenconf = tokenconf.replace("\n", "")

# Token of your telegram bot that you created from @BotFather, write it on token.conf
TOKEN = tokenconf


def cpu_cmd(bot, update):
    message = psutil.cpu_percent()
    bot.sendMessage(chat_id = update.message.chat_id, text = message)