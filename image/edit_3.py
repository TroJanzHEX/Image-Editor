# By @TroJanzHEX
from PIL import Image, ImageOps
import shutil
import os
from googletrans import Translator
from config import Config


async def black_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-black-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                Translator().translate("Downloading image", dest=Config.LANG).text, quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit(Translator().translate("Processing Image...", dest=Config.LANG).text)
            img = Image.open(a)
            img_with_border = ImageOps.expand(img, border=100, fill="black")
            img_with_border.save(edit_img_loc)

            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text(Translator().translate("Why did you delete that??", dest=Config.LANG).text)
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("black_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    Translator().translate("Something went wrong!", dest=Config.LANG).text, quote=True
                )
            except Exception:
                return


async def green_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-green-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                Translator().translate("Downloading image", dest=Config.LANG).text, quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit(Translator().translate("Processing Image...", dest=Config.LANG).text)
            img = Image.open(a)
            img_with_border = ImageOps.expand(img, border=100, fill="green")
            img_with_border.save(edit_img_loc)

            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text(Translator().translate("Why did you delete that??", dest=Config.LANG).text)
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("green_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    Translator().translate("Something went wrong!", dest=Config.LANG).text, quote=True
                )
            except Exception:
                return


async def blue_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-blue-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                Translator().translate("Downloading image", dest=Config.LANG).text, quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit(Translator().translate("Processing Image...", dest=Config.LANG).text)
            img = Image.open(a)
            img_with_border = ImageOps.expand(img, border=100, fill="blue")
            img_with_border.save(edit_img_loc)

            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text(Translator().translate("Why did you delete that??", dest=Config.LANG).text)
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("blue_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    Translator().translate("Something went wrong!", dest=Config.LANG).text, quote=True
                )
            except Exception:
                return


async def red_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-red-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                Translator().translate("Downloading image", dest=Config.LANG).text, quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit(Translator().translate("Processing Image...", dest=Config.LANG).text)
            img = Image.open(a)
            img_with_border = ImageOps.expand(img, border=100, fill="red")
            img_with_border.save(edit_img_loc)

            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text(Translator().translate("Why did you delete that??", dest=Config.LANG).text)
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("red_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    Translator().translate("Something went wrong!", dest=Config.LANG).text, quote=True
                )
            except Exception:
                return
