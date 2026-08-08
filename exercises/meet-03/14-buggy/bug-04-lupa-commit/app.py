# app.py
# Bug: Lupa commit()

# ============================================================
# MISI KAMU
# ============================================================
# Isi form di bawah, klik Simpan. Halaman kembali ke daftar dengan
# lancar, TANPA pesan error apa pun — tapi transaksi barumu TIDAK
# PERNAH muncul di daftar, walau baru saja disimpan.
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
    nominal = request.form['nominal']
    db = get_db()
    db.execute(
        "INSERT INTO transactions (nama, nominal) VALUES (?, ?)",
        (nama, nominal)
    )
    return redirect('/')


app.run(debug=True)

# ---- Petunjuk ----
# get_db() membuka koneksi BARU setiap dipanggil — route tambah()
# dan route index() punya koneksinya masing-masing, terpisah sama
# sekali. Perubahan yang belum "dikunci" di satu koneksi TIDAK
# terlihat oleh koneksi lain, walau ke database yang sama persis.
# Bandingkan route tambah() ini dengan pola get_db()+execute()+???
# di folder-folder sebelumnya (06-11) — ada satu baris yang hilang.
