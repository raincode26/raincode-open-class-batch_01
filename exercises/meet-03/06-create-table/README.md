# 06 · Create Table

# Tujuan

Membuat tabel `transactions` di dalam SQLite lewat Flask — gudang
resmi tempat CRUD kita akan bekerja mulai folder berikutnya.

# Yang Dipelajari

- `get_db()` — pola koneksi yang akan dipakai ULANG di SETIAP route
  CRUD mulai sekarang: buka koneksi baru, set `row_factory`, pakai,
  selesai.
- `CREATE TABLE IF NOT EXISTS` di dalam Flask, dipanggil SATU KALI
  saat aplikasi dinyalakan — bukan tiap ada request.
- `{% if data %} ... {% else %} ... {% endif %}` di Jinja — tampilan
  berbeda untuk data kosong vs ada isinya.

# Penjelasan Konsep

Ingat urutan di SQL: sebelum `INSERT` (Create), tabelnya harus ADA
dulu. `CREATE TABLE` menentukan bentuk gudang — kolom apa saja yang
boleh disimpan — sebelum barang apa pun bisa masuk. Kita panggil
`init_db()` di LUAR function route manapun, supaya ia jalan sekali
saja saat `python app.py` dieksekusi, bukan berulang-ulang tiap
pengunjung buka halaman.

# Langkah Pengerjaan

1. Baca `get_db()` yang sudah lengkap — ini pola yang akan terus
   berulang.
2. Selesaikan `TODO 1`: tulis function `init_db()`.
3. Selesaikan `TODO 2`: panggil `init_db()` sekali, di luar route.
4. Jalankan `python app.py`, buka `localhost:5000`.
5. Cek folder ini — file `expense_tracker.db` seharusnya muncul
   otomatis.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] `init_db()` berhasil dibuat, memakai `CREATE TABLE IF NOT
      EXISTS`.
- [ ] `init_db()` dipanggil di luar function `index()`, hanya sekali.
- [ ] File `expense_tracker.db` muncul setelah `python app.py`
      dijalankan.
- [ ] Halaman `/` menampilkan "Belum ada transaksi..." (bukan error).
- [ ] Menjalankan `python app.py` berkali-kali TIDAK memunculkan
      error "table already exists".

# Hint

- Kalau lupa `IF NOT EXISTS`, aplikasi akan crash tiap kali
  di-restart karena mencoba membuat tabel yang sudah ada.
- `init_db()` butuh koneksinya SENDIRI (panggil `get_db()` di
  dalamnya) — jangan berbagi satu koneksi untuk semua hal.
- Belum ada UI untuk menambah data — itu wajar, fokus latihan ini
  murni menyiapkan tabelnya. Data mulai bisa ditambah di
  `07-create-expense`.

# Hasil Akhir

Aplikasi Flask yang, begitu dinyalakan, otomatis memastikan tabelnya
sudah siap — pondasi wajib sebelum operasi CRUD apa pun bisa berjalan.

# Kesalahan Yang Sering Terjadi

- **`init_db()` dipanggil DI DALAM route `index()`** → tabel dicoba
  dibuat ulang setiap kali halaman dibuka. Tidak fatal (berkat
  `IF NOT EXISTS`), tapi tidak efisien & bukan polanya.
- **Lupa `db.commit()` di `init_db()`** → tabel kadang tidak
  benar-benar tersimpan, terutama kalau koneksinya langsung ditutup.
- **Salah nama tabel** antara `CREATE TABLE transactions` dan
  `SELECT * FROM transaction` (lupa "s") → error
  `no such table: transaction`.
- **Menjalankan `python app.py` dari folder yang salah** → file
  `expense_tracker.db` bisa muncul di lokasi yang tidak terduga,
  karena `sqlite3.connect()` memakai path relatif terhadap folder
  saat perintah dijalankan.
