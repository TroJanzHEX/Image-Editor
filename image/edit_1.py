# By @TroJanzHEX
import pyrogram
from PIL import Image,ImageEnhance,ImageFilter



async def bright(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    image = Image.open(a)
    brightness=ImageEnhance.Brightness(image)
    brightness.enhance(1.5).save('brightness.jpg')
    await msg.delete()
    await message.reply_chat_action("upload_photo")
    await message.reply_photo("brightness.jpg")

      
async def mix(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text(downloading)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    image = Image.open(a)
    red, green, blue = image.split()
    new_image = Image.merge("RGB", (green, red, blue))
    new_image.save('mix.jpg')
    await msg.delete()
    await message.reply_chat_action("upload_photo")
    await message.reply_photo("mix.jpg")

async def black_white(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    image_file = Image.open(a)
    image_file = image_file.convert('1') 
    image_file.save('black_white.jpg')
    await msg.delete()
    await message.reply_chat_action("upload_photo")
   
    await message.reply_photo("black_white.jpg")
    
async def normal_blur(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    OriImage = Image.open(a)
    blurImage = OriImage.filter(ImageFilter.BLUR)
    blurImage.save('BlurImage.jpg')
    await msg.delete()
    await message.reply_chat_action("upload_photo")
   
    await message.reply_photo("BlurImage.jpg")

async def g_blur(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    im1 = Image.open(a)
    im2 = im1.filter(ImageFilter.GaussianBlur(radius = 5)) 
    im2.save("gaussian_blur.jpg")
    await msg.delete()
    await message.reply_chat_action("upload_photo")
   
    await message.reply_photo("gaussian_blur.jpg")

async def box_blur(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_text("downloading")
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("processing")
    im1 = Image.open(a)
    im2 = im1.filter(ImageFilter.BoxBlur(0))
    im2.save("box_blur.jpg")
    await msg.delete()
    
    await message.reply_chat_action("upload_photo")
   
    await message.reply_photo("box_blur.jpg")
