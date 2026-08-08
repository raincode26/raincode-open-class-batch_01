# app.py
# Topik: Template Render — Mengirim Data Python ke HTML

# ============================================================
# MISI KAMU
# ============================================================
# Sejauh ini function route selalu me-return TEKS POLOS. Halaman
# nyata butuh HTML yang lengkap — dan HTML itu sebaiknya ditulis di
# file terpisah (templates/), bukan ditumpuk sebagai string di
# app.py. Di sinilah render_template() dan Jinja bekerja.
#
# Data di bawah ini SEMENTARA masih hidup di memori (list of dict) —
# persis pola dari Pertemuan 1. Baru di 05-sqlite-basic kita pindah
# ke database beneran.

from flask import Flask, render_template

app = Flask(__name__)

# Data sementara — nanti (mulai 06-create-table) ini akan datang dari
# SQLite, bukan ditulis manual seperti ini.
transaksi = [
    {'nama': 'Kopi pagi', 'nominal': 25000},
    {'nama': 'Makan siang', 'nominal': 35000},
    {'nama': 'Ongkos bus', 'nominal': 10000},
]


# TODO 1: Ubah route '/' di bawah supaya:
#   - Tidak lagi me-return teks polos
#   - me-return render_template('index.html', data=transaksi)
#     ("data" adalah nama variabel yang bisa dipakai nanti di HTML)
# Pola:
#   @app.route('/')
#   def index():
#       return render_template('index.html', data=transaksi)

@app.route('/')
def index():
    return "TODO: ganti baris ini dengan render_template"


app.run(debug=True)
