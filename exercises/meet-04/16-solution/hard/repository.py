# repository.py
# Satu-satunya file yang menulis query SQL ke database.

from database import get_connection


def get_all_expenses(search=None, category=None):
    conn = get_connection()
    query = "SELECT * FROM expenses"
    conditions = []
    params = []

    if search:
        conditions.append("title LIKE ?")
        params.append(f"%{search}%")
    if category:
        conditions.append("category = ?")
        params.append(category)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " ORDER BY created_at DESC"

    rows = conn.execute(query, params).fetchall()
    conn.close()
    return rows


def get_expense_by_id(expense_id):
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM expenses WHERE id = ?", (expense_id,)
    ).fetchone()
    conn.close()
    return row


def create_expense(title, amount, category):
    conn = get_connection()
    conn.execute(
        "INSERT INTO expenses (title, amount, category) VALUES (?, ?, ?)",
        (title, amount, category)
    )
    conn.commit()
    conn.close()


def update_expense(expense_id, title, amount, category):
    conn = get_connection()
    conn.execute(
        "UPDATE expenses SET title = ?, amount = ?, category = ? WHERE id = ?",
        (title, amount, category, expense_id)
    )
    conn.commit()
    conn.close()


def delete_expense(expense_id):
    conn = get_connection()
    conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()


def get_total():
    conn = get_connection()
    row = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) AS total FROM expenses"
    ).fetchone()
    conn.close()
    return row["total"]


def title_exists(title, exclude_id=None):
    conn = get_connection()
    if exclude_id is not None:
        row = conn.execute(
            "SELECT id FROM expenses WHERE LOWER(title) = LOWER(?) AND id != ?",
            (title, exclude_id)
        ).fetchone()
    else:
        row = conn.execute(
            "SELECT id FROM expenses WHERE LOWER(title) = LOWER(?)",
            (title,)
        ).fetchone()
    conn.close()
    return row is not None
