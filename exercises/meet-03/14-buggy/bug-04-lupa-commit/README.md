# Bug 4 · Lupa commit()

# Tujuan

Melatih kebiasaan paling mudah luput: memastikan `db.commit()` selalu
ada setelah `INSERT`/`UPDATE`/`DELETE` — apalagi karena bug ini TIDAK
menghasilkan error sama sekali.

# Yang Dipelajari

Tanpa `db.commit()`, perubahan hanya "niat" di satu koneksi — tidak
pernah benar-benar tersimpan ke file `.db`, dan tidak terlihat oleh
koneksi lain (termasuk koneksi baru yang dibuka route lain).

# Penjelasan Konsep

Ini bug PALING BERBAHAYA justru karena diam-diam. Tidak ada pesan
error, tidak ada crash — aplikasi terlihat "berhasil" menyimpan
(redirect berjalan mulus), tapi datanya sebenarnya tidak pernah
masuk. Inilah kenapa kebiasaan MENGECEK HASIL (bukan cuma
"tidak error berarti berhasil") itu penting.

# Langkah Pengerjaan

1. Jalankan `python app.py`, isi form, klik Simpan.
2. Perhatikan: tidak ada error, tapi transaksi barumu tidak muncul
   di daftar.
3. Baca ulang route `tambah()` di `app.py`, bandingkan dengan pola
   yang sama di folder `07-create-expense`.

# File Yang Diubah

- `app.py` — tambahkan baris yang hilang di route `tambah()`.

# Checklist

- [ ] `db.commit()` dipanggil setelah `db.execute("INSERT ...")`.
- [ ] Transaksi baru langsung muncul di daftar setelah disimpan.
- [ ] Transaksi tetap ada setelah server di-restart.

# Hint

- Route ini hampir sama persis dengan `07-create-expense` — cari
  SATU baris yang berbeda.
- "Tidak ada error" BUKAN jaminan "berhasil". Selalu verifikasi
  hasilnya secara langsung (lihat apakah datanya benar-benar muncul).

# Hasil Akhir

Data yang benar-benar tersimpan permanen — bukan cuma "terkirim".

# Kesalahan Yang Sering Terjadi

Ini adalah salah satu bug tersering pada pemula justru karena
aplikasinya "terasa" berfungsi (tidak ada error, redirect jalan
normal) — padahal datanya tidak pernah tersimpan sama sekali.
