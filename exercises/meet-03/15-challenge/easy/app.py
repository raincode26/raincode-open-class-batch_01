# app.py
# Challenge Easy — Kategori Berwarna
# Starter ini SUDAH LENGKAP (hasil dari 11-complete-crud) — tugasmu
# murni di templates/index.html dan style.css. Baca README.md untuk
# spesifikasinya.

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


app.run(debug=True)
