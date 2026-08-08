# app.py
# Bug: request.form Typo

# ============================================================
# MISI KAMU
# ============================================================
# Isi form di bawah, klik Simpan.
#
# Tapi kalau dicoba, muncul halaman debugger Flask (500 Internal
# Server Error) yang menyebutkan "werkzeug.exceptions.
# BadRequestKeyError: 400 Bad Request" di bagian bawah traceback-nya.
#
# Cari tahu kenapa, lalu perbaiki.

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
    data = get_db().execute("SELECT * FROM transactions").fetchall()
    return render_template('index.html', data=data)


@app.route('/tambah', methods=['POST'])
def tambah():
    nama = request.form['nama']
    nominal = request.form['jumlah']
    db = get_db()
    db.execute(
        "INSERT INTO transactions (nama, nominal) VALUES (?, ?)",
        (nama, nominal)
    )
    db.commit()
    return redirect('/')


app.run(debug=True)

# ---- Petunjuk ----
# request.form['jumlah'] mencari sebuah <input> dengan atribut
# name="jumlah". Buka templates/index.html — apakah input nominal
# di sana benar-benar diberi name="jumlah"?
