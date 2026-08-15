"""Validasi data dan query SQL untuk setiap fitur Expense Tracker."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from database import db


CATEGORIES = [
    "Food",
    "Transportation",
    "Shopping",
    "Bills",
    "Entertainment",
    "Education",
    "Other",
]

def get_categories() -> list[str]:
    return CATEGORIES


# CREATE — dipanggil oleh POST /create
def create_expense(form_data: dict) -> dict:
    data = validate_expense(form_data)

    query = """
        INSERT INTO expenses (title, amount, category, notes)
        VALUES (%s, %s, %s, %s)
    """
    params = (data["title"], data["amount"], data["category"], data["notes"])

    result = db.execute(query, params)
    return get_expense_by_id(result["lastrowid"])


# READ — dipanggil oleh GET /expenses
def get_expenses(
    search: str = "",
    category: str = "",
    sort_by: str = "created_at",
    order: str = "desc",
) -> list[dict]:
    # Nama column tidak dapat dikirim melalui %s. Karena itu pilihan sort
    # dibatasi menggunakan allowlist sebelum dimasukkan ke query.
    allowed_sorts = {"title", "amount", "category", "created_at"}
    safe_sort = sort_by if sort_by in allowed_sorts else "created_at"
    safe_order = "ASC" if order.lower() == "asc" else "DESC"

    conditions = []
    params = []

    if search:
        conditions.append("(title LIKE %s OR notes LIKE %s)")
        params.extend([f"%{search}%", f"%{search}%"])
    if category:
        conditions.append("category = %s")
        params.append(category)

    where = "WHERE " + " AND ".join(conditions) if conditions else ""
    query = f"""
        SELECT id, title, amount, category, notes, created_at, updated_at
        FROM expenses
        {where}
        ORDER BY {safe_sort} {safe_order}
    """

    rows = db.execute(query, params, fetch="all")
    return [format_expense(row) for row in rows]


# READ ONE — dipanggil sebelum edit/delete dan setelah create/update
def get_expense_by_id(expense_id: int) -> dict | None:
    query = """
        SELECT id, title, amount, category, notes, created_at, updated_at
        FROM expenses
        WHERE id = %s
    """
    row = db.execute(query, (expense_id,), fetch="one")
    return format_expense(row) if row else None


# UPDATE — dipanggil oleh POST /edit/<id>
def update_expense(expense_id: int, form_data: dict) -> dict | None:
    data = validate_expense(form_data)

    query = """
        UPDATE expenses
        SET title = %s, amount = %s, category = %s, notes = %s
        WHERE id = %s
    """
    params = (
        data["title"],
        data["amount"],
        data["category"],
        data["notes"],
        expense_id,
    )

    db.execute(query, params)
    return get_expense_by_id(expense_id)


# DELETE — dipanggil oleh POST /delete/<id>
def delete_expense(expense_id: int) -> bool:
    query = "DELETE FROM expenses WHERE id = %s"
    result = db.execute(query, (expense_id,))
    return result["rowcount"] > 0


# READ untuk lima transaksi terbaru di dashboard
def get_recent_expenses(limit: int = 5) -> list[dict]:
    query = """
        SELECT id, title, amount, category, notes, created_at, updated_at
        FROM expenses
        ORDER BY created_at DESC
        LIMIT %s
    """
    rows = db.execute(query, (int(limit),), fetch="all")
    return [format_expense(row) for row in rows]


# READ ringkasan dashboard. SUM, COUNT, dan AVG cukup dalam satu query.
def get_summary() -> dict:
    query = """
        SELECT
            COALESCE(SUM(amount), 0) AS total_amount,
            COUNT(*) AS expense_count,
            COALESCE(AVG(amount), 0) AS average_amount
        FROM expenses
    """
    row = db.execute(query, fetch="one")

    return {
        "total_amount": row["total_amount"],
        "formatted_total": format_currency(row["total_amount"]),
        "expense_count": row["expense_count"],
        "average_amount": format_currency(row["average_amount"]),
    }


# READ total setiap kategori untuk dashboard dan halaman summary.
def get_category_totals() -> list[dict]:
    query = """
        SELECT
            category,
            SUM(amount) AS total_amount,
            COUNT(*) AS expense_count
        FROM expenses
        GROUP BY category
        ORDER BY total_amount DESC
    """
    rows = db.execute(query, fetch="all")
    grand_total = sum((row["total_amount"] for row in rows), Decimal("0"))

    for row in rows:
        percentage = (
            row["total_amount"] / grand_total * Decimal("100")
            if grand_total > 0
            else Decimal("0")
        )
        row["formatted_amount"] = format_currency(row["total_amount"])
        row["percentage"] = round(percentage, 1)

    return rows


def validate_expense(form_data: dict) -> dict:
    """Bersihkan input form dan hentikan proses jika datanya tidak valid."""
    title = form_data.get("title", "").strip()
    amount_text = form_data.get("amount", "").strip()
    category = form_data.get("category", "").strip()
    notes = form_data.get("notes", "").strip()

    if not title:
        raise ValueError("Title is required.")
    if len(title) > 200:
        raise ValueError("Title must be 200 characters or less.")

    try:
        amount = Decimal(amount_text)
    except InvalidOperation:
        raise ValueError("Amount must be a valid number.")

    if not amount.is_finite() or amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if category not in CATEGORIES:
        raise ValueError("Please select a valid category.")
    if len(notes) > 1000:
        raise ValueError("Notes must be 1000 characters or less.")

    return {
        "title": title,
        "amount": amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        "category": category,
        "notes": notes,
    }


def format_expense(expense: dict) -> dict:
    """Tambahkan nilai siap tampil tanpa mengubah data asli dari MySQL."""
    notes = expense.get("notes", "")
    return {
        **expense,
        "formatted_amount": format_currency(expense["amount"]),
        "short_notes": notes if len(notes) <= 60 else notes[:60].rstrip() + "...",
    }


def format_currency(amount: Decimal) -> str:
    return f"{amount:,.2f}"
