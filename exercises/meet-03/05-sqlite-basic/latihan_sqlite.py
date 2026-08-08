# latihan_sqlite.py
# Topik: SQLite Dasar — Koneksi & Query (TANPA Flask dulu)

# ============================================================
# MISI KAMU
# ============================================================
# Sebelum SQLite dipakai DI DALAM Flask, kenalan dulu dengan
# sqlite3 sendirian. File ini BUKAN aplikasi web — jalankan langsung
# lewat terminal:
#   python latihan_sqlite.py
#
# Database itu berdiri sendiri, terpisah dari Flask. Flask cuma
# salah satu cara memanggilnya lewat browser.

import sqlite3

# ============================================================
# BAGIAN 1 — Membuat koneksi
# ============================================================
# sqlite3.connect(nama_file) membuka file .db (dibuat otomatis kalau
# belum ada). File ini adalah "gudang arsip" tempat semua data hidup
# permanen, walau program ditutup.

db = sqlite3.connect('latihan.db')
db.row_factory = sqlite3.Row  # hasil query nanti bisa dibaca lewat nama kolom


# ============================================================
# BAGIAN 2 — Membuat tabel (CREATE TABLE)
# ============================================================
# TODO 1: Jalankan query CREATE TABLE untuk membuat tabel bernama
# "transactions" dengan kolom:
#   id       INTEGER PRIMARY KEY AUTOINCREMENT
#   nama     TEXT NOT NULL
#   nominal  INTEGER
#
# IF NOT EXISTS penting supaya query ini aman dijalankan berkali-kali
# tanpa error "tabel sudah ada".
#
# Pola:
#   db.execute("""
#       CREATE TABLE IF NOT EXISTS transactions (
#           id INTEGER PRIMARY KEY AUTOINCREMENT,
#           nama TEXT NOT NULL,
#           nominal INTEGER
#       )
#   """)


# ============================================================
# BAGIAN 3 — Mengisi data (INSERT)
# ============================================================
# TODO 2: Masukkan 2-3 baris data pakai INSERT + placeholder "?".
# Pakai ? (bukan f-string!) supaya aman dari SQL injection.
#
# Pola:
#   db.execute("INSERT INTO transactions (nama, nominal) VALUES (?, ?)",
#              ("Kopi pagi", 25000))
#   db.execute("INSERT INTO transactions (nama, nominal) VALUES (?, ?)",
#              ("Ongkos bus", 10000))


# TODO 3: Jangan lupa commit() supaya data di atas benar-benar
# tersimpan permanen ke file .db (bukan cuma "niat" di memori).
#
# Pola:
#   db.commit()


# ============================================================
# BAGIAN 4 — Membaca data (SELECT)
# ============================================================
# TODO 4: Ambil semua baris dari tabel transactions, lalu cetak
# tiap barisnya ke terminal.
#
# Pola:
#   rows = db.execute("SELECT * FROM transactions").fetchall()
#   for r in rows:
#       print(r['id'], r['nama'], r['nominal'])


# ============================================================
# BAGIAN 5 — Menutup koneksi
# ============================================================
db.close()

# ============================================================
# COBA INI SETELAH SELESAI
# ============================================================
# Jalankan file ini 2x berturut-turut:
#   python latihan_sqlite.py
#   python latihan_sqlite.py
# Perhatikan: transaksinya BERTAMBAH TERUS tiap dijalankan (karena
# INSERT selalu menambah baris baru), tapi TABEL-nya tidak dibuat
# ulang (karena IF NOT EXISTS). Coba juga buka file latihan.db yang
# baru muncul di folder ini — itu database sungguhan di disk-mu.
