import time
import random
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

CMD = ["/", "."]

@Client.on_message(filters.private)
async def grp(client, message):
    buttons = [[
          InlineKeyboardButton("🔍 𝖯𝗋𝗈𝖲𝖾𝖺𝗋𝖼𝗁 𝖥𝖺𝗍𝗁𝖾𝗋 🔎", url='http://t.me/ProsearchFatherbot?start=help'),
        ]]
   buttons = [[ InlineKeyboardButton("🔎 Movie Search Group 🥀", url='https://t.me/+t-HcJA8ged9kNjI1'), ]]

    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await message.reply_photo(
        photo="http://graph.org/file/36a684f0c26c766870f7c.jpg",
        caption="<b> ⚠️ Oops!\n\nYou Can't Use Me for Searching Files from Private, I can only Work in Groups Now.\n\nUse @ProSearchFatherBot for Searching Files easily from private chat.\n\n Team @ProSearchFather !</b>",
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=message.id
    )
        
@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
