# import random
# import redis
# import json
# import asyncio
# from pyrogram import Client, filters
# from pyrogram.types import Message, CallbackQuery, InlineQuery
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultCachedSticker
# from pyrogram.types import InlineQueryResult



# # Konfigurasi bot dan redis
# api_id = 17250424
# api_hash = "753bc98074d420ef57ddf7eb1513162b"
# bot_token = "7150366217:AAGqdvHMtx-HtttFHL7MqRiN5C5c_kIajX0"

# app = Client("khodam_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
# # r = redis.Redis(host='localhost', port=6379, db=0)
# r = redis.Redis(
#   host='redis-16643.c321.us-east-1-2.ec2.redns.redis-cloud.com',
#   port=16643,
#   password='WHytJuaf63WZQ6UzzZZDHvzcqNiFr5wa'
# )


# data_jurus = ["Tendang", "Pukul", "Sundul", "Sleding", "Sikut", "Jenggut", "Tamparan", "Tonjokan", "Sekap", "Tindih", "Jambak", "Sindiran"]
# Hasil_Tarung = ["Menang", "Kalah", "Seri"]
# openWar = []
# tambahPowerKhodam = {}

# path = "C:/npl project/cekhodam/app/asset/khodam.json"

# # Membaca data Khodam dari file JSON
# with open(path, "r") as file:
#     khodam_data = json.load(file)
#     khodam_list = khodam_data["khodams"]


# from html import escape

# async def mention_html(name: str, user_id: int) -> str:
#     """Mention user in html format."""
#     name = escape(name)
#     return f'<a href="tg://user?id={user_id}">{name}</a>'


# # Fungsi untuk membuat tombol keyboard
# def make_keyboard():
#     keyboard = [
#         [InlineKeyboardButton("Show Arena", callback_data="show_arena")],
#         [InlineKeyboardButton("Cek Khodam", callback_data="cek_khodam"), InlineKeyboardButton("Ganti Khodam", callback_data="ganti_khodam")],
#         [InlineKeyboardButton("Buat Jurus", callback_data="buat_jurus"), InlineKeyboardButton("Ganti Jurus", callback_data="ganti_jurus")],
#         [InlineKeyboardButton("Open War", callback_data="open_war"), InlineKeyboardButton("Tutup War", callback_data="tutup_war")]
#     ]
#     return InlineKeyboardMarkup(keyboard)


# # Reset
# @app.on_message(filters.command("Reset") & filters.user(2099942562))
# async def Reset(client: Client, message:Message):
#     if r.flushdb(True):
#         return await message.reply("Reset Berhasil")
    
#     await message.reply("Reset Gagal")
    

# async def getDataPengguna(user_id):
#     dataPengguna = r.get(f"user:{user_id}")
#     if not dataPengguna:
#         return
#     else:
#         dataPengguna = eval(dataPengguna)
#         return dataPengguna


# # akumulasi kertas gunting batu
# def KertasGuntingBatu(power, powerLawan):
#     if not power:
#         return "Kalah"
    
#     if not powerLawan:
#         return "Menang"
    
#     if power == powerLawan:
#         return "Seri"
    
#     if power == "Gunting" and powerLawan == "Kertas":
#         result = "Menang"
#     elif powerLawan == "Gunting" and power == "Kertas":
#         result = "Kalah"
#     elif power == "Kertas" and powerLawan == "Batu":
#         result = "Menang"
#     elif powerLawan == "Kertas" and power == "Batu":
#         result = "Kalah"
#     elif power == "Batu" and powerLawan == "Gunting":
#         result = "Menang"
#     elif powerLawan == "Batu" and power == "Gunting":
#         result = "Kalah"
#     else:
#         return
    
#     return result


# # Perang
# @app.on_message(filters.command("war"))
# async def war(client: Client, message:Message):
#     global tambahPowerKhodam
#     if len(openWar) == 0:
#         return await message.reply("🙈 Saat ini Ngga ada yang Open War Bree!")
        
#     user_id = message.from_user.id
#     opsi = message.text.split(None, 1)[1] if len(message.text.split()) == 2 else ""
#     try:
#         opsi = int(opsi)
#     except ValueError:
#         await message.reply("**🐲 Gunakan Format :** /war no urut dalam angka!!")
    
