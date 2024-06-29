import re
import random
import json
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineQuery
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
from app import bot, OWNER_ID, REDISURL
from app.src.helpers.parser import mention_html

app = bot
r = REDISURL

data_jurus = ["Tendang", "Pukul", "Sundul", "Sleding", "Sikut", "Jenggut", "Tamparan", "Tonjokan", "Sekap", "Tindih", "Jambak", "Sindiran"]
Hasil_Tarung = ["Menang", "Kalah", "Seri"]
gamePower = ["Gunting", "Batu", "Kertas"]
openWar = []
tambahPowerKhodam = {}

path = "app/asset/data.json"

# Membaca data Khodam dari file JSON
with open(path, "r") as file:
    khodam_data = json.load(file)
    khodam_list = khodam_data["khodams"]
    dare_list = khodam_data["dare"]
    truth_list = khodam_data["truth"]
    

TruthOrDare = ["truth", "dare"]

def truth_or_dare(hasil):
    TD_ = random.choice(TruthOrDare)
    dareortruth = ""
    question = None
    if TD_ == "dare":
        dareortruth = "Dare"
        question = random.choice(dare_list)
    else:
        dareortruth = "Truth"
        question = random.choice(truth_list)
        
    text_ = f"{dareortruth} untuk kamu!!\n🤷 : {question}"
    text__ = f"Lawan Kamu dapet {dareortruth}\n🤷 : {question}"
    
    return (text__, text_) if hasil == "Menang" else (text_, text__)
    

rank_list = []

