# app.py
# Challenge Hard — Ringkasan Harian + Total Pengeluaran
# Starter ini SUDAH LENGKAP (hasil dari 11-complete-crud) — tugasmu
# ada di route baru '/ringkasan'. Baca README.md untuk spesifikasinya.

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
            nominal INTEGER NOT NULL,
            kategori TEXT NOT NULL DEFAULT 'Lainnya',
            tanggal TEXT
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
    kategori = request.form['kategori']
    tanggal = request.form['tanggal']
    db = get_db()
    db.execute(
        "INSERT INTO transactions (nama, nominal, kategori, tanggal) VALUES (?, ?, ?, ?)",
        (nama, nominal, kategori, tanggal)
    )
    db.commit()
    return redirect('/')


@app.route('/hapus/<int:id>')
def hapus(id):
    db = get_db()
    db.execute("DELETE FROM transactions WHERE id = ?", (id,))
    db.commit()
    return redirect('/')


# TODO 1: Buat route '/ringkasan' dengan function ringkasan() yang
# menampilkan DUA hal:
#
#   A. Total SELURUH pengeluaran (satu angka), pakai SQL SUM():
#        SELECT SUM(nominal) AS total FROM transactions
#      Hasilnya SATU baris — pakai .fetchone(), lalu ambil lewat
#      row['total'] (bisa None kalau tabel masih kosong! cek dulu).
#
#   B. Total pengeluaran PER TANGGAL, pakai SQL GROUP BY:
#        SELECT tanggal, SUM(nominal) AS total_harian
#        FROM transactions
#        GROUP BY tanggal
#        ORDER BY tanggal DESC
#      Hasilnya BANYAK baris (satu per tanggal) — pakai .fetchall().
#
# Lalu render_template('ringkasan.html', total=..., per_tanggal=...)
#
# Pola:
#   @app.route('/ringkasan')
#   def ringkasan():
#       db = get_db()
#       total_row = db.execute("SELECT SUM(nominal) AS total FROM transactions").fetchone()
#       total = total_row['total'] or 0  # "or 0" -> kalau None (tabel kosong), jadi 0
#       per_tanggal = db.execute("""
#           SELECT tanggal, SUM(nominal) AS total_harian
#           FROM transactions
#           GROUP BY tanggal
#           ORDER BY tanggal DESC
#       """).fetchall()
#       return render_template('ringkasan.html', total=total, per_tanggal=per_tanggal)


app.run(debug=True)
