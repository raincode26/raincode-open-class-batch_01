# app.py
# Solusi Challenge Medium — Filter Kategori

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
    kategori_filter = request.args.get('kategori')
    db = get_db()

    if kategori_filter:
        data = db.execute(
            "SELECT * FROM transactions WHERE kategori = ? ORDER BY id DESC",
            (kategori_filter,)
        ).fetchall()
    else:
        data = db.execute(
            "SELECT * FROM transactions ORDER BY id DESC"
        ).fetchall()

    return render_template('index.html', data=data, kategori_filter=kategori_filter)


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
