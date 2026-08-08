# contoh_debug.py
# Topik: Jurus Mengintip — print() sebagai Senter Kode

# ============================================================
# TIDAK ADA TODO DI FILE INI
# ============================================================
# File ini contoh SIAP JALAN yang menunjukkan trik paling sederhana
# untuk debugging: print(). Jalankan filenya, baca outputnya di
# terminal, lalu baca kodenya sambil mencocokkan.
#
#   python contoh_debug.py

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

    # SENTER 1: cek berapa banyak baris yang berhasil diambil.
    print("cek: jumlah transaksi =", len(data))

    return render_template('index.html', data=data)


@app.route('/tambah', methods=['POST'])
def tambah():
    nama = request.form['nama']
    nominal = request.form['nominal']

    # SENTER 2: cek isi variabel SEBELUM dipakai ke query. Ini yang
    # paling sering dilakukan programmer beneran saat curiga ada
    # yang salah — bukan menebak, tapi MELIHAT langsung isinya.
    print("cek: nama =", nama, "| nominal =", nominal, "| tipe nominal =", type(nominal))

    db = get_db()
    db.execute(
        "INSERT INTO transactions (nama, nominal) VALUES (?, ?)",
        (nama, nominal)
    )
    db.commit()
    return redirect('/')


app.run(debug=True)

# ============================================================
# COBA INI
# ============================================================
# 1. Jalankan aplikasi, buka localhost:5000, tambah satu transaksi.
# 2. Lihat kembali TERMINAL (bukan browser) — ada dua baris "cek:"
#    yang muncul di sana. Browser tidak pernah menampilkan print(),
#    hanya terminal tempat "python contoh_debug.py" dijalankan.
# 3. Perhatikan baris kedua: nominal punya "tipe" str (teks), bukan
#    int (angka) — walau kamu mengetik angka di form. Ini karena
#    SEMUA isi request.form selalu berbentuk teks. Kalau butuh
#    operasi matematika (>, <, +), ubah dulu pakai int(...) atau
#    float(...).
