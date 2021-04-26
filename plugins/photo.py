# By @TroJanzHEX
import os
import time
import math
from script import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    if message.from_user.id not in Config.AUTH_USERS:
        if str(message.from_user.id) in Config.ADL_BOT_RQ:
            current_time = time.time()
            previous_time = Config.ADL_BOT_RQ[str(message.from_user.id)]
            process_max_timeout = round(Config.PROCESS_MAX_TIMEOUT/60)
            present_time = round(Config.PROCESS_MAX_TIMEOUT-(current_time - previous_time))
            Config.ADL_BOT_RQ[str(message.from_user.id)] = time.time()
            if round(current_time - previous_time) < Config.PROCESS_MAX_TIMEOUT:
                await client.send_message(text=script.FREE_USER_LIMIT.format(process_max_timeout, present_time), quote=True)
                return
        else:
            Config.ADL_BOT_RQ[str(message.from_user.id)] = time.time()
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Select your required mode from below!ㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="BRIGHT", callback_data="bright"),
                        InlineKeyboardButton(text="MIXED", callback_data="mix"),
                        InlineKeyboardButton(text="B&W", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="CIRCLE", callback_data="circle"),
                        InlineKeyboardButton(text="BLUR", callback_data="blur"),
                        InlineKeyboardButton(text="BORDER", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="STICKER", callback_data="stick"),
                        InlineKeyboardButton(text="ROTATE", callback_data="rotate"),
                        InlineKeyboardButton(text="CONTRAST", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="SEPIA", callback_data="sepia"),
                        InlineKeyboardButton(text="PENCIL", callback_data="pencil"),
                        InlineKeyboardButton(text="CARTOON", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="INVERT", callback_data="inverted"),
                        InlineKeyboardButton(text="GLITCH", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="REMOVE BG", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="CLOSE", callback_data="close_e"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return
