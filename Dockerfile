# Menggunakan image dasar Python 3.10
FROM python:3.10-slim

# Mengupdate sistem dan menginstall paket yang diperlukan termasuk Git
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        git \
        && apt-get upgrade -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Menetapkan direktori kerja
WORKDIR /app

# Menyalin file requirements.txt terlebih dahulu untuk meng-cache dependensi
COPY requirements.txt .

# Menginstal dependensi Python yang diperlukan
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Menyalin semua file ke dalam direktori kerja
COPY . .

# Memberi izin eksekusi pada skrip start.sh
RUN chmod +x start.sh

# Menjalankan skrip start.sh saat container dimulai
CMD ["bash", "start.sh"]
