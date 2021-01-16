# By @TroJanzHEX
import pyrogram
from PIL import Image,ImageOps


async def black_border(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    img = Image.open(a)
    img_with_border = ImageOps.expand(img,border=100,fill= 'black')
    img_with_border.save('imaged-black-border.png')
    await msg.delete()
    await message.reply_chat_action("upload_photo")
  
    await message.reply_photo("imaged-black-border.png")

async def green_border(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    img = Image.open(a)
    img_with_border = ImageOps.expand(img,border=100,fill= 'green')
    img_with_border.save('imaged-green-border.png')
    await msg.delete()
    await message.reply_chat_action("upload_photo")
  
    await message.reply_photo("imaged-green-border.png")

async def blue_border(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    img = Image.open(a)
    img_with_border = ImageOps.expand(img,border=100,fill= 'blue')
    img_with_border.save('imaged-blue-border.png')
    await msg.delete()
    await message.reply_chat_action("upload_photo")
    await message.reply_photo("imaged-blue-border.png")

async def red_border(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    img = Image.open(a)
    img_with_border = ImageOps.expand(img,border=100,fill= 'red')
    img_with_border.save('imaged-red-border.png')
    await msg.delete()
    await message.reply_chat_action("upload_photo")
    await message.reply_photo("imaged-red-border.png")

