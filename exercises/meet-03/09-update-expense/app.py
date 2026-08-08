# app.py
# Topik: Update — Mengedit Transaksi (UPDATE)

# ============================================================
# MISI KAMU
# ============================================================
# "Kopi pagi" ternyata Rp 30.000, bukan Rp 25.000. Kita perlu
# mengubah BARIS YANG SUDAH ADA — bukan menambah baris baru.
#
# Route '/edit/<int:id>' di bawah ini menangani DUA hal sekaligus:
#   GET  -> tampilkan form edit, TERISI data yang sekarang
#   POST -> proses perubahan yang dikirim lewat form itu
#
# Pola GET/POST dalam satu route ini persis seperti yang dipakai di
# project nyata (lihat nanti di 12-read-source-code).

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
    db.commit()
    return redirect('/')


@app.route('/detail/<int:id>')
def detail(id):
    db = get_db()
    item = db.execute(
        "SELECT * FROM transactions WHERE id = ?", (id,)
    ).fetchone()
    return render_template('detail.html', item=item)


# TODO 1: Buat route '/edit/<int:id>' yang menerima methods GET & POST,
# dengan function edit(id) yang:
#
#   Kalau method == 'POST':
#     1. Ambil 'nama' dan 'nominal' baru dari request.form
#     2. UPDATE transactions SET nama=?, nominal=? WHERE id=?
#        (perhatikan urutan tanda tanya HARUS cocok dengan urutan nilai!)
#     3. commit()
#     4. redirect ke '/'
#
#   Kalau method == 'GET' (default, bukan POST):
#     1. Ambil data lama lewat SELECT ... WHERE id = ? + fetchone()
#        (sama seperti route detail())
#     2. render_template('edit.html', item=<data lama>)
#
# Pola:
#   @app.route('/edit/<int:id>', methods=['GET', 'POST'])
#   def edit(id):
#       db = get_db()
#       if request.method == 'POST':
#           nama = request.form['nama']
#           nominal = request.form['nominal']
#           db.execute(
#               "UPDATE transactions SET nama = ?, nominal = ? WHERE id = ?",
#               (nama, nominal, id)
#           )
#           db.commit()
#           return redirect('/')
#       else:
#           item = db.execute(
#               "SELECT * FROM transactions WHERE id = ?", (id,)
#           ).fetchone()
#           return render_template('edit.html', item=item)
#
# AWAS: DELETE FROM tanpa WHERE menghapus SEMUA baris; UPDATE tanpa
# WHERE mengubah SEMUA baris. Jangan sampai id-nya lupa disertakan!


app.run(debug=True)
