# By @TroJanzHEX
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from buttons import Button 
from script import script  # pylint:disable=import-error

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await bot.send_message(chat_id=update.chat.id, text=script.START_MSG.format(update.from_user.mention), parse_mode="html", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(Button.START_BUTTONS), reply_to_message_id=update.message_id)
