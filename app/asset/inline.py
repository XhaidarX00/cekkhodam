# from pyrogram import Client, filters
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultCachedSticker, InputTextMessageContent

# # Inisialisasi bot dengan API ID dan API HASH dari my.telegram.org dan bot token dari BotFather
# app = Client("unobot",
#     api_id=17250424,
#     api_hash="753bc98074d420ef57ddf7eb1513162b",
#     bot_token="7217731238:AAESZA-y-JgN1PwhGdxEewj3kH3bUOG6HHU"
# )

# # Daftar ID pengguna yang diizinkan
# ALLOWED_USER_IDS = [2099942562]  # Ganti dengan ID pengguna yang diizinkan

# # Handler untuk perintah /start
# @app.on_message(filters.command("start"))
# async def start(client, message):
#     keyboard = InlineKeyboardMarkup([
#         [InlineKeyboardButton("Pilih Stiker", switch_inline_query_current_chat="")]
#     ])
#     await message.reply("Klik tombol di bawah untuk memilih stiker:", reply_markup=keyboard)

# # Handler untuk inline queries
# @app.on_inline_query()
# async def inline_query(client: Client, inline_query):
#     user_id = inline_query.from_user.id

#     if user_id not in ALLOWED_USER_IDS:
#         await client.answer_inline_query(
#             inline_query.id,
#             results=[],
#             switch_pm_text="Anda tidak diizinkan menggunakan fitur ini.",
#             switch_pm_parameter="start"
#         )
#         return

#     # Daftar stiker yang tersedia untuk dipilih
#     stickers = [
#         "CAACAgQAAxkBAANpZnlWNbMrqxKO1vwv_szZuF-HA88AAtMUAAKlYZlR8qxUgG8bX48eBA",  # Gantikan dengan file_id stiker yang valid
#         "CAACAgQAAxkBAANrZnlWOL1HPIB3t9nscQfghuvKvEIAAjIQAAL1TphRh9vOCyGO3HoeBA",
#         # "CAACAgQAAxkBAANtZnlWOqOblN_oC9dEC09y0GijjYsAAmEQAAK55JlRpqlx4Y1hAcQeBA",
#         # "CAACAgQAAxkBAANvZnlWPCi2VJK7zirWK3gjT8YMN8IAAvkMAAIG2ZhRpbVJZ7JQzVEeBA",
#         "CAACAgUAAxkBAAMlZodcDctovUUe9RmmQ2iQI2MdSMsAAroRAAKmczlUsrG8cYYIn_QeBA",
#         "CAACAgUAAxkBAAMjZodcC-40HxXprEuQ6Fr74yahUSMAArkQAAJEKUFU87c8xh2rf8keBA",
#         "CAACAgUAAxkBAAMhZodcCpFp5_YTmpeIfqxBb7n-tF0AAjENAAIrIkBU_5irPBWD7DEeBA",
#     ]
    
#     notPLayable = [
#         "CAADBAADsBMAAuGdkFHTZ-jl4eNn-gI",
#         "CAADBAADVA4AAhpfkFEKt19qveGSPgI",
#         "CAADBAADrw0AAoWsmVHguULNoYJwUwI",
#     ]
    
#     results = [
#         InlineQueryResultCachedSticker(
#             id=str(i),
#             sticker_file_id=sticker
#         ) for i, sticker in enumerate(stickers)
#     ]
    
#     results += [
#         InlineQueryResultCachedSticker(
#             id=str(i+len(stickers)),
#             sticker_file_id=sticker,
#             input_message_content=InputTextMessageContent("Masuk")
#         ) for i, sticker in enumerate(notPLayable)
#     ]
    
#     await client.answer_inline_query(inline_query.id, results)

# # Handler untuk chosen inline result
# @app.on_chosen_inline_result()
# async def chosen_inline_result(client, chosen_inline_result):
#     # Mendapatkan informasi tentang hasil yang dipilih
#     result_id = chosen_inline_result.result_id
#     from_user_id = chosen_inline_result.from_user.id

#     # Mengirim pesan ke pengguna
#     await client.send_message(
#         chat_id=from_user_id,
#         text=f"Anda telah memilih stiker dengan ID: {result_id} untuk bantu **Power Khodam**"
#     )

# # Handler untuk mendapatkan file_id stiker
# @app.on_message(filters.sticker)
# async def get_sticker_file_id(client, message):
#     sticker = message.sticker
#     file_id = sticker.file_id
#     await message.reply(f"File ID stiker yang Anda kirim adalah:\n\n`{file_id}`")

# # Menjalankan bot
# app.run()
