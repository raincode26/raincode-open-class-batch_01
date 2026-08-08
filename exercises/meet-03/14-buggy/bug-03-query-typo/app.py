# app.py
# Bug: Query SQL Typo

# ============================================================
# MISI KAMU
# ============================================================
# Halaman ini seharusnya menampilkan transaksi dengan nominal di
# atas Rp 20.000.
#
# Tapi kalau dibuka, muncul error "sqlite3.OperationalError: no such
# column: nomial".
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


@app.route('/tambah-contoh')
def tambah_contoh():
    # Rute bantu supaya ada data untuk dicoba — buka alamat ini
    # sekali lewat browser sebelum membuka "/".
    db = get_db()
    db.execute("INSERT INTO transactions (nama, nominal) VALUES (?, ?)", ("Kopi", 25000))
    db.execute("INSERT INTO transactions (nama, nominal) VALUES (?, ?)", ("Parkir", 5000))
    db.commit()
    return redirect('/')


@app.route('/')
def index():
    data = get_db().execute(
        "SELECT * FROM transactions WHERE nomial > 20000"
    ).fetchall()
    return render_template('index.html', data=data)


app.run(debug=True)

# ---- Petunjuk ----
# Baca pesan error-nya persis kata per kata — Python biasanya
# menyebutkan nama kolom yang "tidak ditemukan". Bandingkan ejaan
# itu dengan nama kolom asli di CREATE TABLE.
