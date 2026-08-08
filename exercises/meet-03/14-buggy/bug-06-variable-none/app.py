# app.py
# Bug: Variabel None Tidak Dicek

# ============================================================
# MISI KAMU
# ============================================================
# Buka /detail/1 — kalau id=1 memang ada di database, halaman
# tampil normal.
#
# Tapi buka /detail/999 (id yang TIDAK ada), muncul error "500
# Internal Server Error" — "'NoneType' object is not subscriptable"
# alih-alih pesan "transaksi tidak ditemukan" yang ramah.
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
    # Buka alamat ini sekali dulu supaya id=1 tersedia untuk dicoba.
    db = get_db()
    db.execute("INSERT INTO transactions (nama, nominal) VALUES (?, ?)", ("Kopi", 25000))
    db.commit()
    return redirect('/detail/1')


@app.route('/detail/<int:id>')
def detail(id):
    db = get_db()
    item = db.execute(
        "SELECT * FROM transactions WHERE id = ?", (id,)
    ).fetchone()

    # BUG-nya ada tepat di baris ini:
    print("Menampilkan detail untuk:", item['nama'])

    return render_template('detail.html', item=item)


app.run(debug=True)

# ---- Petunjuk ----
# .fetchone() TIDAK SELALU menemukan barisnya — kalau id tidak ada
# di tabel, hasilnya None. Apa yang terjadi kalau kode mencoba
# membaca item['nama'] padahal item itu sendiri adalah None?
#
# (Catatan: di dalam kode Python biasa, isi Row HANYA bisa diambil
# lewat item['nama'] atau item[0] — beda dengan di dalam file HTML/
# Jinja yang boleh memakai item.nama. Jinja punya kemudahan khusus
# ini, Python murni tidak.)
