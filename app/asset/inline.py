# from pyrogram import Client, filters
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultCachedSticker, InlineQueryResultArticle, InputTextMessageContent

# # Inisialisasi bot dengan API ID dan API HASH dari my.telegram.org dan bot token dari BotFather
# app = Client("khodam_bot",
#     api_id = 17250424,
#     api_hash = "753bc98074d420ef57ddf7eb1513162b",
#     bot_token = "7150366217:AAGqdvHMtx-HtttFHL7MqRiN5C5c_kIajX0"
# )


# # Handler untuk perintah /start
# @app.on_message(filters.command("start"))
# async def start(client, message):
#     keyboard = InlineKeyboardMarkup([
#         [InlineKeyboardButton("Pilih Stiker", switch_inline_query_current_chat="")]
#     ])
#     await message.reply("Klik tombol di bawah untuk memilih stiker:", reply_markup=keyboard)

# # Handler untuk inline queries
# @app.on_inline_query()
# async def inline_query(client, inline_query):
#     # Daftar stiker yang tersedia untuk dipilih
#     # stickers = [
#     #     "CAACAgQAAxkBAANpZnlWNbMrqxKO1vwv_szZuF-HA88AAtMUAAKlYZlR8qxUgG8bX48eBA",  # Gantikan dengan file_id stiker yang valid
#     #     "CAACAgQAAxkBAANrZnlWOL1HPIB3t9nscQfghuvKvEIAAjIQAAL1TphRh9vOCyGO3HoeBA",
#     #     "CAACAgQAAxkBAANtZnlWOqOblN_oC9dEC09y0GijjYsAAmEQAAK55JlRpqlx4Y1hAcQeBA",
#     #     "CAACAgQAAxkBAANvZnlWPCi2VJK7zirWK3gjT8YMN8IAAvkMAAIG2ZhRpbVJZ7JQzVEeBA",
#     # ]

#     # results = [
#     #     InlineQueryResultCachedSticker(
#     #         id=str(i),
#     #         sticker_file_id=sticker
#     #     ) for i, sticker in enumerate(stickers)
#     # ]
    
#     emojis = [
#         ("Gunting", "✌️"),  # Peace hand sign
#         ("Batu", "✊"),  # Raised fist
#         ("Kertas", "✋")   # Raised hand
#     ]

#     results = [
#         InlineQueryResultArticle(
#             id=i,
#             title=i,
#             input_message_content=InputTextMessageContent(message_text=emoji)
#         ) for i, emoji in emojis
#     ]

#     await client.answer_inline_query(inline_query.id, results)

# # Handler untuk chosen inline result
# @app.on_chosen_inline_result()
# async def chosen_inline_result(client, chosen_inline_result):
#     # Mendapatkan informasi tentang hasil yang dipilih
#     result_id = chosen_inline_result.result_id
#     from_user_id = chosen_inline_result.from_user.id
    
#     if result_id == "Gunting":
#         result_id = "Gunting"
#     elif result_id =="Batu":
#         result_id = "Batu"
#     else:
#         result_id = "Kertas"
    
#     # Mengirim pesan ke pengguna
#     await client.send_message(
#         chat_id=from_user_id,
#         text=f"Anda telah memilih {result_id} untuk bantu **Power Khodam**"
#     )



# @app.on_message(filters.sticker)
# async def get_sticker_file_id(client, message):
#     sticker = message.sticker
#     file_id = sticker.file_id
#     await message.reply(f"File ID stiker yang Anda kirim adalah:\n\n`{file_id}`")




# # Menjalankan bot
# app.run()