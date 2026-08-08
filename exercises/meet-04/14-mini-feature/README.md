# 14 · Mini Feature

# Tujuan Belajar

Menambah fitur kecil ke aplikasi yang SUDAH BEKERJA, mengikuti pola
arsitektur yang sudah kamu pahami (Route → Service → Repository) —
TANPA memakai materi yang belum pernah diajarkan.

# Penjelasan

Semua fitur yang SUDAH ADA di folder ini (Add, Edit, Delete, Search,
Filter kategori, Total keseluruhan) tetap `given/complete` — jangan
diubah. Tugasmu: tambah SATU fitur baru — **Total Per Kategori** —
mengikuti 3 TODO yang sudah ditandai di kode.

Fitur ini SENGAJA memakai pola yang PERSIS sama dengan yang sudah
kamu kuasai: `SUM()` + `GROUP BY` (dari `meet-03/15-challenge/hard`),
dan pola Repository → Service → Route → Template (dari SEMUA folder
01–13 di `meet-04`). Tidak ada syntax baru sama sekali di sini.

# Diagram

```
templates/index.html          app.py             service.py           repository.py
   TODO 3                        │  TODO 2 dipanggil    TODO 2                TODO 1
   tampilkan category_totals ◀───┴── category_totals ◀── get_totals_per_ ◀── get_category_totals()
                                                          category()          SUM()+GROUP BY
```

# Langkah Pengerjaan

1. Jalankan `python app.py`, buka `/`, pastikan SEMUA fitur yang ada
   sekarang bekerja normal (Add, Edit, Delete, Search, Filter, Total).
2. Buka `repository.py`, cari `# TODO 1`. Lengkapi function
   `get_category_totals()` — hapus baris `return None`, aktifkan
   (uncomment) kode contoh di atasnya, atau tulis versimu sendiri.
3. Buka `service.py`, cari `# TODO 2`. Function `get_totals_per_category()`
   SEHARUSNYA sudah otomatis bekerja begitu TODO 1 selesai (ia cuma
   memanggil `get_category_totals()`) — baca komentarnya untuk
   konfirmasi.
4. Buka `templates/index.html`, cari `TODO 3`. Aktifkan blok Jinja
   yang menampilkan `category_totals` di halaman (di antara total
   keseluruhan dan tabel daftar expense).
5. Jalankan ulang, tambah beberapa expense dengan kategori berbeda,
   pastikan total per kategori muncul dan angkanya benar.

# File Yang Diubah

- `repository.py`
- `service.py`
- `templates/index.html`

# Checklist

- [ ] `get_category_totals()` di `repository.py` mengembalikan data
      SUM per kategori, bukan lagi `None`.
- [ ] Halaman `/` menampilkan daftar total per kategori.
- [ ] Menambah expense baru dengan kategori baru langsung memperbarui
      angka total kategori tersebut setelah refresh.
- [ ] SEMUA fitur lama (Add, Edit, Delete, Search, Filter) masih
      bekerja seperti sebelumnya.

# Hint

- `pass`/`return None` di function TODO 1 sengaja dibiarkan supaya
  aplikasi TETAP BISA DIJALANKAN sebelum kamu selesai — cuma bagian
  "Total Per Kategori" saja yang belum muncul (karena `{% if
  category_totals %}` aman menerima `None`, Jinja cukup tidak
  menampilkan apa-apa, tidak crash).
- Jangan sentuh function CRUD yang sudah ada (`get_all_expenses`,
  `create_expense`, dst.) — fitur baru ini HANYA menambah, tidak
  mengubah yang lama.
- Kalau angka total per kategori terasa salah, cek dulu: apakah kamu
  memakai `GROUP BY category` (mengelompokkan per NILAI kategori),
  bukan `GROUP BY id` atau lupa `GROUP BY` sama sekali?

# Hasil yang Diharapkan

Halaman daftar expense yang sekarang juga menampilkan ringkasan total
per kategori — fitur baru, ditambahkan tanpa merusak yang lama.

# Refleksi

1. Kenapa TODO 1 (repository) harus selesai SEBELUM TODO 2 (service)
   bisa "berarti", padahal secara teknis kamu bisa mengetik urutan
   file berapa pun? Apa yang terjadi kalau kamu kerjakan TODO 3
   (template) duluan, sebelum TODO 1 & 2?
2. Fitur ini sengaja tidak butuh perubahan di `app.py` bagian try/
   except (validasi) sama sekali — kenapa? Fitur macam apa yang PASTI
   butuh perubahan di sana, dan fitur macam apa yang tidak?
