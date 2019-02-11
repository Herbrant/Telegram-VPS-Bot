# -*- coding: utf-8 -*-
from functions import *

bot = telegram.Bot(TOKEN)

def main():
	updater = Updater(TOKEN, request_kwargs={'read_timeout': 20, 'connect_timeout': 20})
	dp = updater.dispatcher

	dp.add_handler(CommandHandler('cpu', cpu_cmd))

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()
