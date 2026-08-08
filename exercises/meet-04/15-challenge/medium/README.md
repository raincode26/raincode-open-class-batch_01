# Challenge Medium · Aktifkan Search

# Tujuan Belajar

Melengkapi SATU function di lapisan Repository — tanpa tuntunan
langkah-per-langkah, cuma tujuan akhir & satu TODO.

# Penjelasan

Kotak pencarian di halaman `/` SUDAH ADA di HTML, dan `app.py` /
`service.py` SUDAH mengirim nilai `search` sampai ke Repository — tapi
`repository.py` belum benar-benar MEMAKAI nilai itu di query SQL-nya.
Akibatnya, ketik apa pun di kotak search, hasilnya tidak berubah sama
sekali (semua expense tetap muncul).

# Diagram

```
templates/index.html   app.py         service.py      repository.py
<input name="search">  request.args   list_expenses   get_all_expenses(search=...)
       │                    │               │                  │
       └────────────────────┴───────────────┴──── sampai di sini, TAPI
                                                     belum dipakai di query
                                                     TODO: tambahkan
                                                     "title LIKE ?"
```

# Langkah Pengerjaan

1. Jalankan `python app.py`, tambah beberapa expense dengan title
   berbeda-beda, coba ketik sesuatu di kotak search — buktikan dulu
   bahwa search MEMANG belum bekerja.
2. Buka `repository.py`, cari `TODO 1` di function
   `get_all_expenses`.
3. Lengkapi kondisi untuk `search`, mengikuti pola yang SUDAH ada
   untuk `category` tepat di bawahnya.
4. Jalankan ulang, buktikan search sekarang bekerja.

# File Yang Diubah

- `repository.py`

# Checklist

- [ ] Mengetik kata kunci di kotak search HANYA menampilkan expense
      yang title-nya mengandung kata itu.
- [ ] Search & filter kategori bisa dipakai BERSAMAAN (keduanya aktif
      sekaligus).
- [ ] Search kosong (dikosongkan lagi) menampilkan semua expense
      seperti semula.

# Hint

- Pola yang kamu butuhkan SUDAH ADA persis di bawahnya (blok `if
  category:`) — tinggal disesuaikan untuk `search` & kolom `title`.
- `LIKE` di SQLite butuh tanda `%` di kiri-kanan kata kunci untuk
  mencari "mengandung" (bukan "sama persis") — `f"%{search}%"`.
- Kalau search & category SAMA-SAMA diisi, keduanya harus digabung
  dengan `AND` — perhatikan bagaimana `conditions` (list) sudah
  dirancang untuk menangani ini secara otomatis, apa pun jumlah
  kondisi aktifnya.

# Hasil yang Diharapkan

Fitur search yang benar-benar menyaring daftar expense berdasarkan
title, bisa dipakai sendiri atau digabung dengan filter kategori.

# Refleksi

Kenapa perubahan untuk fitur ini HANYA perlu terjadi di
`repository.py`, padahal `search` datang dari input user lewat
`app.py`? Lapisan mana yang SUDAH cukup siap menerima fitur baru,
tanpa perlu ikut diubah?
