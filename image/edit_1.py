# By @TroJanzHEX
from PIL import Image, ImageEnhance, ImageFilter
import shutil
import cv2
import os
from googletrans import Translator
from config import Config
from bs4 import BeautifulSoup

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

async def bright(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "brightness.jpg"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                Translator().translate("Downloading image", dest=Config.LANG).text, quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit(Translator().translate("Processing Image...", dest=Config.LANG).text)
            image = Image.open(a)
            brightness = ImageEnhance.Brightness(image)
            brightness.enhance(1.5).save(edit_img_loc)

            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text(Translator().translate("Why did you delete that??", dest=Config.LANG).text)
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("bright-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    Translator().translate("Something went wrong!", dest=Config.LANG).text, quote=True
                )
            except Exception:
                return


async def mix(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "mix.jpg"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                Translator().translate("Downloading image", dest=Config.LANG).text, quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit(Translator().translate("Processing Image...", dest=Config.LANG).text)
            image = Image.open(a)
            red, green, blue = image.split()
            new_image = Image.merge("RGB", (green, red, blue))
            new_image.save(edit_img_loc)

            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text(Translator().translate("Why did you delete that??", dest=Config.LANG).text)
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("mix-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    Translator().translate("Something went wrong!", dest=Config.LANG).text, quote=True
                )
            except Exception:
                return


async def black_white(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "black_white.jpg"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                Translator().translate("Downloading image", dest=Config.LANG).text, quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit(Translator().translate("Processing Image...", dest=Config.LANG).text)
            image_file = cv2.imread(a)
            grayImage = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(edit_img_loc, grayImage)

            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text(Translator().translate("Why did you delete that??", dest=Config.LANG).text)
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("black_white-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    Translator().translate("Something went wrong!", dest=Config.LANG).text, quote=True
                )
            except Exception:
                return


async def normal_blur(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "BlurImage.jpg"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                Translator().translate("Downloading image", dest=Config.LANG).text, quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit(Translator().translate("Processing Image...", dest=Config.LANG).text)
            OriImage = Image.open(a)
            blurImage = OriImage.filter(ImageFilter.BLUR)
            blurImage.save(edit_img_loc)

            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text(Translator().translate("Why did you delete that??", dest=Config.LANG).text)
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("normal_blur-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    Translator().translate("Something went wrong!", dest=Config.LANG).text, quote=True
                )
            except Exception:
                return


async def g_blur(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "gaussian_blur.jpg"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                Translator().translate("Downloading image", dest=Config.LANG).text, quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit(Translator().translate("Processing Image...", dest=Config.LANG).text)
            im1 = Image.open(a)
            im2 = im1.filter(ImageFilter.GaussianBlur(radius=5))
            im2.save(edit_img_loc)

            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text(Translator().translate("Why did you delete that??", dest=Config.LANG).text)
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("g_blur-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    Translator().translate("Something went wrong!", dest=Config.LANG).text, quote=True
                )
            except Exception:
                return


async def box_blur(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "box_blur.jpg"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                Translator().translate("Downloading image", dest=Config.LANG).text, quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit(Translator().translate("Processing Image...", dest=Config.LANG).text)
            im1 = Image.open(a)
            im2 = im1.filter(ImageFilter.BoxBlur(0))
            im2.save(edit_img_loc)

            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text(Translator().translate("Why did you delete that??", dest=Config.LANG).text)
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("box_blur-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    Translator().translate("Something went wrong!", dest=Config.LANG).text, quote=True
                )
            except Exception:
                return


async def add_cover(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./downloads/{userid}"):
            os.makedirs(f"./downloads/{userid}")
        download_location = "./downloads" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./downloads" + "/" + userid + "/" + "add_cover.jpg"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                Translator().translate("Downloading image", dest=Config.LANG).text, quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            im1 = Image.open(a)
            width, height = im1.size
            sq_fit_size = height
            im1 = crop_center(im1, sq_fit_size, sq_fit_size)
            mycaption = message.reply_to_message.caption

            logoIm = Image.open("logo/cover.png")

            logoWidth, logoHeight = logoIm.size

            width = sq_fit_size
            height = sq_fit_size
            logoIm = logoIm.resize((width, height))
            logoWidth, logoHeight = logoIm.size

            im1.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

            im1.save(os.path.join(edit_img_loc))

            await message.reply_to_message.reply_photo(edit_img_loc, caption="", quote=True)
            await msg.delete()
        else:
            await message.reply_text(Translator().translate("Why did you delete that??", dest=Config.LANG).text)
        try:
            shutil.rmtree(f"./downloads/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("add_cover-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    Translator().translate("Something went wrong!", dest=Config.LANG).text, quote=True
                )
            except Exception:
                return