# service.py
# Logika & aturan bisnis — validasi hidup di sini, bukan di route atau repository.

from repository import (
    get_all_expenses, get_expense_by_id, create_expense,
    update_expense, delete_expense, get_total
)

CATEGORIES = ["Food", "Transport", "Bills", "Entertainment", "Other"]


def list_expenses(search=None, category=None):
    return get_all_expenses(search=search, category=category)


def get_expense(expense_id):
    return get_expense_by_id(expense_id)


def add_expense(form_data):
    cleaned = _validate(form_data)
    create_expense(cleaned["title"], cleaned["amount"], cleaned["category"])


def edit_expense(expense_id, form_data):
    cleaned = _validate(form_data)
    update_expense(expense_id, cleaned["title"], cleaned["amount"], cleaned["category"])


def remove_expense(expense_id):
    delete_expense(expense_id)


def get_grand_total():
    return get_total()


def _validate(form_data):
    title = form_data.get("title", "").strip()
    amount_raw = form_data.get("amount", "").strip()
    category = form_data.get("category", "").strip()

    if not title:
        raise ValueError("Title wajib diisi.")

    if not amount_raw:
        raise ValueError("Amount wajib diisi.")

    try:
        amount = float(amount_raw)
    except ValueError:
        raise ValueError("Amount harus berupa angka.")

    if amount <= 0:
        raise ValueError("Amount harus lebih besar dari 0.")

    if category not in CATEGORIES:
        category = "Other"

    return {"title": title, "amount": amount, "category": category}
