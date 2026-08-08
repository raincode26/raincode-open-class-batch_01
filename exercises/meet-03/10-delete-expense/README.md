# 10 · Delete Expense

# Tujuan

Menghapus data — huruf terakhir CRUD. Setelah ini kamu resmi
menguasai keempatnya: Create, Read, Update, Delete.

# Yang Dipelajari

- `DELETE FROM transactions WHERE id = ?` — pola SQL untuk
  menghapus satu baris.
- Pola route yang sama sekali lagi: ambil `id` dari URL, jalankan
  query, `commit()`, `redirect`.

# Penjelasan Konsep

**Aturan emas yang sama persis dengan Update, kali ini lebih
berbahaya:** `DELETE FROM transactions` TANPA `WHERE id = ?`
menghapus **SELURUH ISI TABEL** — bukan cuma satu baris. Tidak ada
"tombol undo" di SQLite untuk ini. Selalu pastikan `WHERE` ada
sebelum menjalankan `DELETE`.

Perhatikan juga: setelah folder ini, route `hapus()` polanya SANGAT
mirip dengan `detail()` dari `08-read-expense` — sama-sama menerima
`<int:id>` dan memakai `WHERE id = ?`. Bedanya cuma perintah SQL-nya
(`SELECT` vs `DELETE`) dan apa yang dilakukan setelahnya (tampilkan
vs hapus).

# Langkah Pengerjaan

1. Baca `templates/index.html` — tautan "Hapus" sudah ditambahkan.
2. Selesaikan `TODO 1` di `app.py`: buat route `/hapus/<int:id>`.
3. Jalankan `python app.py`, klik "Hapus" pada salah satu transaksi.
4. Pastikan HANYA transaksi itu yang hilang, yang lain tetap ada.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] Route `/hapus/<int:id>` berhasil dibuat.
- [ ] Query memakai `WHERE id = ?` (BUKAN `DELETE FROM transactions`
      polos tanpa `WHERE`).
- [ ] `db.commit()` dipanggil setelah `DELETE`.
- [ ] Setelah hapus, transaksi lain (yang tidak diklik) TETAP ada.

# Hint

- Kalau ragu, cetak dulu query-nya dengan `print()` sebelum
  dijalankan — pastikan ada `WHERE id = ?` di dalamnya sebelum kamu
  yakin untuk menjalankannya.
- Tidak ada konfirmasi "yakin mau hapus?" di latihan ini — sengaja
  dibuat sesederhana mungkin. Kamu boleh menambahkannya sendiri
  sebagai latihan tambahan (lihat `15-challenge`).
- Klik "Hapus" pada id yang SUDAH dihapus sebelumnya (misalnya lewat
  dua tab browser) tidak akan error — `DELETE ... WHERE id = ?`
  yang tidak menemukan barisnya cukup "tidak melakukan apa-apa",
  bukan crash.

# Hasil Akhir

CRUD lengkap: kamu bisa menambah, melihat, mengubah, dan menghapus
data — semuanya tersimpan permanen di SQLite. Selanjutnya di
`11-complete-crud`, kita rapikan semuanya jadi satu aplikasi utuh
dan menambah dua kolom baru.

# Kesalahan Yang Sering Terjadi

- **Lupa `WHERE id = ?` di `DELETE`** → SELURUH tabel kosong dalam
  sekejap. Ini bug paling merusak di seluruh modul — jangan pernah
  menjalankan `DELETE` tanpa memastikan `WHERE`-nya ada.
- **Salah urutan**: `db.commit()` dipanggil SEBELUM
  `db.execute("DELETE ...")` → perubahan belum ada saat commit
  dijalankan, jadi tidak berpengaruh.
- **Tombol Hapus lupa dibungkus tautan ke `/hapus/{{ t.id }}`** yang
  benar → mengklik tombol tidak melakukan apa-apa atau menghapus
  baris yang salah.
