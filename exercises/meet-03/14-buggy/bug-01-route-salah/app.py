# app.py
# Bug: Route Salah

# ============================================================
# MISI KAMU
# ============================================================
# Klik "Simpan" pada form di halaman ini seharusnya menyimpan
# transaksi baru dan kembali ke daftar.
#
# Tapi kalau dicoba, muncul halaman error "404 Not Found".
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


@app.route('/simpan-transaksi', methods=['POST'])
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


app.run(debug=True)

# ---- Petunjuk ----
# Bandingkan alamat "action" pada <form> di templates/index.html
# dengan alamat yang didaftarkan lewat @app.route(...) di file ini.
# Apakah keduanya menyebut alamat yang sama persis?
