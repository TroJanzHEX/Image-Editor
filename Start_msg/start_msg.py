fsub_text = """
* 🌹Massege For You 🌹 *
You see this message because you are not subscribed to the channel:
@{UPDATED_CHANNEL}
Hey Join Our Channel And You Can Use Me."""


async def get_user(message):
    ok = True
    try:
        await message._client.get_chat_member({UPDATED_CHANNEL_ID}, message.from_user.id)
        ok = True
    except UserNotParticipant:
        ok = False
    return ok 

@app.on_message(filters.command("start"))
async def start(_, message: Message):
    if not await get_user(message):   
        return await app.send_message(
			chat_id=message.from_user.id,
			text=fsub_text) 
    name = message.from_user.id
    await app.send_message(
    name,
    text = start_text.format(message.from_user.mention),
    reply_markup = start_button)
    return await add_served_user(message.from_user.id) 
    
#****************************
API1='https://www.1secmail.com/api/v1/?action=getDomainList'
API2='https://www.1secmail.com/api/v1/?action=getMessages&login='
API3='https://www.1secmail.com/api/v1/?action=readMessage&login='
#****************************
create = InlineKeyboardMarkup(
            [[InlineKeyboardButton(" 💙 {CHANNEL_NAME}  💙", url="https://t.me/{UPDATED_CHANNEL_USERNAME}")]])
