# Bug 6 · Variabel None Tidak Dicek

# Tujuan

Melatih kebiasaan mengecek `None` sebelum mengakses isi sebuah hasil
query — `fetchone()` tidak selalu berhasil menemukan barisnya.

# Yang Dipelajari

`.fetchone()` mengembalikan `None` (bukan error) kalau tidak ada
baris yang cocok. Masalah baru muncul kalau kode SETELAHNYA mencoba
mengakses `.nama` atau `.nominal` dari `None` itu tanpa dicek dulu.

# Penjelasan Konsep

`'NoneType' object is not subscriptable` selalu berarti: sesuatu
yang kamu kira berisi data (Row, bisa diakses lewat `[...]`), ternyata
`None`. Ini SANGAT umum terjadi tepat setelah `.fetchone()`, karena
satu-satunya cara tahu "ketemu atau tidak" adalah dengan mengecek
hasilnya secara eksplisit — Python tidak melakukannya otomatis.

# Langkah Pengerjaan

1. Jalankan `python app.py`, buka `/tambah-contoh` sekali (supaya
   ada data id=1).
2. Buka `/detail/1` — harus tampil normal.
3. Buka `/detail/999` — amati error `500 Internal Server Error` dan
   baca traceback-nya.
4. Perbaiki `app.py`.

# File Yang Diubah

- `app.py` — tambahkan pengecekan sebelum mengakses `item['nama']`.

# Checklist

- [ ] `/detail/1` (id yang ada) tetap tampil normal.
- [ ] `/detail/999` (id yang tidak ada) TIDAK LAGI menyebabkan error
      500 — cukup tampilkan halaman "tidak ditemukan" (template
      `detail.html` sudah siap menanganinya lewat `{% if item %}`).

# Hint

- `templates/detail.html` SUDAH benar (sudah memakai `{% if item
  %}`) — bug-nya ada di `app.py`, SEBELUM `render_template`
  dipanggil.
- Cara paling sederhana: bungkus baris `print(...)` yang bermasalah
  dengan pengecekan `if item:` terlebih dulu, atau hapus saja baris
  `print()` itu (ia cuma alat bantu debugging, bukan bagian penting
  dari fitur).
- Perhatikan: di dalam kode Python biasa, isi `Row` HANYA bisa
  diambil lewat `item['nama']` (gaya dict) — beda dengan di dalam
  file HTML/Jinja yang boleh memakai `item.nama` (gaya atribut).
  Jinja punya kemudahan khusus ini, Python murni tidak.

# Hasil Akhir

Halaman detail yang menangani KEDUA kemungkinan dengan baik: id yang
ada, dan id yang tidak ada — tanpa membuat aplikasi crash.

# Kesalahan Yang Sering Terjadi

Bug ini sangat umum saat menambahkan `print()` untuk debugging
(seperti di `13-debugging`) tanpa sadar bahwa variabel yang di-print
bisa saja `None` dalam kondisi tertentu.
