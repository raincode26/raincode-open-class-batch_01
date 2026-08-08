# app.py
# Route layer — menerima request, memanggil service, mengirim response.

from flask import Flask, render_template, request, redirect, url_for, flash
import service
import database

app = Flask(__name__)
app.secret_key = "practice-secret-key"

database.init_db()


@app.route("/")
def index():
    search = request.args.get("search", "")
    category = request.args.get("category", "")
    expenses = service.list_expenses(search=search or None, category=category or None)
    total = service.get_grand_total()
    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        search=search,
        category=category,
        categories=service.CATEGORIES,
    )


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        try:
            service.add_expense(request.form)
            flash("Expense berhasil ditambahkan.")
            return redirect(url_for("index"))
        except ValueError as e:
            flash(str(e))
            return render_template("create.html", categories=service.CATEGORIES, form_data=request.form)
    return render_template("create.html", categories=service.CATEGORIES, form_data={})


@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit(expense_id):
    expense = service.get_expense(expense_id)
    print("Editing expense:", expense["title"])

    if request.method == "POST":
        try:
            service.edit_expense(expense_id, request.form)
            flash("Expense berhasil diubah.")
            return redirect(url_for("index"))
        except ValueError as e:
            flash(str(e))
            return render_template("edit.html", expense=expense, categories=service.CATEGORIES, form_data=request.form)

    return render_template("edit.html", expense=expense, categories=service.CATEGORIES, form_data=expense)


@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete(expense_id):
    service.remove_expense(expense_id)
    flash("Expense berhasil dihapus.")
    return redirect(url_for("index"))


app.run(debug=True)
