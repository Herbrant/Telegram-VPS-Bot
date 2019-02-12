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

#Admin chatid
adminconf = open('config/admin.conf', 'r').read()
adminconf = adminconf.replace("\n", "")
ADMIN = int(adminconf)

#Admingroup chatid
adminconf = open('config/admingroup.conf', 'r').read()
adminconf = adminconf.replace("\n", "")
ADMINGROUP = int(adminconf)

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def print_memory(nt):
    memory = ""
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        else:
            value = str(value) + '%'
        value = str(value)
        memory += name.capitalize() + ': \t'  + value + "\n"
        
    return memory

# def disk_info():
#     templ = "%-17s %8s %8s %8s %5s"
#     disk = templ % ("Device", "Total", "Used", "Free", "Use\n")

#     for part in psutil.disk_partitions(all= False):
#         usage = psutil.disk_usage(part.mountpoint)

#         disk += templ % (
#                 part.device,
#                 bytes2human(usage.total),
#                 bytes2human(usage.used),
#                 bytes2human(usage.free),
#                 int(usage.percent)) + "%\n"
#         disk = str(disk).replace("/dev", "")
    
#     return disk

def info_cmd(bot, update):
    chat_id = update.message.chat_id
    if chat_id == ADMIN or chat_id == ADMINGROUP:
        info = "*----VPS INFO----*\n\n"
        
        #CPU
        cpu = "*--CPU--*\n"
        cpu += "Percent:\t" + str(psutil.cpu_percent()) + "%\n"
        freq = str(psutil.cpu_freq()).replace("scpufreq", '')
        cpu += "Frequencies:\t" + freq + "\n"
        cpu += "Stats:\t" + str(psutil.cpu_stats()).replace("scpustats", "") + "\n"
        cpu += "Cores:\t" + str(psutil.cpu_count()) + "\n\n"
        
        #RAM
        ram = '*--RAM--*\n' + print_memory(psutil.virtual_memory()) + "\n"
        #SWAP
        swap = '*--SWAP--*\n' + print_memory(psutil.swap_memory()) + "\n"

        #DISK
        #disk = '*--DISK--*\n' + str(disk_info()) + "\n"
        message = info + cpu + ram + swap
        bot.sendMessage(chat_id = chat_id, text = message,  parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        message = "You're not allowed :)"
        bot.sendMessage(chat_id = chat_id, text = message,  parse_mode=telegram.ParseMode.MARKDOWN)


def alert_cmd(bot, update):
    cpuval = psutil.cpu_percent()
    if cpuval > 80.0:
        message = "*ALERT CPU USAGE!*\n" + "Percent:\t" + str(cpuval) + "%"
        bot.sendMessage(chat_id = ADMIN, text = message, parse_mode=telegram.ParseMode.MARKDOWN)
        bot.sendMessage(chat_id = ADMINGROUP, text = message, parse_mode=telegram.ParseMode.MARKDOWN)
    
    ramval = psutil.virtual_memory()[2]
    if ramval > 75.0:
        message = "*ALERT RAM USAGE!*\n" + "Percent:\t" + str(ramval) + "%"
        bot.sendMessage(chat_id = ADMIN, text = message, parse_mode=telegram.ParseMode.MARKDOWN)
        bot.sendMessage(chat_id = ADMINGROUP, text = message, parse_mode=telegram.ParseMode.MARKDOWN)