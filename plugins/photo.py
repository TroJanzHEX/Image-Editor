# By @TroJanzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters


@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Select your required mode from below!ㅤㅤ",
            reply_markup=BUTTONS,
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
