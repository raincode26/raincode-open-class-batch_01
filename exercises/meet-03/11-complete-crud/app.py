# app.py
# Topik: Complete CRUD — Merapikan Semuanya + Level Up

# ============================================================
# MISI KAMU
# ============================================================
# CRUD-mu sudah LENGKAP sejak 10-delete-expense (Create, Read,
# Update, Delete semua jalan).
#
# Folder ini punya dua bagian:
#   BAGIAN A — semua CRUD dari 06-10, SUDAH LENGKAP, tinggal dibaca
#              ulang sebagai rangkuman.
#   BAGIAN B — "Level Up": tambah kolom kategori & tanggal, persis
#              seperti Latihan 05 & 06 di modul. Ini bagian TODO-mu.

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db():
    db = sqlite3.connect('expense_tracker.db')
    db.row_factory = sqlite3.Row
    return db


def init_db():
    db = get_db()
    # TODO 1: Tambahkan DUA kolom baru ke CREATE TABLE di bawah ini:
    #   kategori  TEXT NOT NULL DEFAULT 'Lainnya'
    #   tanggal   TEXT
    # (tulis di antara "nominal INTEGER NOT NULL," dan tanda kurung
    # tutup ")"). Ingat: ini tabel yang BARU akan dibuat pertama kali
    # (belum ada datanya), jadi cukup ubah CREATE TABLE-nya langsung
    # — tidak perlu ALTER TABLE untuk latihan ini.
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
    data = get_db().execute(
        "SELECT * FROM transactions ORDER BY id DESC"
    ).fetchall()
    return render_template('index.html', data=data)


@app.route('/tambah', methods=['POST'])
def tambah():
    nama = request.form['nama']
    nominal = request.form['nominal']

    # TODO 2: Ambil juga 'kategori' dan 'tanggal' dari request.form,
    # lalu sertakan keduanya di query INSERT (jadi ada 4 kolom & 4
    # placeholder "?" sekarang, bukan 2).
    # Pola:
    #   kategori = request.form['kategori']
    #   tanggal = request.form['tanggal']
    #   db.execute(
    #       "INSERT INTO transactions (nama, nominal, kategori, tanggal) "
    #       "VALUES (?, ?, ?, ?)",
    #       (nama, nominal, kategori, tanggal)
    #   )

    db = get_db()
    db.execute(
        "INSERT INTO transactions (nama, nominal) VALUES (?, ?)",
        (nama, nominal)
    )
    db.commit()
    return redirect('/')


@app.route('/detail/<int:id>')
def detail(id):
    db = get_db()
    item = db.execute(
        "SELECT * FROM transactions WHERE id = ?", (id,)
    ).fetchone()
    return render_template('detail.html', item=item)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    db = get_db()
    if request.method == 'POST':
        nama = request.form['nama']
        nominal = request.form['nominal']

        # TODO 3: Sama seperti TODO 2, ambil & sertakan 'kategori'
        # dan 'tanggal' juga di query UPDATE.
        # Pola:
        #   kategori = request.form['kategori']
        #   tanggal = request.form['tanggal']
        #   db.execute(
        #       "UPDATE transactions "
        #       "SET nama=?, nominal=?, kategori=?, tanggal=? WHERE id=?",
        #       (nama, nominal, kategori, tanggal, id)
        #   )

        db.execute(
            "UPDATE transactions SET nama = ?, nominal = ? WHERE id = ?",
            (nama, nominal, id)
        )
        db.commit()
        return redirect('/')
    else:
        item = db.execute(
            "SELECT * FROM transactions WHERE id = ?", (id,)
        ).fetchone()
        return render_template('edit.html', item=item)


@app.route('/hapus/<int:id>')
def hapus(id):
    db = get_db()
    db.execute("DELETE FROM transactions WHERE id = ?", (id,))
    db.commit()
    return redirect('/')


app.run(debug=True)
