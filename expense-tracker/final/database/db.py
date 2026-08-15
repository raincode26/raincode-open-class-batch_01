"""Satu pintu untuk membuka connection dan menjalankan query MySQL."""

from typing import Any, Literal

import mysql.connector
from mysql.connector import Error

from config import config


FetchMode = Literal["one", "all"] | None


def get_connection():
    """Buka connection baru menggunakan konfigurasi dari .env."""
    return mysql.connector.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME,
    )


def execute(
    query: str,
    params: tuple | list = (),
    fetch: FetchMode = None,
) -> Any:
    """Jalankan satu query, lalu fetch atau commit sesuai operation."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, tuple(params))

        if fetch == "one":
            return cursor.fetchone()
        if fetch == "all":
            return cursor.fetchall()

        result = {
            "lastrowid": cursor.lastrowid,
            "rowcount": cursor.rowcount,
        }
        connection.commit()
        return result
    except Error:
        if connection is not None:
            connection.rollback()
        raise
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


def init_db() -> None:
    """Buat table expenses jika belum tersedia."""
    query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(200) NOT NULL,
            amount DECIMAL(15, 2) NOT NULL,
            category VARCHAR(100) NOT NULL DEFAULT 'Other',
            notes TEXT NOT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """
    execute(query)
