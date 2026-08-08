# database.py
# Koneksi & skema database — satu-satunya tempat sqlite3.connect() dipanggil.

import sqlite3

DATABASE_PATH = "expenses.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
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
