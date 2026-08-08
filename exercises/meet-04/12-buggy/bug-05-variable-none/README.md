# Bug 5 · Variable None

# Tujuan Belajar

Melatih kebiasaan mengecek `None` SEBELUM mengakses isi hasil query —
`fetchone()` tidak selalu berhasil menemukan barisnya.

# Penjelasan

`service.get_expense(expense_id)` mengembalikan `None` kalau `id`
yang diminta tidak ada di database. Kalau baris kode SETELAHNYA
langsung mengakses `expense["title"]` tanpa mengecek `None` dulu,
Python akan crash dengan `TypeError: 'NoneType' object is not
subscriptable` — ini SANGAT umum terjadi tepat setelah
`fetchone()`/pencarian by-id, karena satu-satunya cara tahu "ketemu
atau tidak" adalah mengecek hasilnya secara eksplisit.

# Diagram

```
app.py → def edit(expense_id):

expense = service.get_expense(expense_id)   # None kalau id tak ada
print("Editing expense:", expense["title"]) # ✗ crash kalau expense None
        │
        ▼
TypeError: 'NoneType' object is not subscriptable
```

# Langkah Pengerjaan

1. Jalankan `python app.py`, tambah satu expense lewat `/create`.
2. Buka `/edit/1` (ganti `1` dengan id yang BENAR-benar ada) — harus
   tampil normal.
3. Buka `/edit/999` (id yang TIDAK ada) — amati error 500 dan baca
   traceback-nya.
4. Buka `app.py`, cari function `edit()`.
5. Perbaiki dengan mengecek `None` SEBELUM baris yang bermasalah.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] `/edit/1` (id yang ada) tetap tampil normal.
- [ ] `/edit/999` (id yang tidak ada) TIDAK LAGI menyebabkan error
      500 — cukup flash pesan "Expense tidak ditemukan." dan redirect
      ke halaman daftar.

# Hint

- Solusi paling sederhana: tambahkan `if expense is None: flash(...);
  return redirect(url_for("index"))` SEGERA setelah baris
  `expense = service.get_expense(expense_id)`, sebelum baris
  `print(...)` yang bermasalah.
- Baris `print(...)` itu sendiri cuma alat bantu debugging — kamu
  boleh menghapusnya sepenuhnya kalau mau, ia bukan bagian penting
  dari fitur Edit.
- Perhatikan: di kode Python biasa, isi sebuah baris hasil query
  (`sqlite3.Row`) HANYA bisa diambil lewat `expense["title"]` (gaya
  dict) — beda dengan di dalam file HTML/Jinja yang boleh memakai
  `expense.title` (gaya atribut). Jinja punya kemudahan khusus ini,
  Python murni tidak.

# Hasil yang Diharapkan

Halaman Edit yang menangani KEDUA kemungkinan dengan baik: id yang
ada, dan id yang tidak ada — tanpa membuat aplikasi crash.

# Refleksi

Bandingkan dengan Skenario 5 di `11-debugging` — apakah dugaanmu di
sana (sebelum melihat kode sungguhan) sudah tepat?
