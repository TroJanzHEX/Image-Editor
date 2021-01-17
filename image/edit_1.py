# By @TroJanzHEX

import pyrogram
import shutil
import cv2
import os
from PIL import Image,ImageEnhance,ImageFilter



async def bright(client, message):
    userid = str(message.from_user.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.mkdir(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "brightness.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        image = Image.open(a)
        brightness=ImageEnhance.Brightness(image)
        brightness.enhance(1.5).save(edit_img_loc)
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
      
async def mix(client, message):
    userid = str(message.from_user.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.mkdir(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "mix.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        image = Image.open(a)
        red, green, blue = image.split()
        new_image = Image.merge("RGB", (green, red, blue))
        new_image.save(edit_img_loc)
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()    
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        
        
async def black_white(client, message):
    userid = str(message.from_user.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.mkdir(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "black_white.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        image_file =  cv2.imread(a)
        grayImage = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(edit_img_loc,grayImage)
        await message.reply_chat_action("upload_photo")  
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass

        
async def normal_blur(client, message):
    userid = str(message.from_user.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.mkdir(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "BlurImage.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        OriImage = Image.open(a)
        blurImage = OriImage.filter(ImageFilter.BLUR)
        blurImage.save(edit_img_loc)
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        
        
async def g_blur(client, message):
    userid = str(message.from_user.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.mkdir(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "gaussian_blur.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        im1 = Image.open(a)
        im2 = im1.filter(ImageFilter.GaussianBlur(radius = 5)) 
        im2.save(edit_img_loc)
        await message.reply_chat_action("upload_photo")  
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        
        
async def box_blur(client, message):
    userid = str(message.from_user.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.mkdir(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        im1 = Image.open(a)
        im2 = im1.filter(ImageFilter.BoxBlur(0))
        im2.save(edit_img_loc)
        await message.reply_chat_action("upload_photo") 
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        