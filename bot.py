import time
from pyrogram import Client,filters
bot = Client(session_name='auto',config_file='config.ini')
@bot.on_message(filters.regex('')&filters.private)
async def start(client,message):
    chat_id = message.chat.id
    await bot.send_message(chat_id,"سلام ، این پیام بصورت خودکار توسط ربات برای شما ارسال شده است. لطفا منتظر پاسخگویی باشید.")
bot.run()
    
