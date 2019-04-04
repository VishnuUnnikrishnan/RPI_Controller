'''
    Telegram Bot to generate telegram notifications. Acts as a psuedo
    sms and email service with gauranteed delivery as long as both the
    sender and recipient have internet access.
'''

import telegram
import json
import os

MODULE_NAME = "modules/telegram"
USERNAME = "username"
TOKEN = "api_key"

def returnBot():
    with open("settings/settings.json","r") as f:
        os.chdir('..')
        data = json.load(f)
        token = data[MODULE_NAME][TOKEN]
        bot = telegram.Bot(token=token)
        print(bot.get_me())

if __name__ == "__main__":
    returnBot()