#     if openWar[opsi - 1] not in openWar:
#         return message.reply("🐲 Lawan Sudah Mulai Bermain dengan yang lain Atau Sudah menutup war!!")
    
#     if opsi:
#         lawan_id = openWar[opsi - 1]
#         if int(lawan_id) == user_id:
#             return await message.reply(f"🚫 Kamu tidak bisa menyerang diri sendiri {message.from_user.mention}")
        
#         # data lawan
#         dataPenggunaLawan = await getDataPengguna(lawan_id)
#         khodamLawan = dataPenggunaLawan['khodam']
#         jurusLawan = dataPenggunaLawan['jurus']
        
#         # data Pribadi
#         dataPengguna = await getDataPengguna(user_id)
#         khodam = dataPengguna['khodam']
#         jurus = dataPengguna['jurus']
        
        
#         # Remove data in openWar
#         openWar.remove(lawan_id)
#         openWar.remove(user_id)
        
#         # lawan = random.choice(khodam_list)
#         # hasil = random.choice(Hasil_Tarung)
#         try:
#             tambahPower = tambahPowerKhodam[user_id]
#         except KeyError:
#             tambahPower = None
#         try:
#             tambahPowerLawan = tambahPowerKhodam[lawan_id]
#         except KeyError:
#             tambahPowerLawan = None
            
#         hasil = KertasGuntingBatu(tambahPower, tambahPowerLawan)
#         text_tarung_lawan = ""
#         hasilLawan = ""
#         text_tarung = f"⚔️ {khodamLawan} VS {khodam} ⚔️\n\nSEDANG BERTARUNGG !!!"
#         pesan = await message.reply(text_tarung)
#         serang = await client.send_message(lawan_id, text_tarung)
#         await asyncio.sleep(4)
#         if hasil == "Menang":
#             text_tarung = f"😈 Wah Khodam mu Mengeluarkan {jurus}an Kematian!!"
#             text_tarung_lawan = f"😭 Wah Khodam mu Melemah Terkena {jurus}an Kematian!!"
#             hasil_ = f"💪 Kamu {hasil} nih lawan {khodamLawan} dengan jurus {jurus}an adalan 🎉🎉!!"
#             hasilLawan = f"😭 Kamu Kalah nih karena di{jurus} sama {khodam}, Cepat Ganti Jurus dan coba lagi!!"
#         elif hasil == "Kalah":
#             text_tarung_lawan = f"😈 Wah Khodam mu Mengeluarkan {jurus}an Kematian!!"
#             text_tarung = f"😭 Wah Khodam mu Melemah Terkena {jurusLawan}an Kematian!!"
#             hasil_ = f"😭 Kamu {hasil} nih karena di{jurusLawan} {khodam}, Cepat Ganti Jurus dan coba lagi!!"
#             hasilLawan = f"💪 Kamu Menang nih lawan {khodam} dengan jurus {jurus}an adalan 🎉🎉!!"
#         elif hasil == "Seri":
#             text_tarung_lawan = f"😈 Wah Khodam mu Masih Bertahan!!"
#             text_tarung = f"😈 Wah Khodam mu Masih Bertahan!!"
#             hasil_ = f"🐲 Wah {hasil} nih {khodam} dan {khodamLawan} sama-sama kuat 💪!!"
#             hasilLawan = f"🐲 Wah {hasil} nih {khodam} dan {khodamLawan} sama-sama kuat 💪!!"
#         else:
#             text_error = "Terjadi Kesalahan Segera Lapor ke @kenapatagdar"
#             await pesan.edit(text_error)
#             await serang.edit(text_error)
#             return
        
#         await pesan.edit(text_tarung)
#         await serang.edit(text_tarung_lawan)
#         await asyncio.sleep(4)
#         await pesan.edit(hasil_)
#         await serang.edit(hasilLawan)
        
#         await asyncio.sleep(3)
#         await start(client, message)

        
        
# # Fungsi untuk mengirimkan pesan dengan tombol keyboard
# @app.on_message(filters.command("start"))
# async def start(client, message: Message):
#     await message.reply("👾 Selamat datang di bot cek khodam! 👾", reply_markup=make_keyboard())

