# By @TroJanzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from script import script  # pylint:disable=import-error


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    try:
        await client.send_message(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🔰 HELP 🔰', callback_data='help'), InlineKeyboardButton('🔰 ABOUT 🔰', callback_data='about')]]),
            reply_to_message_id=update.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(bot, update):
    try:
        await bot.send_message(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🔰 HOME 🔰', callback_data='home'), InlineKeyboardButton('🔰 ABOUT 🔰', callback_data='about')]]),
            reply_to_message_id=update.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["about"]) & filters.private)
async def about(bot, update):
    try:
        await bot.send_message(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🔰 HELP 🔰', callback_data='help'), InlineKeyboardButton('🔰 HOME 🔰', callback_data='home')]]),
            reply_to_message_id=update.message_id,
        )
    except Exception:
        pass
