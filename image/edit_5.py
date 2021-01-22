# By @TroJanzHEX


import os
import shutil
import asyncio
import pyrogram
import subprocess

import glitch_this


async def normalglitch_1(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "normalglitch_1.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        cd = ["glitch_this", "-c", "-o", edit_img_loc, download_location, "1"]
        process = await asyncio.create_subprocess_exec(*cd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        
        
async def normalglitch_2(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "normalglitch_2.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        cd = ["glitch_this", "-c", "-o", edit_img_loc, download_location, "2"]
        process = await asyncio.create_subprocess_exec(*cd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        
        
async def normalglitch_3(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "normalglitch_3.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        cd = ["glitch_this", "-c", "-o", edit_img_loc, download_location, "3"]
        process = await asyncio.create_subprocess_exec(*cd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass


async def normalglitch_4(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "normalglitch_4.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        cd = ["glitch_this", "-c", "-o", edit_img_loc, download_location, "4"]
        process = await asyncio.create_subprocess_exec(*cd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass


async def normalglitch_5(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "normalglitch_5.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        cd = ["glitch_this", "-c", "-o", edit_img_loc, download_location, "5"]
        process = await asyncio.create_subprocess_exec(*cd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass        
        




async def scanlineglitch_1(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "scanlineglitch_1.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        cd = ["glitch_this", "-c", "-s", "-o", edit_img_loc, download_location, "1"]
        process = await asyncio.create_subprocess_exec(*cd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        
        
async def scanlineglitch_2(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "scanlineglitch_2.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        cd = ["glitch_this", "-c", "-s", "-o", edit_img_loc, download_location, "2"]
        process = await asyncio.create_subprocess_exec(*cd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        

async def scanlineglitch_3(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "scanlineglitch_3.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        cd = ["glitch_this", "-c", "-s", "-o", edit_img_loc, download_location, "3"]
        process = await asyncio.create_subprocess_exec(*cd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass


async def scanlineglitch_4(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "scanlineglitch_4.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        cd = ["glitch_this", "-c", "-s", "-o", edit_img_loc, download_location, "4"]
        process = await asyncio.create_subprocess_exec(*cd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
        
        
async def scanlineglitch_5(client, message):
    userid = str(message.chat.id)
    if not os.path.isdir(f"./DOWNLOADS/{userid}"):
        os.makedirs(f"./DOWNLOADS/{userid}")
    download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
    edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "scanlineglitch_5.jpg"
    if not message.reply_to_message.empty:
        msg = await message.reply_to_message.reply_text("Downloading image", quote=True)
        a  =   await client.download_media(
               message=message.reply_to_message,
               file_name=download_location
            )
        await msg.edit("Processing Image...")
        cd = ["glitch_this", "-c", "-s", "-o", edit_img_loc, download_location, "5"]
        process = await asyncio.create_subprocess_exec(*cd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        await message.reply_chat_action("upload_photo")
        await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
        await msg.delete()
    else:
        await message.reply_text("Why did you delete that??")
    try:
        shutil.rmtree(f"./DOWNLOADS/{userid}")
    except:
        pass
