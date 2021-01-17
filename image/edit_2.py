# By @TroJanzHEX

import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image,ImageEnhance,ImageDraw,ImageFilter,ImageOps
import numpy as np
import os
import cv2

async def circle(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    img=Image.open(a).convert("RGB")
    npImage = np.array(img)
    h,w = img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage,npAlpha))
    Image.fromarray(npImage).save('circle.png')
    await msg.delete()
    await message.reply_chat_action("upload_photo")
    await message.reply_to_message.reply_photo("circle.png", quote=True)



async def sticker(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    os.rename(a,"sticker.webp")
    await msg.delete()
    await  message.reply_to_message.reply_sticker("sticker.webp", quote=True)


async def contrast(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    image=Image.open(a)
    contrast=ImageEnhance.Contrast(image)
    contrast.enhance(1.5).save('contrast.jpg')
    await msg.delete()
    
    await message.reply_chat_action("upload_photo")
  
    await message.reply_to_message.reply_photo("contrast.jpg", quote=True)



def sepia(img):
    width, height = img.size
    new_img = img.copy()
    for x in range(width):
        for y in range(height):
            red, green, blue = img.getpixel((x,y))
            new_val = (0.3 * red + 0.59 * green + 0.11 * blue)
            new_red = int(new_val * 2)
            if new_red > 255:
                new_red = 255
            new_green = int(new_val * 1.5)
            if new_green > 255:
                new_green = 255
            new_blue = int(new_val)
            if new_blue > 255:
                new_blue = 255

            new_img.putpixel((x,y), (new_red, new_green, new_blue))

    return new_img

async def sepia_mode(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    image=Image.open(a)
    new_img = sepia(image)
    new_img.save("sepia.jpg")
    await msg.delete()
    await message.reply_chat_action("upload_photo")
    await message.reply_to_message.reply_photo("sepia.jpg", quote=True)


def dodgeV2(x, y):
       return cv2.divide(x, 255 - y, scale=256)


async def pencil(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    img = cv2.imread(a)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    cv2.imwrite("pencil.jpg", final_img)
    await msg.delete()
    await message.reply_chat_action("upload_photo")
    await message.reply_to_message.reply_photo("pencil.jpg", quote=True)





def color_quantization(img, k):
        data = np.float32(img).reshape((-1, 3))
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
        ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        result = center[label.flatten()]
        result = result.reshape(img.shape)
        return result


async def cartoon(client, message):
    media = message
    download_location = "./DOWNLOADS" + "/" + str(message.from_user.id) + ".jpg"
    msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
    a  =   await client.download_media(
           message=media.reply_to_message,
           file_name=download_location
        )
    await msg.edit("Processing Image...")
    img = cv2.imread(a)
    edges = cv2.Canny(img, 100, 200)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
    color = cv2.bilateralFilter(img, d=9, sigmaColor=200,sigmaSpace=200)
   
    cartoon = cv2.bitwise_and(color, color, mask=edges) 
    img_1 = color_quantization(img, 7)
    cv2.imwrite("kang.jpg",img_1)
    await msg.delete()
    await message.reply_chat_action("upload_photo")
    await message.reply_to_message.reply_photo("kang.jpg", quote=True)
