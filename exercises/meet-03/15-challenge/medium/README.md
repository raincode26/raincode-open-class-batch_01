# Challenge Medium · Filter Kategori

# Tujuan

Menampilkan hanya transaksi dari SATU kategori pilihan user — memakai
`request.args` (data dari URL) dan `SELECT ... WHERE` yang dibangun
secara kondisional.

# Yang Dipelajari

- `request.args.get('nama')` — mengambil data dari query string URL
  (`?kategori=Makanan`), BEDA dengan `request.form` yang mengambil
  dari body form yang di-POST.
- Query `SELECT` yang berubah tergantung ada/tidaknya filter —
  konsep percabangan (if/else) diterapkan ke pembuatan query SQL.

# Penjelasan Konsep

Form filter di `templates/index.html` memakai `method="GET"` (BUKAN
`POST`) — makanya kategori pilihan muncul di alamat URL, contoh:
`/?kategori=Makanan`. Ini yang membuatnya bisa dibagikan sebagai
tautan atau di-bookmark. Route `index()` perlu membaca nilai itu
lewat `request.args.get('kategori')`, LALU memutuskan: query SELECT
biasa (tanpa filter) atau `SELECT ... WHERE kategori = ?` (dengan
filter).

# Langkah Pengerjaan

1. Baca `templates/index.html` — form filter sudah lengkap.
2. Selesaikan `TODO 1` di `app.py`.
3. Jalankan `python app.py`, tambah beberapa transaksi dengan
   kategori berbeda-beda.
4. Pilih satu kategori di dropdown filter, klik Tampilkan.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] Memilih "Semua Kategori" menampilkan SEMUA transaksi.
- [ ] Memilih kategori tertentu HANYA menampilkan transaksi dari
      kategori itu.
- [ ] Dropdown filter tetap menunjukkan pilihan yang sedang aktif
      setelah halaman di-refresh (baca lagi bagaimana `templates/
      index.html` memakai `kategori_filter`).

# Hint

- `request.args.get('kategori')` mengembalikan `None` kalau filter
  kosong (`?kategori=`) ATAU kalau parameternya tidak ada sama
  sekali di URL — keduanya dianggap "tidak difilter".
- Gunakan `if kategori_filter:` untuk mengecek — string kosong `""`
  dan `None` sama-sama dianggap "falsy" di Python, jadi satu kondisi
  ini cukup menangani keduanya.
- Ingat untuk tetap mengirim `kategori_filter` ke
  `render_template(...)` — template butuh nilai itu untuk menandai
  pilihan yang aktif di dropdown.

# Hasil Akhir

Filter kategori yang benar-benar bekerja — daftar transaksi yang
bisa dipersempit sesuai kebutuhan, dengan alamat URL yang bisa
dibagikan.
