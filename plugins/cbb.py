# By @TroJanzHEX

import pyrogram
from image.edit_1 import bright, mix, black_white, g_blur, normal_blur, box_blur
from image.edit_2 import circle_with_bg, circle_without_bg, sticker, edge_curved, contrast, sepia_mode, pencil, cartoon
from image.edit_3 import green_border, blue_border, black_border, red_border
from image.edit_4 import rotate_90, rotate_180, rotate_270, inverted, round_sticker, removebg_white, removebg_plain, removebg_sticker
from image.edit_5 import (
    normalglitch_1,
    normalglitch_2,
    normalglitch_3,
    normalglitch_4,
    normalglitch_5,
    scanlineglitch_1,
    scanlineglitch_2,
    scanlineglitch_3,
    scanlineglitch_4,
    scanlineglitch_5
)

from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from script import script


@Client.on_callback_query()
async def cb_handler(client, query):

    if query.data == "bright":
        await query.message.delete()
        await bright(client, query.message)

    elif query.data == "mix":
        await query.message.delete()
        await mix(client, query.message)

    elif query.data == "b|w":
        await query.message.delete()
        await black_white(client, query.message)

    elif query.data == "circle":
        await query.message.edit_text(
            "**Select required mode**",
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text="WITH BG", callback_data ="circlewithbg"),
                    InlineKeyboardButton(text="WITHOUT BG", callback_data ="circlewithoutbg")]
            ])
        )

    elif query.data == "circlewithbg":
        await query.message.delete()
        await circle_with_bg(client, query.message)

    elif query.data == "circlewithoutbg":
        await query.message.delete()
        await circle_without_bg(client, query.message)

    elif query.data == "blur":
        await query.message.edit("**Select a Type**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="box", callback_data="box"), InlineKeyboardButton(text="normal", callback_data="normal")], [InlineKeyboardButton(text="Gaussian", callback_data="gas")]]))

    elif query.data == "border":
        await query.message.edit("**Select Border**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="🔴 RED 🔴", callback_data="red"), InlineKeyboardButton(text="🟢 Green 🟢", callback_data="green")],
                                                                                         [InlineKeyboardButton(text="⚫ Black ⚫", callback_data="black"), InlineKeyboardButton(text="🔵 Blue 🔵", callback_data="blue")]]))
    elif query.data == "green":
        await query.message.delete()
        await green_border(client, query.message)

    elif query.data == "blue":
        await query.message.delete()
        await blue_border(client, query.message)

    elif query.data == "red":
        await query.message.delete()
        await red_border(client, query.message)

    elif query.data == "black":
        await query.message.delete()
        await black_border(client, query.message)

    elif query.data == "stick":
        await query.message.edit("**Select a Type**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Normal", callback_data="stkr"), InlineKeyboardButton(text="Edge Curved", callback_data="cur_ved")],
                                                                                         [InlineKeyboardButton(text="Circle", callback_data="circle_sticker")]]))

    elif query.data == "circle_sticker":
        await query.message.delete()
        await round_sticker(client, query.message)

    elif query.data == "inverted":
        await query.message.delete()
        await inverted(client, query.message)

    elif query.data == "stkr":
        await query.message.delete()
        await sticker(client, query.message)

    elif query.data == "cur_ved":
        await query.message.delete()
        await edge_curved(client, query.message)

    elif query.data == "rotate":
        await query.message.edit_text("**Select the Degree**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="180", callback_data="180"), InlineKeyboardButton(text="90", callback_data="90")],
                                                                                                  [InlineKeyboardButton(text="270", callback_data="270")]]))

    elif query.data == "90":
        await query.message.delete()
        await rotate_90(client, query.message)

    elif query.data == "180":
        await query.message.delete()
        await rotate_180(client, query.message)

    elif query.data == "270":
        await query.message.delete()
        await rotate_270(client, query.message)

    elif query.data == "contrast":
        await query.message.delete()
        await contrast(client, query.message)

    elif query.data == "close_e":
        await query.message.delete()

    elif query.data == "box":
        await query.message.delete()
        await box_blur(client, query.message)

    elif query.data == "gas":
        await query.message.delete()
        await g_blur(client, query.message)

    elif query.data == "normal":
        await query.message.delete()
        await normal_blur(client, query.message)

    elif query.data == "sepia":
        await query.message.delete()
        await sepia_mode(client, query.message)

    elif query.data == "pencil":
        await query.message.delete()
        await pencil(client, query.message)

    elif query.data == "cartoon":
        await query.message.delete()
        await cartoon(client, query.message)

        
    elif query.data == "glitch":
        await query.message.edit_text(
            "**Select required mode**ㅤㅤㅤㅤ",
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text="NORMAL", callback_data ="normalglitch"),
                    InlineKeyboardButton(text="SCAN LINES", callback_data ="scanlineglitch")]
            ])
        )

    elif query.data == "normalglitch":
        await query.message.edit_text(
            "**Select Glitch power level**",
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text="1", callback_data ="normalglitch1"),
                    InlineKeyboardButton(text="2", callback_data ="normalglitch2"),
                        InlineKeyboardButton(text="3", callback_data ="normalglitch3")],
                [InlineKeyboardButton(text="4", callback_data ="normalglitch4"),
                    InlineKeyboardButton(text="5", callback_data ="normalglitch5")]
            ])
        )
        
    elif query.data == "scanlineglitch":
        await query.message.edit_text(
            "**Select Glitch power level**",
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text="1", callback_data ="scanlineglitch1"),
                    InlineKeyboardButton(text="2", callback_data ="scanlineglitch2"),
                        InlineKeyboardButton(text="3", callback_data ="scanlineglitch3")],
                [InlineKeyboardButton(text="4", callback_data ="scanlineglitch4"),
                    InlineKeyboardButton(text="5", callback_data ="scanlineglitch5")]
            ])
        )

    elif query.data == "normalglitch1":
        await query.message.delete()
        await normalglitch_1(client, query.message)

    elif query.data == "normalglitch2":
        await query.message.delete()
        await normalglitch_2(client, query.message)

    elif query.data == "normalglitch3":
        await query.message.delete()
        await normalglitch_3(client, query.message)

    elif query.data == "normalglitch4":
        await query.message.delete()
        await normalglitch_4(client, query.message)

    elif query.data == "normalglitch5":
        await query.message.delete()
        await normalglitch_5(client, query.message)
        
        
    elif query.data == "scanlineglitch1":
        await query.message.delete()
        await scanlineglitch_1(client, query.message)

    elif query.data == "scanlineglitch2":
        await query.message.delete()
        await scanlineglitch_2(client, query.message)

    elif query.data == "scanlineglitch3":
        await query.message.delete()
        await scanlineglitch_3(client, query.message)

    elif query.data == "scanlineglitch4":
        await query.message.delete()
        await scanlineglitch_4(client, query.message)

    elif query.data == "scanlineglitch5":
        await query.message.delete()
        await scanlineglitch_5(client, query.message) 


   
    elif query.data == "removebg":
        await query.message.edit_text(
            "**Select required mode**ㅤㅤㅤㅤ",
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text="WITH WHITE BG", callback_data ="rmbgwhite"),
                    InlineKeyboardButton(text="WITHOUT BG", callback_data ="rmbgplain")],
                [InlineKeyboardButton(text="STICKER", callback_data ="rmbgsticker")]
            ])
        )      
        
    elif query.data == "rmbgwhite":
        await query.message.delete()
        await removebg_white(client, query.message)

    elif query.data == "rmbgplain":
        await query.message.delete()
        await removebg_plain(client, query.message)

    elif query.data == "rmbgsticker":
        await query.message.delete()
        await removebg_sticker(client, query.message)


    elif query.data == "start_data":

        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("HELP", callback_data="help_data"), InlineKeyboardButton("ABOUT", callback_data="about_data"), ],
                                         [InlineKeyboardButton("SOURCE CODE", url="https://github.com/TroJanzHEX/Image-Editor")]])

        await query.message.edit_text(script.START_MSG.format(query.from_user.mention), reply_markup=keyboard, disable_web_page_preview=True)

    elif query.data == "help_data":

        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="start_data"), InlineKeyboardButton("ABOUT", callback_data="about_data"), ],
                                         [InlineKeyboardButton("SOURCE CODE", url="https://github.com/TroJanzHEX/Image-Editor")]])

        await query.message.edit_text(script.HELP_MSG, reply_markup=keyboard, disable_web_page_preview=True)

    elif query.data == "about_data":

        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="help_data"), InlineKeyboardButton("START", callback_data="start_data"), ],
                                         [InlineKeyboardButton("SOURCE CODE", url="https://github.com/TroJanzHEX/Image-Editor")]])

        await query.message.edit_text(script.ABOUT_MSG, reply_markup=keyboard, disable_web_page_preview=True)
