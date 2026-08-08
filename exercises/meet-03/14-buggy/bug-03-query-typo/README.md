# Bug 3 · Query SQL Typo

# Tujuan

Melatih membaca error `OperationalError` dari SQLite dan
mencocokkan nama kolom di query dengan nama kolom asli di tabel.

# Yang Dipelajari

SQLite sangat teliti soal ejaan nama kolom — satu huruf tertukar
saja sudah membuat query gagal total.

# Penjelasan Konsep

`no such column: ...` selalu berarti: nama kolom yang kamu tulis di
query TIDAK ADA di tabel — biasanya karena salah ketik, bukan karena
kolomnya benar-benar tidak pernah dibuat.

# Langkah Pengerjaan

1. Jalankan `python app.py`.
2. Buka `localhost:5000/tambah-contoh` SEKALI untuk mengisi data
   contoh.
3. Buka `localhost:5000` — baca pesan error yang muncul.
4. Bandingkan nama kolom di pesan error dengan `CREATE TABLE`.

# File Yang Diubah

- `app.py` — perbaiki ejaan nama kolom di query `SELECT`.

# Checklist

- [ ] Nama kolom di query `SELECT ... WHERE ...` sudah sama persis
      dengan nama kolom di `CREATE TABLE`.
- [ ] Halaman `/` menampilkan transaksi dengan nominal di atas
      Rp 20.000, tanpa error.

# Hint

- Pesan error SQLite biasanya sangat spesifik — ia menyebutkan
  PERSIS nama kolom yang tidak ditemukan.
- Cek juga: apakah ejaan yang sama juga dipakai konsisten di seluruh
  query dalam file yang sama?

# Hasil Akhir

Query yang berhasil memfilter data sesuai nominal, tanpa error.

# Kesalahan Yang Sering Terjadi

Typo nama kolom sering lolos tanpa ketahuan saat menulis `INSERT`
(karena SQLite tidak selalu mengecek nama kolom di beberapa bentuk
query), tapi langsung ketahuan saat dipakai di `SELECT ... WHERE`.
