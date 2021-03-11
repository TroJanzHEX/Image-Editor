# By @TroJanzHEX
import os
import time
import math 
from script import script  # pylint:disable=import-error
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message 
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


@Client.on_message(filters.photo & filters.private)
async def photo(bot, update):
    if Config.UPDATE_CHANNEL:
        try:
          user = await bot.get_chat_member(Config.UPDATE_CHANNEL, update.chat.id)
          if user.status == "kicked":
            await update.reply_text(text=script.BANNED_USER_TEXT)
            return
        except UserNotParticipant:
          await update.reply_text(text=script.FORCE_SUBSCRIBE_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="😎 Join Channel 😎", url=f"https://telegram.me/{Config.UPDATE_CHANNEL}")]]))
          return
        except Exception:
          await update.reply_text(text=script.SOMETHING_WRONG)
          return
    if update.from_user.id not in Config.AUTH_USERS:
        if str(update.from_user.id) in Config.ADL_BOT_RQ:
            current_time = time.time()
            previous_time = Config.ADL_BOT_RQ[str(update.from_user.id)]
            process_max_timeout = round(Config.PROCESS_MAX_TIMEOUT/60)
            present_time = round(Config.PROCESS_MAX_TIMEOUT-(current_time - previous_time))
            Config.ADL_BOT_RQ[str(update.from_user.id)] = time.time()
            if round(current_time - previous_time) < Config.PROCESS_MAX_TIMEOUT:
                await bot.send_message(text=script.FREE_USER_LIMIT.format(process_max_timeout, present_time), quote=True)
                return
        else:
            Config.ADL_BOT_RQ[str(update.from_user.id)] = time.time()
    try:
        await bot.send_message(
            chat_id=update.chat.id,
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
                        InlineKeyboardButton(text="CLOSE", callback_data="close"),
                    ],
                ]
            ),
            reply_to_message_id=update.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text(script.SOMETHING_WRONG, quote=True)
            except Exception:
                return
