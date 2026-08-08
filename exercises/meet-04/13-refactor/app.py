# app.py
# PERINGATAN: file ini SENGAJA ditulis berantakan untuk latihan refactor.
# Semua fitur di sini BEKERJA dengan benar — tugasmu bukan memperbaiki bug,
# tapi merapikan strukturnya. Baca README.md di folder ini untuk instruksi.

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "practice-secret-key"


def get_db():
    conn = sqlite3.connect("expenses.db")
    conn.row_factory = sqlite3.Row
    return conn


conn = get_db()
conn.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        title      TEXT    NOT NULL,
        amount     REAL    NOT NULL,
        category   TEXT    NOT NULL DEFAULT 'Other',
        created_at TEXT    NOT NULL DEFAULT (datetime('now', 'localtime'))
    )
""")
conn.commit()
conn.close()


@app.route("/")
def index():
    search = request.args.get("search", "")
    category = request.args.get("category", "")
    conn = get_db()
    query = "SELECT * FROM expenses"
    conditions = []
    params = []
    if search:
        conditions.append("title LIKE ?")
        params.append("%" + search + "%")
    if category:
        conditions.append("category = ?")
        params.append(category)
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " ORDER BY created_at DESC"
    expenses = conn.execute(query, params).fetchall()
    total_row = conn.execute("SELECT COALESCE(SUM(amount), 0) AS total FROM expenses").fetchone()
    total = total_row["total"]
    conn.close()
    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        search=search,
        category=category,
        categories=["Food", "Transport", "Bills", "Entertainment", "Other"],
    )


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        amount_raw = request.form.get("amount", "").strip()
        category = request.form.get("category", "").strip()

        if not title:
            flash("Title wajib diisi.")
            return render_template("create.html", categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data=request.form)

        if not amount_raw:
            flash("Amount wajib diisi.")
            return render_template("create.html", categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data=request.form)

        try:
            amount = float(amount_raw)
        except ValueError:
            flash("Amount harus berupa angka.")
            return render_template("create.html", categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data=request.form)

        if amount <= 0.01:
            flash("Amount harus lebih besar dari 0.")
            return render_template("create.html", categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data=request.form)

        if amount > 999999999.99:
            flash("Amount terlalu besar.")
            return render_template("create.html", categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data=request.form)

        if category not in ["Food", "Transport", "Bills", "Entertainment", "Other"]:
            category = "Other"

        conn = get_db()
        conn.execute(
            "INSERT INTO expenses (title, amount, category) VALUES (?, ?, ?)",
            (title, amount, category)
        )
        conn.commit()
        conn.close()
        flash("Expense berhasil ditambahkan.")
        return redirect(url_for("index"))

    return render_template("create.html", categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data={})


@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit(expense_id):
    conn = get_db()
    expense = conn.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,)).fetchone()
    conn.close()

    if expense is None:
        flash("Expense tidak ditemukan.")
        return redirect(url_for("index"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        amount_raw = request.form.get("amount", "").strip()
        category = request.form.get("category", "").strip()

        if not title:
            flash("Title wajib diisi.")
            return render_template("edit.html", expense=expense, categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data=request.form)

        if not amount_raw:
            flash("Amount wajib diisi.")
            return render_template("edit.html", expense=expense, categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data=request.form)

        try:
            amount = float(amount_raw)
        except ValueError:
            flash("Amount harus berupa angka.")
            return render_template("edit.html", expense=expense, categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data=request.form)

        if amount <= 0.01:
            flash("Amount harus lebih besar dari 0.")
            return render_template("edit.html", expense=expense, categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data=request.form)

        if amount > 999999999.99:
            flash("Amount terlalu besar.")
            return render_template("edit.html", expense=expense, categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data=request.form)

        if category not in ["Food", "Transport", "Bills", "Entertainment", "Other"]:
            category = "Other"

        conn = get_db()
        conn.execute(
            "UPDATE expenses SET title = ?, amount = ?, category = ? WHERE id = ?",
            (title, amount, category, expense_id)
        )
        conn.commit()
        conn.close()
        flash("Expense berhasil diubah.")
        return redirect(url_for("index"))

    return render_template("edit.html", expense=expense, categories=["Food", "Transport", "Bills", "Entertainment", "Other"], form_data=expense)


@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete(expense_id):
    conn = get_db()
    conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    flash("Expense berhasil dihapus.")
    return redirect(url_for("index"))


app.run(debug=True)
