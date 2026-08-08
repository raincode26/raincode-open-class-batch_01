# Bug 3 · SQL Typo

# Tujuan Belajar

Membaca `sqlite3.OperationalError` dan tahu kenapa error ini SELALU
berarti "masalah di query, bukan di Python."

# Penjelasan

Python tidak tahu apa isi tabel `expenses` di database — ia cuma
mengirim STRING (query SQL) ke SQLite, dan SQLite-lah yang menolaknya
kalau ada nama kolom yang tidak ada. Errornya baru muncul saat query
DIJALANKAN, bukan saat kode Python-nya ditulis — itu sebabnya bug ini
tidak akan pernah terlihat cuma dengan membaca kode Python sekilas.

# Diagram

```
repository.py

conn.execute(
    "UPDATE expenses SET titl = ?, ...", (...)
)                        ↑
                    kolom "titl" TIDAK ADA
                    (yang ada: "title")
        │
        ▼
sqlite3.OperationalError: no such column: titl
```

# Langkah Pengerjaan

1. Jalankan `python app.py`, buka `/`, klik Edit pada salah satu
   expense (kalau belum ada data, tambah satu dulu lewat `/create`).
2. Ubah sesuatu di form edit, klik Update.
3. Baca traceback — cari baris `sqlite3.OperationalError`.
4. Buka `repository.py`, cari function `update_expense`.
5. Bandingkan nama kolom di query dengan skema tabel di `database.py`.

# File Yang Diubah

- `repository.py`

# Checklist

- [ ] Nama kolom di query `UPDATE` pada `update_expense` sekarang
      cocok dengan skema di `database.py`.
- [ ] Submit form Edit tidak lagi menampilkan error 500.
- [ ] Perubahan data BENAR-BENAR tersimpan (cek di halaman daftar).

# Hint

- Skema tabel yang BENAR ada di `database.py`, fungsi `init_db()` —
  itu "sumber kebenaran" untuk nama kolom.
- Error `no such column: X` HAMPIR SELALU berarti typo nama kolom di
  SATU baris query tertentu — cari nama `X` itu persis di
  `repository.py`.

# Hasil yang Diharapkan

Fitur Edit yang benar-benar menyimpan perubahan ke database.

# Refleksi

Kalau typo ini ada di kolom `WHERE id = ?` (bukan di `SET`), apakah
errornya akan sama persis? Coba jelaskan bedanya.
