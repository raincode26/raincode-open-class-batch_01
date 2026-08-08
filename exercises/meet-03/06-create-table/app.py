# app.py
# Topik: Create Table — Menyiapkan Gudang Sebelum Mengisi Barang

# ============================================================
# MISI KAMU
# ============================================================
# Mulai folder ini, Expense Tracker kita pindah dari "data sementara
# di memori" (list Python) ke SQLITE SUNGGUHAN. Tugas pertama sebelum
# CRUD bisa jalan: siapkan dulu tabelnya.
#
# get_db() di bawah ini SUDAH LENGKAP — pola yang sama akan dipakai
# di SETIAP route mulai sekarang. Baca dulu supaya paham, baru
# kerjakan TODO-nya.

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_db():
    """Buka koneksi baru ke database, siap dipakai satu route."""
    db = sqlite3.connect('expense_tracker.db')
    db.row_factory = sqlite3.Row  # hasil bisa diakses via nama kolom, mis. row['nama']
    return db


# TODO 1: Buat function init_db() yang membuat tabel "transactions"
# KALAU BELUM ADA (IF NOT EXISTS), dengan kolom:
#   id       INTEGER PRIMARY KEY AUTOINCREMENT
#   nama     TEXT NOT NULL
#   nominal  INTEGER NOT NULL
# Jangan lupa commit() di akhir supaya tabelnya benar-benar dibuat.
#
# Pola:
#   def init_db():
#       db = get_db()
#       db.execute("""
#           CREATE TABLE IF NOT EXISTS transactions (
#               id INTEGER PRIMARY KEY AUTOINCREMENT,
#               nama TEXT NOT NULL,
#               nominal INTEGER NOT NULL
#           )
#       """)
#       db.commit()


# TODO 2: Panggil init_db() SATU KALI di sini (bukan di dalam route),
# supaya tabelnya sudah siap begitu aplikasi pertama kali dinyalakan
# — sebelum ada satu permintaan (request) pun yang masuk.


@app.route('/')
def index():
    # Tabel pasti ada (walau masih kosong) berkat init_db() di atas.
    data = get_db().execute("SELECT * FROM transactions").fetchall()
    return render_template('index.html', data=data)


app.run(debug=True)
