# app.py
# Challenge Medium — Filter Kategori
# Starter ini SUDAH LENGKAP (hasil dari 11-complete-crud) — tugasmu
# ada di route index(). Baca README.md untuk spesifikasinya.

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


# TODO 1: Ubah route index() supaya bisa memfilter berdasarkan
# kategori lewat query string di URL, contoh: /?kategori=Makanan
#
#   1. Ambil kategori pilihan lewat request.args.get('kategori')
#      (pakai .get() supaya aman kalau tidak ada filter sama sekali
#      — hasilnya None, bukan error)
#   2. Kalau kategori TERISI (bukan None/kosong), tambahkan
#      "WHERE kategori = ?" ke query SELECT
#   3. Kalau kategori KOSONG (user memilih "Semua Kategori"),
#      tampilkan semua transaksi seperti biasa
#
# Pola:
#   @app.route('/')
#   def index():
#       kategori_filter = request.args.get('kategori')
#       db = get_db()
#       if kategori_filter:
#           data = db.execute(
#               "SELECT * FROM transactions WHERE kategori = ? ORDER BY id DESC",
#               (kategori_filter,)
#           ).fetchall()
#       else:
#           data = db.execute(
#               "SELECT * FROM transactions ORDER BY id DESC"
#           ).fetchall()
#       return render_template('index.html', data=data, kategori_filter=kategori_filter)

@app.route('/')
def index():
    data = get_db().execute(
        "SELECT * FROM transactions ORDER BY id DESC"
    ).fetchall()
    return render_template('index.html', data=data, kategori_filter=None)


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


app.run(debug=True)