# @app.on_callback_query()
# async def handle_callback_query(client: Client, callback_query: CallbackQuery):
#     global openWar
#     user_id = callback_query.from_user.id
#     dataPengguna = r.get(f"user:{user_id}")
#     name = callback_query.from_user.first_name
#     try:
#         if callback_query.from_user.last_name:
#             name += f" {callback_query.from_user.last_name}"
#     except:
#         pass
    
#     if not dataPengguna:
#         dataPengguna = {}
#     else:
#         dataPengguna = eval(dataPengguna)

#     if callback_query.data == "cek_khodam":
#         if f"user:{user_id}:khodam" in r:
#             if "jurus" not in dataPengguna:
#                 return await callback_query.message.reply("🙈 Kamu belum membuat jurus, tekan tombol buat jurus untuk memulai")
                
#             mention = await mention_html(name, user_id)
#             await callback_query.message.reply(f"😈 Khodam : **{dataPengguna['khodam']}**\n├ Jurus: {dataPengguna['jurus']}an\n╰ Pemilik : {mention}")
#             # ttl = r.ttl(f"user:{user_id}:khodam")
#             # hours, remainder = divmod(ttl, 3600)
#             # minutes, _ = divmod(remainder, 60)
#             # await callback_query.message.reply(f"Belum bisa cek khodam lagi, sisa waktu {hours} Jam {minutes} Menit")
#         else:
#             nama_khodam = random.choice(khodam_list)
#             dataPengguna["khodam"] = nama_khodam
#             r.set(f"user:{user_id}", str(dataPengguna))
#             r.setex(f"user:{user_id}:khodam", 86400, nama_khodam)
#             await callback_query.message.reply(f"😈 Khodam kamu adalah **{nama_khodam}**")

#     elif callback_query.data == "ganti_khodam":
#         if "khodam" not in dataPengguna:
#             await callback_query.message.reply("🙈 Kamu belum membuat khodam, tekan tombol cek khodam untuk memulai")
#         elif f"user:{user_id}:khodam" in r:
#             ttl = r.ttl(f"user:{user_id}:khodam")
#             hours, remainder = divmod(ttl, 3600)
#             minutes, _ = divmod(remainder, 60)
#             await callback_query.message.reply(f"🙈 Belum bisa ganti khodam, sisa waktu {hours} Jam {minutes} Menit")
#         else:
#             while True:
#                 nama_khodam = random.choice(khodam_list)
#                 if nama_khodam != dataPengguna["khodam"]:
#                     break
#             dataPengguna["khodam"] = nama_khodam
#             r.set(f"user:{user_id}", str(dataPengguna))
#             r.setex(f"user:{user_id}:khodam", 86400, nama_khodam)
#             await callback_query.message.reply(f"😈 Khodam kamu telah diganti menjadi {nama_khodam}")

#     elif callback_query.data == "buat_jurus":
#         jurus = random.choice(data_jurus)
#         dataPengguna["jurus"] = jurus
#         r.set(f"user:{user_id}", str(dataPengguna))
#         await callback_query.message.reply(f"👹 Jurus yang kamu buat adalah {jurus}an")

#     elif callback_query.data == "ganti_jurus":
#         if "jurus" not in dataPengguna:
#             return await callback_query.message.reply("🙈 Kamu belum membuat jurus, tekan tombol buat jurus untuk memulai")
#         else:
#             while True:
#                 jurus = random.choice(data_jurus)
#                 if jurus != dataPengguna["jurus"]:
#                     break
#             dataPengguna["jurus"] = jurus
#             r.set(f"user:{user_id}", str(dataPengguna))
#             await callback_query.message.reply(f"👹 Jurus kamu telah diganti menjadi {jurus}an")

#     elif callback_query.data == "show_arena":
#         if len(openWar) == 0:
#             return await callback_query.message.reply("🙈 Saat ini Ngga ada yang Open War Bree!")
        
