from pyrogram.types import InlineKeyboardButton

class Button(object):

    START_BUTTONS = [[InlineKeyboardButton('⚙ Channel ⚙', url='https://telegram.me/FayasNoushad'), InlineKeyboardButton('⚙ Group ⚙', url='https://telegram.me/FayasChat'),],
                        [InlineKeyboardButton('⚜ Help and Informations ⚜', callback_data='help')]]

    HELP_BUTTONS = [[InlineKeyboardButton('⚙ Channel ⚙', url='https://telegram.me/FayasNoushad'), InlineKeyboardButton('⚙ Group ⚙', url='https://telegram.me/FayasChat'),],
                        [InlineKeyboardButton('⚜ Back to Home ⚜', callback_data='home')]]
