from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import Message

bot = Client("bot",
             bot_token= "your _bot token", 
             api_id= , #api
             api_hash= "harsh")

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
