# By @TroJanzHEX
import pyrogram
import cv2


async def rotate_90(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    src=cv2.imread(a)
    image = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE) 
    cv2.imwrite("rotate_90.jpg",image)
    await msg.delete()
    await message.reply_chat_action("upload_photo")
    await message.reply_photo("rotate_90.jpg")

async def rotate_180(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    src=cv2.imread(a)
    image = cv2.rotate(src, cv2.ROTATE_180) 
    cv2.imwrite("rotate_180.jpg",image)
    await msg.delete()
    await message.reply_chat_action("upload_photo")
    await message.reply_photo("rotate_180.jpg")

async def rotate_270(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    src = cv2.imread(a)
    image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE) 
    cv2.imwrite("rotate_270.jpg",image)
    await msg.delete()
    await message.reply_chat_action("upload_photo")
  
    await message.reply_photo("rotate_270.jpg")
