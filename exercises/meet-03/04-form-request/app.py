# app.py
# Topik: Form & Request — Menerima Data dari Pengunjung

# ============================================================
# MISI KAMU
# ============================================================
# Sampai sekarang data (transaksi) hanya kita TULIS MANUAL di
# app.py. Sekarang giliran PENGUNJUNG yang mengisi datanya sendiri
# lewat form HTML — dan Python menangkapnya lewat objek `request`.
#
# Peringatan jujur: data baru di latihan ini masih hilang tiap kali
# server di-restart, karena masih tersimpan di memori (list Python),
# BUKAN di database. Itu sengaja — supaya kamu betul-betul merasakan
# masalahnya sebelum kita pindah ke SQLite di 05-sqlite-basic.

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

transaksi = [
    {'nama': 'Kopi pagi', 'nominal': 25000},
    {'nama': 'Makan siang', 'nominal': 35000},
]


@app.route('/')
def index():
    return render_template('index.html', data=transaksi)


# TODO 1: Buat route '/tambah' yang menerima method POST, dengan
# function bernama tambah() yang:
#   1. Mengambil 'nama' dan 'nominal' dari request.form
#   2. Menambahkannya ke list transaksi lewat transaksi.append({...})
#   3. Redirect kembali ke '/' supaya user melihat daftar terbaru
#
# Pola:
#   @app.route('/tambah', methods=['POST'])
#   def tambah():
#       nama = request.form['nama']
#       nominal = request.form['nominal']
#       transaksi.append({'nama': nama, 'nominal': nominal})
#       return redirect('/')


app.run(debug=True)
