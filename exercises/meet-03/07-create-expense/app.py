# app.py
# Topik: Create — Menyimpan Pengeluaran Baru (INSERT)

# ============================================================
# MISI KAMU
# ============================================================
# Tabelnya sudah siap sejak 06-create-table. Sekarang giliran huruf
# pertama CRUD: C - Create. Form di templates/index.html sudah
# lengkap — tugasmu murni di sisi Python: tangkap datanya, INSERT ke
# database, commit, lalu redirect.

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


# TODO 1: Buat route '/tambah' (method POST) dengan function tambah()
# yang:
#   1. Mengambil 'nama' dan 'nominal' dari request.form
#   2. INSERT ke tabel transactions (pakai placeholder ?, BUKAN f-string!)
#   3. commit()
#   4. redirect kembali ke '/'
#
# Pola:
#   @app.route('/tambah', methods=['POST'])
#   def tambah():
#       nama = request.form['nama']
#       nominal = request.form['nominal']
#       db = get_db()
#       db.execute(
#           "INSERT INTO transactions (nama, nominal) VALUES (?, ?)",
#           (nama, nominal)
#       )
#       db.commit()
#       return redirect('/')


app.run(debug=True)
