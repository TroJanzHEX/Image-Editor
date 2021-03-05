# By @TroJanzHEX


import os


class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # The Telegram API things from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")

    # Get this api from https://www.remove.bg/b/background-removal-api
    REMOVEBG_API = os.environ.get("REMOVEBG_API", "")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")

    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = int(os.environ.get("TIME_LIMIT", ""))
    
    # server info 
    SERVER_DOMAIN = os.environ.get("SERVER_DOMAIN", "")
    SERVER = os.environ.get("SERVER", "")
