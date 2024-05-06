from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os


bot = Client("bot",
             bot_token= os.environ.get("BOT_TOKEN", ""), 
             api_id= int(os.environ.get("APP_ID", 12345)), #api
             api_hash= os.environ.get("API_HASH"))


keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/ITS_NOT_ROMEO",
            ),
            InlineKeyboardButton(
                text="❣️ GITHUB",
                url="https://github.com/Devansh20055",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🪄 Main Channel",
                url="https://t.me/TEAM_SILENT_KING_OG",
            ),
            
        ],
    ]
)


@bot.on_message(filters.command(["start"]))
async def STRT(bot: Client, m: Message):
    editable = await m.reply_text(f"**➠ HI ! I AM ADDITION BOT  **",reply_markup=keyboard)
     
@bot.on_message(filters.command(["add"]))
async def add(bot: Client, m: Message):
    editable = await m.reply_text(f"**➠ SEND 1ST NO TO ADD **")
    input: Message = await bot.listen(editable.chat.id)
    raw_text0 = input.text
    editable = await m.reply_text(f"**➠ SEND 2ND NUMBER **")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1 = input1.text
    ADDIND = int(raw_text0)+int(raw_text1)
    #ADDIND = raw_text0+raw_text1
    await m.reply_text(f"**Addition is : {ADDIND} \n BOT BY @ITS _NOT _ROMEO ON TG **")
     
bot.run()