def urutTerbesar(ranking_list):
    # Mengurutkan kamus berdasarkan nilai (value) dari yang terbesar ke yang terkecil
    sorted_ranking = dict(sorted(ranking_list.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_ranking


async def show_ranking():
    try:
        if not r.get("ranklist"):
            return "😈 Rank Khodam Kosong!"
    except:
        return "😈 Rank Khodam Kosong!"
    
    rank_list = r.get("ranklist")
    list_ = {}
    for user_id in rank_list:
        value = r.get(f"{user_id}_point")
        list_[user_id] = value
    
    text = "😈 Ranking Khodam : \n"
    list_urut = urutTerbesar(list_)
    for index, (user_id, value) in enumerate(list_urut.items(), start = 1):
        user = await bot.get_users(user_id)
        mention = user.mention
        text += f"{index}. {mention}\n"
    
    return text
    

def byte_to_string(value):
    
    # Mengubah byte ke string
    value_str = value.decode('utf-8')

    # Menggunakan regex untuk mengambil angka saja
    numbers = re.findall(r'\d+', value_str)

    # Menggabungkan angka yang ditemukan (jika ada lebih dari satu) menjadi satu string
    result = ''.join(numbers)
    
    return int(result)

async def tambah_point(user_id):
    if not r.get("ranklist"):
        r.set("ranklist", str([user_id]))
    else:
        list_rank = r.get("ranklist")
        list_rank = eval(list_rank)
        list_rank.append(user_id)
        r.set("ranklist", list_rank)
        
    try:
        key = f"{user_id}_point"
        if r.get(key):
            r.incr(key)
            value = byte_to_string(r.get(key))
            return value
        else:
            r.set(key, 1)
            return 1
    except:
        return None


# Fungsi untuk membuat tombol keyboard
def make_keyboard():
    keyboard = [
        [InlineKeyboardButton("🔥 Show Arena", callback_data="show_arena"), InlineKeyboardButton("Show Rank 🔥", callback_data="show_rank")],
        [InlineKeyboardButton("👾 Cek Khodam 👾", callback_data="cek_khodam")],
        [InlineKeyboardButton("👹 Ganti Jurus", callback_data="ganti_jurus"), InlineKeyboardButton("Ganti Khodam 👹", callback_data="ganti_khodam")],
        # [InlineKeyboardButton("Buat Jurus", callback_data="buat_jurus"), InlineKeyboardButton("Ganti Jurus", callback_data="ganti_jurus")],
        [InlineKeyboardButton("⚔️ Open War", callback_data="open_war"), InlineKeyboardButton("Tutup War ⚔️", callback_data="tutup_war")]
    ]
    return InlineKeyboardMarkup(keyboard)


# Reset
@app.on_message(filters.command("reset") & filters.user(2099942562))
async def Reset(client: Client, message:Message):
    if r.flushdb(True):
        return await message.reply("Reset Berhasil")
    
    await message.reply("Reset Gagal")
    

async def getDataPengguna(user_id):
    dataPengguna = r.get(f"user:{user_id}")
    if not dataPengguna:
        return
    else:
        dataPengguna = eval(dataPengguna)
        return dataPengguna


# akumulasi kertas gunting batu
async def KertasGuntingBatu(power, powerLawan):
    # await bot.send_message(OWNER_ID, f"Power {power}\n PowerLawan {powerLawan}")
    power = power.capitalize()
    powerLawan = powerLawan.capitalize()
    if not power:
        return "Kalah"
    
    if not powerLawan:
        return "Menang"
    
    if power == powerLawan:
        return "Seri"
    
    if power == "Gunting" and powerLawan == "Kertas":
        result = "Menang"
    elif powerLawan == "Gunting" and power == "Kertas":
        result = "Kalah"
    elif power == "Kertas" and powerLawan == "Batu":
        result = "Menang"
    elif powerLawan == "Kertas" and power == "Batu":
        result = "Kalah"
    elif power == "Batu" and powerLawan == "Gunting":
        result = "Menang"
    elif powerLawan == "Batu" and power == "Gunting":
        result = "Kalah"
    else:
        return
    
    return result


# Perang
@app.on_message(filters.command("war"))
async def war(client: Client, message:Message):
    global tambahPowerKhodam
    if len(openWar) == 0:
        return await message.reply("🙈 Saat ini Ngga ada yang Open War Bree!")
        
    user_id = message.from_user.id
    opsi = message.text.split(None, 1)[1] if len(message.text.split()) == 2 else ""
    try:
        opsi = int(opsi)
    except ValueError:
        await message.reply("**🐲 Gunakan Format :** /war no urut dalam angka!!")
    
    if opsi:
        try:
            lawan_id = openWar[opsi - 1]
        except:
            return message.reply("🐲 Lawan Sudah Menutup war!!")
        
        if int(lawan_id) == user_id:
            return await message.reply(f"🚫 Kamu tidak bisa menyerang diri sendiri {message.from_user.mention}")
        
        # data lawan
        dataPenggunaLawan = await getDataPengguna(lawan_id)
        khodamLawan = dataPenggunaLawan['khodam']
        jurusLawan = dataPenggunaLawan['jurus']
        
        # data Pribadi
        dataPengguna = await getDataPengguna(user_id)
        khodam = dataPengguna['khodam']
        jurus = dataPengguna['jurus']
        
        # Remove data in openWar
        # openWar.remove(lawan_id)
        # openWar.remove(user_id)
        
        # lawan = random.choice(khodam_list)
        # hasil = random.choice(Hasil_Tarung)
        tambahPower = tambahPowerKhodam[user_id] if user_id in tambahPowerKhodam else ""
        tambahPowerLawan = tambahPowerKhodam[lawan_id] if lawan_id in tambahPowerKhodam else ""
        
        hasil = await KertasGuntingBatu(tambahPower, tambahPowerLawan)
        text_tarung_lawan = ""
        hasilLawan = ""
        text_tarung = f"⚔️ {khodamLawan} VS {khodam} ⚔️\n\nSEDANG BERTARUNGG !!!"
        pesan = await client.send_message(user_id, text_tarung)
        serang = await client.send_message(lawan_id, text_tarung)
        await asyncio.sleep(4)
        if hasil == "Menang":
            text_tarung = f"😈 Wah Khodam mu Mengeluarkan {jurus}an Kematian!!"
            text_tarung_lawan = f"😭 Wah Khodam mu Melemah Terkena {jurus}an Kematian!!"
            hasil_ = f"💪 Kamu {hasil} lawan {khodamLawan} dengan jurus {jurus}an adalan 🎉🎉!!"
            hasilLawan = f"😭 Kamu Kalah karena di{jurus} sama {khodam}, Cepat Ganti Jurus dan coba lagi!!"
            Point = await tambah_point(user_id)
            if Point:
                hasil_ += f"\n📝 Score Kamu : {Point}"
        
        elif hasil == "Kalah":
            text_tarung_lawan = f"😈 Wah Khodam mu Mengeluarkan {jurus}an Kematian!!"
            text_tarung = f"😭 Wah Khodam mu Melemah Terkena {jurusLawan}an Kematian!!"
            hasil_ = f"😭 Kamu {hasil} karena di{jurusLawan} {khodam}, Cepat Ganti Jurus dan coba lagi!!"
            hasilLawan = f"💪 Kamu Menang lawan {khodam} dengan jurus {jurus}an adalan 🎉🎉!!"
            Point = await tambah_point(lawan_id)
            if Point:
                hasilLawan += f"\n📝 Score Kamu : {Point}"
        
        elif hasil == "Seri":
            text_tarung_lawan = f"😈 Wah Khodam mu Masih Bertahan!!"
            text_tarung = f"😈 Wah Khodam mu Masih Bertahan!!"
            hasil_ = f"🐲 Wah {hasil} {khodam} dan {khodamLawan} sama-sama kuat 💪!!"
            hasilLawan = f"🐲 Wah {hasil} {khodam} dan {khodamLawan} sama-sama kuat 💪!!"
        
        else:
            text_error = "Terjadi Kesalahan Segera Lapor ke @kenapatagdar"
            await pesan.edit(text_error)
            await serang.edit(text_error)
            await bot.send_message(OWNER_ID, "Hasil dari Kertas Gunting Batu Tidak Ada!!")
            return
        
        await pesan.edit(text_tarung)
        await serang.edit(text_tarung_lawan)
        await asyncio.sleep(3)
        
        hasil_ += "\n\nKetik /gaskeun untuk memulai kembali"
        hasilLawan += "\n\nKetik /gaskeun untuk memulai kembali"
        await pesan.edit(hasil_)
        await serang.edit(hasilLawan)
        await asyncio.sleep(2)
        if hasil != "Seri":
            notif, question = truth_or_dare(hasil)
            await client.send_message(lawan_id, question)
            await client.send_message(user_id, notif)

        
        
# Fungsi untuk mengirimkan pesan dengan tombol keyboard
@app.on_message(filters.command(["start", "gaskeun"]))
async def start(client, message: Message):
    await message.reply("👾 Selamat datang di bot cek khodam!", reply_markup=make_keyboard())

@app.on_callback_query()
async def handle_callback_query(client: Client, callback_query: CallbackQuery):
    global openWar
    user_id = callback_query.from_user.id
    dataPengguna = r.get(f"user:{user_id}")
    name = callback_query.from_user.first_name
    try:
        if callback_query.from_user.last_name:
            name += f" {callback_query.from_user.last_name}"
    except:
        pass
    
    if not dataPengguna:
        dataPengguna = {}
    else:
        dataPengguna = eval(dataPengguna)
    
    jurus = "Sledingan"
    
    if callback_query.data == "cek_khodam":
        if "jurus" not in dataPengguna:
            jurus = random.choice(data_jurus)
            dataPengguna["jurus"] = jurus
            r.set(f"user:{user_id}", str(dataPengguna))
            
        if f"user:{user_id}:khodam" in r: 
            jurus = dataPengguna["jurus"]    
            mention = await mention_html(name, user_id)
            await callback_query.message.reply(f"😈 Khodam : **{dataPengguna['khodam']}**\n├ Jurus: {dataPengguna['jurus']}\n╰ Pemilik : {mention}")
        
        else:
            nama_khodam = random.choice(khodam_list)
            dataPengguna["khodam"] = nama_khodam
            r.set(f"user:{user_id}", str(dataPengguna))
            # r.setex(f"user:{user_id}:khodam", 86400, nama_khodam)
            r.setex(f"user:{user_id}:khodam", 300, nama_khodam)
            await callback_query.message.reply(f"😈 Khodam kamu adalah **{nama_khodam}**")

    elif callback_query.data == "ganti_khodam":
        if "khodam" not in dataPengguna:
            await callback_query.message.reply("🙈 Kamu belum membuat khodam, tekan tombol cek khodam untuk memulai")
        elif f"user:{user_id}:khodam" in r:
            ttl = r.ttl(f"user:{user_id}:khodam")
            hours, remainder = divmod(ttl, 3600)
            minutes, _ = divmod(remainder, 60)
            await callback_query.message.reply(f"🙈 Belum bisa ganti khodam, sisa waktu {hours} Jam {minutes} Menit")
        else:
            while True:
                nama_khodam = random.choice(khodam_list)
                if nama_khodam != dataPengguna["khodam"]:
                    break
            dataPengguna["khodam"] = nama_khodam
            r.set(f"user:{user_id}", str(dataPengguna))
            r.setex(f"user:{user_id}:khodam", 300, nama_khodam)
            await callback_query.message.reply(f"😈 Khodam kamu telah diganti menjadi {nama_khodam}")

    # elif callback_query.data == "buat_jurus":
    #     if "jurus" not in dataPengguna:
    #         jurus = random.choice(data_jurus)
    #         dataPengguna["jurus"] = jurus
    #         r.set(f"user:{user_id}", str(dataPengguna))
        
    #     jurus = dataPengguna["jurus"]
    #     await callback_query.message.reply(f"👹 Jurus yang kamu buat adalah {jurus}an")

    elif callback_query.data == "ganti_jurus":
        if "jurus" not in dataPengguna:
            return await callback_query.message.reply("🙈 Kamu belum membuat jurus, tekan tombol buat jurus untuk memulai")
        else:
            while True:
                jurus = random.choice(data_jurus)
                if jurus != dataPengguna["jurus"]:
                    break
            dataPengguna["jurus"] = jurus
            r.set(f"user:{user_id}", str(dataPengguna))
            await callback_query.message.reply(f"👹 Jurus kamu telah diganti menjadi {jurus}an")
    
    elif callback_query.data == "show_rank":
        text = await show_ranking()
        await callback_query.message.reply(text) 
        
    elif callback_query.data == "show_arena":
        if len(openWar) == 0:
            return await callback_query.message.reply("🙈 Saat ini Ngga ada yang Open War Bree!")
        
        if "khodam" not in dataPengguna or "jurus" not in dataPengguna:
            await callback_query.message.reply("🙈 Kamu harus membuat khodam dan atau jurus terlebih dahulu")
        else:
            text = "😈 Khodam open War\n"
            for index, user_id in enumerate(openWar, start=1):
                # mention = await mention_html(name, user_id)
                dataPengguna = r.get(f"user:{user_id}")
                if not dataPengguna:
                    pass
                else:
                    dataPengguna = eval(dataPengguna)
                    user = await client.get_users(user_id)
                    text += f"{index}. {dataPengguna['khodam']} [{user.mention}]\n"
                    
                if index % 20 == 0:
                    await callback_query.message.reply(text)
            
            text += "\n⚔️ Untuk menyerang ketik /war lalu tambahkan nomor urut lawan\nContoh : /war 1 yang artinya kamu akan menyerang khodam lawan no urut 1"
            await callback_query.message.reply(text)
            # await callback_query.message.reply(f"Khodam: {dataPengguna['khodam']}\nJurus: {dataPengguna['jurus']}")

    elif callback_query.data == "open_war":
        if "khodam" not in dataPengguna or "jurus" not in dataPengguna:
            await callback_query.message.reply("Kamu harus membuat khodam dan jurus terlebih dahulu")
        else:
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("Tambah Power", switch_inline_query_current_chat="")]
            ])
            
            text = "⚔️ Kamu sudah Open War klik show arena untuk mulai perang ⚔️!!"
            if user_id in openWar:
                pass
            else:
                openWar.append(user_id)
                text = "⚔️ Open War telah dibuka klik show arena untuk mulai perang ⚔️!!"
            
            text += "\nKlik tombol untuk menambah Power Khodam 🔥🔥"
            return await callback_query.message.reply(text, reply_markup=keyboard)
            
            # lawan = random.choice(khodam_list)
            # hasil = random.choice(Hasil_Tarung)
            # await callback_query.message.reply(f"Khodam kamu: {dataPengguna['khodam']}\nJurus kamu: {dataPengguna['jurus']}\n\nLawan: {lawan}\n\nHasil Tarung: {hasil}")

    elif callback_query.data == "tutup_war":
        if user_id not in openWar:
            return await callback_query.message.reply("🙈 Kamu belum Open War Gimana mau ditutup?")
        else:
            try:
                openWar.remove(user_id)
            except:
                pass
            
            if user_id not in tambahPowerKhodam:
                pass
            else:
                del tambahPowerKhodam[user_id]
                
            await callback_query.message.reply("🙈 War telah ditutup")


