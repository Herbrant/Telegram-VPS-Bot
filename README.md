# Telegram-VPS-Bot

**Telegram-VPS-Bot** is  a Telegram bot that make easy to control a VPS.


### Setting up a local istance
If you want to test the bot by creating your personal istance, follow this steps:
* **Clone this repository** or download it as zip.
* **Copy config/token.conf.dist into "token.conf" and write your telegram bot token here.** (If you don't have a token, message Telegram's [@BotFather](http://telegram.me/Botfather) to create a bot and get a token for it)
* **Copy config/admin.conf.dist into "admin.conf" and write your telegram admin chatid**
* **Copy config/admingroup.conf.dist int "admingroup.conf" and write your telegram admin group chatid**


### System requirements

- Python 3
- python-pip

#### To install with *pip*

- python-telegram-bot
- psutil

#### How to use

Add the API TOKEN in /config/token.conf
Add the admin chatid in /config/admin.conf
Add the admingroup chatid in /config/admingroup.conf

Run from shell:
```
$ python3 main.py
```

### License
This open-source software is published under the GNU General Public License (GNU GPL) version 3. Please refer to the "LICENSE" file of this project for the full text.
