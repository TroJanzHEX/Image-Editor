# By @TroJanzHEX

import pyrogram
import shutil
import cv2
import os


async def rotate_90(client, message):
    userid = str(message.from_user.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.mkdir(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "rotate_90.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        src=cv2.imread(a)
        image = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE) 
        cv2.imwrite(edit_img_loc,image)
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        
        
async def rotate_180(client, message):
    userid = str(message.from_user.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.mkdir(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "rotate_180.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        src=cv2.imread(a)
        image = cv2.rotate(src, cv2.ROTATE_180) 
        cv2.imwrite(edit_img_loc,image)
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        
        
async def rotate_270(client, message):
    userid = str(message.from_user.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.mkdir(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "rotate_270.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        src = cv2.imread(a)
        image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE) 
        cv2.imwrite(edit_img_loc,image)
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        
