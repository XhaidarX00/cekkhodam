import ast
from pyrogram import filters
from app import bot, OWNER_ID
from pyrogram.raw.functions import Ping
from datetime import datetime
from app.database import udb

@bot.on_message(filters.user(OWNER_ID) & filters.command("rkey", ""))
async def display_key(client, message):
    chat_id = message.chat.id
    key = message.text.split(None, 1)[1]
    value = udb.read(key)
    if value:
        return await bot.send_message(chat_id, value)
    else:
        return await bot.send_message(chat_id, "Data Tidak Ditemukan!!")


@bot.on_message(filters.user(OWNER_ID) & filters.command("dkey", ""))
async def display_key(client, message):
    chat_id = message.chat.id
    key = message.text.split(None, 1)[1]
    if udb.delete(key):
        return await bot.send_message(chat_id, "Done!!")
    else:
        return await bot.send_message(chat_id, "Data Tidak Ditemukan!!")
    

@bot.on_message(filters.user(OWNER_ID) & filters.command("ukey", ""))
async def display_key(client, message):
    chat_id = message.chat.id
    key = message.text.split(None, 1)[1]
    value = message.text.split(None, 2)[2]
    if udb.update(key, value):
        return await bot.send_message(chat_id, "Done!!")
    else:
        return await bot.send_message(chat_id, "Data Tidak Ditemukan!!")


"""bot Ping"""
@bot.on_message(filters.command("ping", "") & filters.user(OWNER_ID))
async def ping_(client, message):
    start = datetime.now()
    ping = udb.ping()
    end = datetime.now()
    delta_ping = (end - start).microseconds / 100000
    delta_ping_str = f"{delta_ping:.2f}"
    if ping:
        await message.reply(f"PONGG  `{delta_ping_str.replace('.', ',')}ms` !!")