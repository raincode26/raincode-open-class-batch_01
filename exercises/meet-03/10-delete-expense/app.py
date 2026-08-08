# app.py
# Topik: Delete — Menghapus Transaksi (DELETE)

# ============================================================
# MISI KAMU
# ============================================================
# Huruf terakhir CRUD: D - Delete. Polanya mirip sekali dengan
# detail() (08) — sama-sama pakai WHERE id = ? untuk menunjuk baris
# mana yang dimaksud. Bedanya, kali ini barisnya DIHAPUS, bukan
# ditampilkan.

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


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    db = get_db()
    if request.method == 'POST':
        nama = request.form['nama']
        nominal = request.form['nominal']
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


# TODO 1: Buat route '/hapus/<int:id>' dengan function hapus(id) yang:
#   1. DELETE FROM transactions WHERE id = ?
#   2. commit()
#   3. redirect ke '/'
#
# Pola:
#   @app.route('/hapus/<int:id>')
#   def hapus(id):
#       db = get_db()
#       db.execute("DELETE FROM transactions WHERE id = ?", (id,))
#       db.commit()
#       return redirect('/')
#
# AWAS: DELETE FROM transactions TANPA "WHERE id = ?" menghapus
# SELURUH isi tabel, bukan cuma satu baris. Selalu double-check!


app.run(debug=True)