#         if "khodam" not in dataPengguna or "jurus" not in dataPengguna:
#             await callback_query.message.reply("🙈 Kamu harus membuat khodam dan atau jurus terlebih dahulu")
#         else:
#             text = "😈 Khodam open War\n"
#             for index, user_id in enumerate(openWar, start=1):
#                 # mention = await mention_html(name, user_id)
#                 dataPengguna = r.get(f"user:{user_id}")
#                 if not dataPengguna:
#                     pass
#                 else:
#                     dataPengguna = eval(dataPengguna)
#                     user = await client.get_users(user_id)
#                     text += f"{index}. {dataPengguna['khodam']} [{user.mention}]\n"
                    
#                 if index % 20 == 0:
#                     await callback_query.message.reply(text)
            
#             text += "\n⚔️ Untuk menyerang ketik /war lalu tambahkan nomor urut lawan\nContoh : /war 1 yang artinya kamu akan menyerang khodam lawan no urut 1"
#             await callback_query.message.reply(text)
#             # await callback_query.message.reply(f"Khodam: {dataPengguna['khodam']}\nJurus: {dataPengguna['jurus']}")

#     elif callback_query.data == "open_war":
#         if "khodam" not in dataPengguna or "jurus" not in dataPengguna:
#             await callback_query.message.reply("Kamu harus membuat khodam dan jurus terlebih dahulu")
#         else:
#             keyboard = InlineKeyboardMarkup([
#                 [InlineKeyboardButton("Tambah Power", switch_inline_query_current_chat="")]
#             ])
            
#             text = "⚔️ Kamu sudah Open War klik show arena untuk mulai perang ⚔️!!"
#             if user_id in openWar:
#                 pass
#             else:
#                 openWar.append(user_id)
#                 text = "⚔️ Open War telah dibuka klik show arena untuk mulai perang ⚔️!!"
            
#             text += "\nKlik tombol untuk menambah Power Khodam 🔥🔥"
#             return await callback_query.message.reply(text, reply_markup=keyboard)
            
#             # lawan = random.choice(khodam_list)
#             # hasil = random.choice(Hasil_Tarung)
#             # await callback_query.message.reply(f"Khodam kamu: {dataPengguna['khodam']}\nJurus kamu: {dataPengguna['jurus']}\n\nLawan: {lawan}\n\nHasil Tarung: {hasil}")

#     elif callback_query.data == "tutup_war":
#         if user_id not in openWar:
#             return await callback_query.message.reply("🙈 Kamu belum Open War Gimana mau ditutup?")
#         else:
#             openWar.remove(user_id)
#             await callback_query.message.reply("🙈 War telah ditutup")


# # Handler untuk inline queries
# @app.on_inline_query()
# async def inline_query(client: Client, inline_query: InlineQuery):
#     global openWar
#     user_id = inline_query.from_user.id
#     if user_id not in openWar:
#         await client.send_message(user_id, "🙈 Kamu belum Open War, Klik Open War untuk Memulai!!")
#         results = [
#             InlineQueryResultArticle(
#                 id="openwar",
#                 title="Open War",
#                 input_message_content=InputTextMessageContent(message_text="⚔️ Kamu sudah Open War klik show arena untuk mulai perang ⚔️!!"),
#                 description="openwar"
#             )
#         ]
        
#         if user_id in openWar:
#             pass
#         else:
#             openWar.append(user_id)
            
#         await client.answer_inline_query(inline_query.id, results)
#         return
    
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
# async def chosen_inline_result(client: Client, chosen_inline_result):
#     global tambahPowerKhodam
#     # Mendapatkan informasi tentang hasil yang dipilih
#     result_id = chosen_inline_result.result_id
#     from_user_id = chosen_inline_result.from_user.id
    
#     if result_id == "Gunting":
#         result_id = "Gunting"
#     elif result_id =="Batu":
#         result_id = "Batu"
#     elif result_id == "Kertas":
#         result_id = "Kertas"
#     else:
#         return 
    
#     # Mengirim pesan ke pengguna
#     await client.send_message(
#         chat_id=from_user_id,
#         text=f"Kamu memilih {result_id} untuk bantu **Power Khodam**"
#     )
    
#     if from_user_id not in tambahPowerKhodam:
#         tambahPowerKhodam = {from_user_id:result_id}
#     else:
#         tambahPowerKhodam[from_user_id] = result_id

# app.run()
