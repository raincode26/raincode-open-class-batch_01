# 08 · Database Analysis

# Tujuan Belajar

Membaca skema SQLite di `database/db.py` dan SEMUA query di
`repositories/expense_repository.py` — tahu persis kolom apa saja
yang ada, dan query apa yang menyentuh data.

# Penjelasan

Tabelnya cuma satu: `expenses`. Skemanya ada di
`database/db.py`:

```sql
CREATE TABLE IF NOT EXISTS expenses (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    amount      REAL    NOT NULL,
    category    TEXT    NOT NULL DEFAULT 'Other',
    notes       TEXT             DEFAULT '',
    created_at  TEXT    NOT NULL DEFAULT (datetime('now', 'localtime')),
    updated_at  TEXT    NOT NULL DEFAULT (datetime('now', 'localtime'))
);
```

Perhatikan tiga hal yang tidak pernah kamu tulis sendiri di
`meet-03`:

- **`DEFAULT (datetime('now', 'localtime'))`** — waktu dibuat OLEH
  DATABASE itu sendiri, bukan oleh Python (`datetime.now()`). Ini
  disengaja: satu sumber waktu yang sama, tidak peduli dari komputer
  mana request datang.
- **`category TEXT NOT NULL DEFAULT 'Other'`** — kalau `category`
  tidak diisi sama sekali saat INSERT, SQLite otomatis mengisi
  `'Other'`. Tapi project ini TETAP memvalidasi kategori di
  `services/` juga — kenapa validasi ganda? (jawabannya ada di
  Refleksi).
- **Tidak ada `FOREIGN KEY`** — tabel ini berdiri sendiri, tidak
  terhubung ke tabel lain (belum ada tabel `users`, misalnya).

Semua query CRUD (semuanya, tanpa kecuali) hidup di
`repositories/expense_repository.py`:

| Operasi | Function | Query inti |
|---|---|---|
| Create | `create_expense(...)` | `INSERT INTO expenses (title, amount, category, notes) VALUES (?, ?, ?, ?)` |
| Read (banyak) | `get_expenses(...)` | `SELECT ... FROM expenses {WHERE ...} ORDER BY ...` |
| Read (satu) | `get_expense_by_id(id)` | `SELECT ... FROM expenses WHERE id = ?` |
| Update | `update_expense(...)` | `UPDATE expenses SET ..., updated_at = datetime('now','localtime') WHERE id = ?` |
| Delete | `delete_expense(id)` | `DELETE FROM expenses WHERE id = ?` |
| Agregat | `get_category_totals()` | `SELECT category, SUM(amount), COUNT(*) FROM expenses GROUP BY category` |

# Diagram

```
expenses
┌────┬───────┬────────┬──────────┬───────┬────────────┬────────────┐
│ id │ title │ amount │ category │ notes │ created_at │ updated_at │
├────┼───────┼────────┼──────────┼───────┼────────────┼────────────┤
│ PK │ TEXT  │ REAL   │ TEXT     │ TEXT  │ TEXT       │ TEXT       │
│    │ NOT   │ NOT    │ NOT NULL │       │ NOT NULL   │ NOT NULL   │
│    │ NULL  │ NULL   │ DEFAULT  │       │ DEFAULT    │ DEFAULT    │
│    │       │        │ 'Other'  │       │ now()      │ now()      │
└────┴───────┴────────┴──────────┴───────┴────────────┴────────────┘
 id dibuat OTOMATIS (AUTOINCREMENT) — tidak pernah kamu isi manual.
```

# Langkah Pengerjaan

1. Buka `database/db.py`, cari `CREATE TABLE IF NOT EXISTS expenses`.
   Untuk SETIAP kolom, tulis: nama, tipe data, dan apakah boleh kosong
   (`NOT NULL` atau tidak).
2. Buka `repositories/expense_repository.py`, cari SEMUA baris yang
   mengandung kata `SELECT`, `INSERT`, `UPDATE`, `DELETE` (pakai
   `Ctrl+F`, case-sensitive kalau perlu). Hitung: ada berapa query
   unik total?
3. Cari function `get_expenses(...)`. Perhatikan query-nya dibangun
   sebagian dari STRING BIASA (bukan cuma `?` placeholder) — cari
   variabel `sort_by` di dekatnya, dan baca kenapa nama kolom untuk
   `ORDER BY` TIDAK bisa memakai `?` seperti value biasa (petunjuk:
   `?` cuma bisa menggantikan NILAI, bukan NAMA KOLOM).
4. Cari function `get_category_totals()`. Baca query `GROUP BY
   category`-nya — bandingkan dengan `SUM()` + `GROUP BY` yang sudah
   kamu pelajari di `meet-03/15-challenge/hard`.
5. Cari SEMUA tempat yang memanggil `conn.commit()`. Untuk operasi
   MANA saja `commit()` dipanggil, dan untuk operasi mana TIDAK
   (petunjuk: `SELECT` tidak pernah butuh `commit()` — kenapa?).

# File Yang Diubah

Tidak ada — folder ini murni membaca.

# Checklist

- [ ] Skema tabel `expenses` (7 kolom, tipe, NOT NULL/tidak) sudah
      kamu tulis ulang dari ingatan dengan benar.
- [ ] Tahu berapa total query SQL unik di seluruh project, dan bisa
      menyebutkan masing-masing termasuk operasi CRUD yang mana.
- [ ] Paham kenapa nama kolom untuk `ORDER BY` tidak bisa diparameter-
      kan dengan `?` seperti value biasa.

# Hint

- SQLite menyimpan SEMUA angka desimal (`amount`) sebagai `REAL`,
  bukan tipe uang/currency khusus — ini sebabnya `round(amount, 2)`
  dipanggil manual di `services/` sebelum disimpan, supaya tidak ada
  angka aneh seperti `25000.0000000001` akibat pembulatan biner.
- Kalau bingung kenapa `sort_by` "berbahaya" ditulis langsung ke
  string SQL: baca lagi bagaimana ia DIBATASI dulu (whitelist) sebelum
  dipakai — cari kata `{"id", "title", "amount", ...}` di dekatnya.
  Ini SATU-SATUNYA pengecualian dari aturan "selalu pakai `?`" di
  seluruh project, dan dilakukan dengan sangat hati-hati.
- `PRAGMA foreign_keys = ON` di `database/db.py` terlihat aneh karena
  belum ada `FOREIGN KEY` sama sekali di skema saat ini — itu
  kebiasaan baik yang disiapkan untuk masa depan (kalau nanti ada
  tabel `users`, aturan relasi akan langsung ditegakkan).

# Hasil yang Diharapkan

Kamu bisa menggambar skema tabel `expenses` dari ingatan, dan
menunjuk baris query mana pun di `expense_repository.py` sambil
menjelaskan operasi CRUD apa yang diwakilinya.

# Refleksi

1. `category` punya `DEFAULT 'Other'` di level DATABASE, tapi
   `services/expense_service.py` JUGA menolak kategori yang tidak
   valid. Kenapa validasi dilakukan di DUA tempat, bukan cukup satu
   saja? Apa yang terjadi kalau hanya database yang memvalidasi
   (tanpa Service)?
2. Kalau kamu diminta menambah kolom baru `is_recurring` (boolean,
   menandai pengeluaran berulang), langkah mana saja yang perlu
   diubah — dan di file/lapisan mana masing-masing?
