# app.py
# Topik: Read — Membaca Satu Data Spesifik (SELECT ... WHERE)

# ============================================================
# MISI KAMU
# ============================================================
# Kamu sudah diam-diam menguasai Read versi "ambil SEMUA data" sejak
# 06-create-table (lihat route index() di bawah — polanya sama).
#
# Read versi kedua yang BELUM kamu pakai: mengambil SATU baris
# spesifik lewat id-nya. Ini skill wajib sebelum bisa Update
# (09) & Delete (10) — keduanya butuh tahu "baris mana" yang dituju.

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db():
    db = sqlite3.connect('expense_tracker.db')
    db.row_factory = sqlite3.Row
    return db


def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            nominal INTEGER NOT NULL
        )
    """)
    db.commit()


init_db()


@app.route('/')
def index():
    # Read versi "ambil semua" — sudah kamu kenal sejak 06.
    data = get_db().execute("SELECT * FROM transactions").fetchall()
    return render_template('index.html', data=data)


@app.route('/tambah', methods=['POST'])
def tambah():
    nama = request.form['nama']
    nominal = request.form['nominal']
    db = get_db()
    db.execute(
        "INSERT INTO transactions (nama, nominal) VALUES (?, ?)",
        (nama, nominal)
    )
    db.commit()
    return redirect('/')


# TODO 1: Buat route '/detail/<int:id>' dengan function detail(id)
# yang:
#   1. Mengambil SATU baris dari transactions dengan id yang cocok
#      (pakai WHERE id = ? dan .fetchone(), BUKAN .fetchall())
#   2. me-render_template('detail.html', item=<hasilnya>)
#
# Pola:
#   @app.route('/detail/<int:id>')
#   def detail(id):
#       db = get_db()
#       item = db.execute(
#           "SELECT * FROM transactions WHERE id = ?", (id,)
#       ).fetchone()
#       return render_template('detail.html', item=item)
#
# Perhatikan: (id,) memakai koma di dalam kurung — itu cara Python
# menulis tuple berisi SATU elemen. Tanpa koma, (id) bukan tuple,
# cuma id yang dibungkus kurung biasa.


app.run(debug=True)
