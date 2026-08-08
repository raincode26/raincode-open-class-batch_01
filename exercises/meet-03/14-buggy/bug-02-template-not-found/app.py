# app.py
# Bug: Template Tidak Ditemukan

# ============================================================
# MISI KAMU
# ============================================================
# Halaman ini seharusnya menampilkan daftar transaksi.
#
# Tapi kalau dibuka, muncul error "jinja2.exceptions.TemplateNotFound".
#
# Cari tahu kenapa, lalu perbaiki.

from flask import Flask, render_template
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
    return render_template('daftar.html', data=data)


app.run(debug=True)

# ---- Petunjuk ----
# Buka folder templates/ di folder ini. Ada file HTML di sana —
# tapi namanya apa persis? Bandingkan dengan nama file yang diminta
# oleh render_template(...) di atas.
