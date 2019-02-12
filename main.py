# -*- coding: utf-8 -*-
from functions import *

bot = telegram.Bot(TOKEN)

def main():
	updater = Updater(TOKEN, request_kwargs={'read_timeout': 20, 'connect_timeout': 20})
	dp = updater.dispatcher

	dp.add_handler(CommandHandler('info', info_cmd))
	dp.add_handler(CommandHandler('reboot', reboot_cmd))
	
	#JobQueue
	j = updater.job_queue

	j.run_repeating(alert_cmd, interval= 30, first= 0)
	

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()
