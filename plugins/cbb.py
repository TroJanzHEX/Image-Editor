# By @TroJanzHEX
import pyrogram
from image.edit_1 import bright,mix,black_white,g_blur,normal_blur,box_blur
from image.edit_2 import circle, sticker, edge_curved, contrast,sepia_mode,pencil,cartoon
from image.edit_3 import green_border,blue_border,black_border,red_border
from image.edit_4 import rotate_90,rotate_180,rotate_270
from pyrogram import Client 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from script import script

@Client.on_callback_query()
async def cb_handler(client, query):

    if "bright" in query.data:
        await query.message.delete()
        await bright(client, query.message) 
    
    elif "mix" in query.data:
        await query.message.delete()
        await mix(client, query.message)
  
    elif "b|w" in query.data:
        await query.message.delete()
        await black_white(client, query.message)

    elif "circle" in query.data:
        await query.message.delete()
        await circle(client, query.message)
   
    elif "blur" in query.data:
        await query.message.edit("**Select a Type**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="box",callback_data="box"),InlineKeyboardButton(text="normal",callback_data="normal")],[InlineKeyboardButton(text="Gaussian",callback_data="gas")]]))

    elif "border" in query.data:
        await query.message.edit("**Select Border**",reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="🔴 RED 🔴", callback_data = "red"), InlineKeyboardButton(text="🟢 Green 🟢", callback_data = "green")],
                                                    [InlineKeyboardButton(text="⚫ Black ⚫", callback_data="black"), InlineKeyboardButton(text="🔵 Blue 🔵",callback_data = "blue")]]))     
    elif "green" in query.data:
        await query.message.delete()
        await green_border(client, query.message)

    elif "blue" in query.data:
        await query.message.delete()
        await blue_border(client, query.message)

    elif "red" in query.data:
        await query.message.delete()
        await red_border(client, query.message)

    elif "black" in query.data:
        await query.message.delete()
        await black_border(client, query.message)
   
    elif "stick" in query.data:
        await query.message.edit("**Select a Type**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Normal",callback_data="stkr"),InlineKeyboardButton(text="Edge Curved",callback_data="cur_ved")]]))

    elif "stkr" in query.data:
        await query.message.delete()
        await sticker(client, query.message)

    elif "cur_ved" in query.data:
        await query.message.delete()
        await edge_curved(client, query.message)

    elif "rotate" in query.data:
        await query.message.edit_text("**Select the Degree**",reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="180", callback_data = "180"), InlineKeyboardButton(text="90", callback_data = "90")],
                            [InlineKeyboardButton(text="270", callback_data="270")]]))

    elif "90" in query.data:
         await query.message.delete()
         await rotate_90(client, query.message)

    elif "180" in query.data:
        await query.message.delete()
        await rotate_180(client, query.message)

    elif "270" in query.data:
        await query.message.delete()
        await rotate_270(client, query.message)

    elif "contrast" in query.data:
        await query.message.delete()
        await contrast(client, query.message)

    elif "close_e" in query.data:
        await query.message.delete()
    
    elif "box" in query.data:
        await query.message.delete()
        await box_blur(client, query.message)

    elif "gas" in query.data:
        await query.message.delete()
        await g_blur(client, query.message)

    elif "normal" in query.data:
        await query.message.delete()
        await normal_blur(client, query.message)

    elif "sepia" in query.data:
        await query.message.delete()
        await sepia_mode(client,query.message)

    elif "pencil" in query.data:
        await query.message.delete()
        await pencil(client,query.message)

    elif "cartoon" in query.data:
        await query.message.delete()
        await cartoon(client,query.message)

    elif  "start_data" in query.data:

        keyboard=InlineKeyboardMarkup([[InlineKeyboardButton("HELP", callback_data="help_data"),InlineKeyboardButton("ABOUT", callback_data="about_data"),],
                                       [InlineKeyboardButton("SOURCE CODE", url="https://github.com/TroJanzHEX/Image-Editor")]])

        await query.message.edit_text(script.START_MSG.format(query.from_user.mention), reply_markup=keyboard, disable_web_page_preview=True)  

   
    elif "help_data" in query.data:

        keyboard=InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="start_data"),InlineKeyboardButton("ABOUT", callback_data="about_data"),],
                                       [InlineKeyboardButton("SOURCE CODE", url="https://github.com/TroJanzHEX/Image-Editor")]])

        await query.message.edit_text(script.HELP_MSG, reply_markup=keyboard, disable_web_page_preview=True)  
        

    elif "about_data" in query.data:

        keyboard=InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="help_data"),InlineKeyboardButton("START", callback_data="start_data"),],
                                       [InlineKeyboardButton("SOURCE CODE", url="https://github.com/TroJanzHEX/Image-Editor")]])

        await query.message.edit_text(script.ABOUT_MSG, reply_markup=keyboard, disable_web_page_preview=True)  
       
    
