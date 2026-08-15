"""Route Flask: menerima request, memanggil service, lalu mengirim response."""

from flask import Flask, flash, redirect, render_template, request, url_for

from config import config
from database.db import init_db
from services import expense_service as service


app = Flask(__name__)
app.secret_key = config.SECRET_KEY

# Database harus sudah dibuat. Aplikasi hanya memastikan table tersedia.
init_db()


def read_expense_form() -> dict:
    """Ambil empat field yang dipakai form create dan edit."""
    return {
        "title": request.form.get("title", "").strip(),
        "amount": request.form.get("amount", "").strip(),
        "category": request.form.get("category", "").strip(),
        "notes": request.form.get("notes", "").strip(),
    }


@app.get("/")
def index():
    """Dashboard: summary, transaksi terbaru, dan total per kategori."""
    try:
        return render_template(
            "index.html",
            page_title="Dashboard",
            summary=service.get_summary(),
            recent_expenses=service.get_recent_expenses(
                config.RECENT_EXPENSES_LIMIT
            ),
            category_totals=service.get_category_totals(),
        )
    except Exception:
        app.logger.exception("Could not load dashboard")
        flash("Could not load the dashboard.", "error")
        return render_template(
            "index.html",
            page_title="Dashboard",
            summary={},
            recent_expenses=[],
            category_totals=[],
        )


@app.get("/expenses")
def expenses():
    """READ: tampilkan transaksi dengan search, filter, dan sort."""
    search = request.args.get("search", "").strip()
    category = request.args.get("category", "").strip()
    sort_by = request.args.get("sort", "created_at").strip()
    order = request.args.get("order", "desc").strip()

    try:
        rows = service.get_expenses(search, category, sort_by, order)
        return render_template(
            "expenses.html",
            page_title="Expenses",
            expenses=rows,
            categories=service.get_categories(),
            search=search,
            selected_category=category,
            sort_by=sort_by,
            order=order,
        )
    except Exception:
        app.logger.exception("Could not load expenses")
        flash("Could not load expenses.", "error")
        return redirect(url_for("index"))


@app.route("/create", methods=["GET", "POST"])
def create():
    """GET menampilkan form; POST memvalidasi dan menjalankan INSERT."""
    form_data = {}

    if request.method == "POST":
        form_data = read_expense_form()
        try:
            expense = service.create_expense(form_data)
            flash(f"Expense '{expense['title']}' created successfully!", "success")
            return redirect(url_for("expenses"))
        except ValueError as error:
            flash(str(error), "error")
        except Exception:
            app.logger.exception("Could not create expense")
            flash("Could not create the expense.", "error")

    return render_template(
        "create.html",
        page_title="Create Expense",
        categories=service.get_categories(),
        form_data=form_data,
    )


@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit(expense_id: int):
    """GET menampilkan data lama; POST menjalankan UPDATE berdasarkan ID."""
    try:
        expense = service.get_expense_by_id(expense_id)
    except Exception:
        app.logger.exception("Could not find expense %s", expense_id)
        flash("Could not load the expense.", "error")
        return redirect(url_for("expenses"))

    if expense is None:
        flash("Expense not found.", "error")
        return redirect(url_for("expenses"))

    form_data = expense
    if request.method == "POST":
        form_data = read_expense_form()
        try:
            updated = service.update_expense(expense_id, form_data)
            flash(f"Expense '{updated['title']}' updated successfully!", "success")
            return redirect(url_for("expenses"))
        except ValueError as error:
            flash(str(error), "error")
        except Exception:
            app.logger.exception("Could not update expense %s", expense_id)
            flash("Could not update the expense.", "error")

    return render_template(
        "edit.html",
        page_title="Edit Expense",
        expense=expense,
        categories=service.get_categories(),
        form_data=form_data,
    )


@app.post("/delete/<int:expense_id>")
def delete(expense_id: int):
    """DELETE berdasarkan ID, dipanggil melalui form POST."""
    try:
        expense = service.get_expense_by_id(expense_id)
        if expense is None:
            flash("Expense not found.", "error")
        elif service.delete_expense(expense_id):
            flash(f"Expense '{expense['title']}' deleted successfully.", "success")
    except Exception:
        app.logger.exception("Could not delete expense %s", expense_id)
        flash("Could not delete the expense.", "error")

    return redirect(url_for("expenses"))


@app.get("/summary")
def summary():
    """Tampilkan aggregate total dan breakdown kategori."""
    try:
        return render_template(
            "summary.html",
            page_title="Summary",
            category_totals=service.get_category_totals(),
            summary=service.get_summary(),
        )
    except Exception:
        app.logger.exception("Could not load summary")
        flash("Could not load the summary.", "error")
        return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(_error):
    return render_template("errors/404.html", page_title="Page Not Found"), 404


@app.errorhandler(500)
def internal_server_error(_error):
    return render_template("errors/500.html", page_title="Server Error"), 500


if __name__ == "__main__":
    app.run(debug=config.DEBUG)