# Handler untuk inline queries
@app.on_inline_query()
async def inline_query(client: Client, inline_query: InlineQuery):
    global openWar
    user_id = inline_query.from_user.id
    if user_id not in openWar:
        return await client.send_message(user_id, "🙈 Kamu belum Open War, Klik Open War untuk Memulai!!")
    else:
        emojis = [
            ("Gunting", "✌️"),  # Peace hand sign
            ("Batu", "✊"),  # Raised fist
            ("Kertas", "✋")   # Raised hand
        ]

        results = [
            InlineQueryResultArticle(
                id=i,
                title=i,
                input_message_content=InputTextMessageContent(message_text=emoji)
            ) for i, emoji in emojis
        ]

        await client.answer_inline_query(inline_query.id, results)

# Handler untuk chosen inline result
@app.on_chosen_inline_result()
async def chosen_inline_result(client: Client, chosen_inline_result):
    global tambahPowerKhodam, gamePower
    # Mendapatkan informasi tentang hasil yang dipilih
    result_id = chosen_inline_result.result_id
    from_user_id = chosen_inline_result.from_user.id
    
    # if result_id == "Gunting":
    #     result_id = "Gunting"
    # elif result_id =="Batu":
    #     result_id = "Batu"
    # elif result_id == "Kertas":
    #     result_id = "Kertas"
    # else:
    #     return 
    
    if result_id not in gamePower:
        return await client.send_message(
        chat_id=from_user_id,
        text=f"{result_id} Tidak ada di list Game Power"
    )
    
    # Mengirim pesan ke pengguna
    await client.send_message(
        chat_id=from_user_id,
        text=f"Kamu memilih {result_id} untuk bantu **Power Khodam**"
    )
    
    await client.send_message(
        chat_id=OWNER_ID,
        text=f"{chosen_inline_result.from_user.mention} {result_id}"
    )
    
    result_id = result_id.capitalize()
    
    tambahPowerKhodam[from_user_id] = result_id
    
    text = "😈 Khodam open War\n"
    for index, user_id in enumerate(openWar, start=1):
        # mention = await mention_html(name, user_id)
        dataPengguna = r.get(f"user:{user_id}")
        if not dataPengguna:
            pass
        else:
            dataPengguna = eval(dataPengguna)
            user = await client.get_users(user_id)
            text += f"{index}. {dataPengguna['khodam']} [{user.mention}]\n"
            
        if index % 20 == 0:
           await client.send_message(
                chat_id=from_user_id,
                text=text
            )
    
    text += "\n⚔️ Untuk menyerang ketik /war lalu tambahkan nomor urut lawan\nContoh : /war 1 yang artinya kamu akan menyerang khodam lawan no urut 1"
    await client.send_message(
        chat_id=from_user_id,
        text=text
    )