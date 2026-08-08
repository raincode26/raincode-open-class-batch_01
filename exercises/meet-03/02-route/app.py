# app.py
# Topik: Route — Alamat Halaman

# ============================================================
# MISI KAMU
# ============================================================
# Route adalah alamat. / = halaman utama, /tentang = halaman lain,
# seperti alamat rumah yang menentukan surat diantar ke mana.
# Satu aplikasi boleh punya banyak route sekaligus.
#
# Route "/" di bawah sudah lengkap (hasil dari 01-flask-hello-world).
# Tugasmu: tambahkan beberapa route baru mengikuti pola yang sama.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Selamat datang di Expense Tracker!"


# TODO 1: Tambahkan route '/tentang' dengan function bernama tentang()
# yang me-return teks singkat menjelaskan aplikasi ini.
# Pola:
#   @app.route('/tentang')
#   def tentang():
#       return "Aplikasi pencatat pengeluaran harian, dibuat di RainCode."


# TODO 2: Tambahkan route '/kontak' dengan function bernama kontak()
# yang me-return teks kontak (bebas, contoh email/medsos).


# TODO 3: Tambahkan route DINAMIS '/halo/<nama>' dengan function
# sapa(nama) yang menerima bagian alamat sebagai parameter, lalu
# me-return sapaan personal. Ini pola yang SAMA dengan '/edit/<id>'
# dan '/hapus/<id>' yang akan kita pakai nanti di Expense Tracker.
# Pola:
#   @app.route('/halo/<nama>')
#   def sapa(nama):
#       return f"Halo, {nama}! Selamat datang."
#
# Coba buka /halo/Budi dan /halo/Sari di browser — perhatikan
# bagaimana satu route bisa melayani banyak alamat berbeda.


app.run(debug=True)
