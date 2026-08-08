# 07 · Create Expense

# Tujuan

Menyimpan data yang diisi pengunjung ke SQLite — huruf **C** pertama
dari CRUD, benar-benar permanen kali ini (tidak seperti
`04-form-request`).

# Yang Dipelajari

- Perjalanan lengkap Create: `User → HTML Form → Flask Route →
  Python → INSERT → SQLite`.
- `INSERT INTO transactions (nama, nominal) VALUES (?, ?)` — pola
  SQL untuk menambah baris baru.
- Kenapa `db.commit()` WAJIB — tanpanya, `INSERT` hanya "niat", data
  tidak benar-benar tersimpan ke file `.db`.

# Penjelasan Konsep

Ini bab yang mengubah `04-form-request` dari "terasa tersimpan" jadi
"BENAR-BENAR tersimpan". Alurnya: form dikirim → `request.form`
menangkapnya → SQL `INSERT` menaruhnya ke tabel → `commit()`
menguncinya permanen → `redirect` membawa user kembali melihat
hasilnya. Coba matikan & nyalakan ulang server setelah menambah
data — kali ini datanya TIDAK hilang.

# Langkah Pengerjaan

1. Baca `templates/index.html` — form sudah lengkap, sama seperti
   `04-form-request`.
2. Selesaikan `TODO 1` di `app.py`: buat route `/tambah`.
3. Jalankan `python app.py`, isi form, klik Simpan.
4. Restart server (`Ctrl+C`, jalankan lagi), refresh browser —
   datamu masih ada.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] Route `/tambah` memakai `methods=['POST']`.
- [ ] Query `INSERT` memakai placeholder `?`, bukan f-string.
- [ ] `db.commit()` dipanggil setelah `db.execute(...)`.
- [ ] Setelah submit, data baru muncul di daftar `/`.
- [ ] Data tetap ada setelah server di-restart.

# Hint

- Urutan di dalam function `tambah()` penting: ambil data →
  `execute` → `commit` → `redirect`. Menukar urutan `commit` dan
  `redirect` tidak masalah, tapi `commit` harus SETELAH `execute`.
- Kalau data tidak muncul setelah submit tapi juga tidak ada error,
  cek dulu: apakah `db.commit()` benar-benar terpanggil?
- Jumlah `?` di query harus sama dengan jumlah nilai di tuple
  `(nama, nominal)` — dua `?`, dua nilai.

# Hasil Akhir

Form yang benar-benar menyimpan — pengeluaran yang kamu tambahkan
sekarang bertahan walau server dimatikan. Satu dari empat huruf CRUD
selesai, tiga lagi menyusul di folder berikutnya.

# Kesalahan Yang Sering Terjadi

- **Lupa `db.commit()`** → data terlihat masuk sesaat, tapi hilang
  lagi setelah restart server — gejala paling membingungkan buat
  pemula karena TIDAK ada pesan error sama sekali.
- **Nama kolom di query typo** (`nomianl` alih-alih `nominal`) →
  `sqlite3.OperationalError: table transactions has no column named
  nomianl`.
- **Jumlah placeholder `?` tidak cocok dengan jumlah nilai** →
  `sqlite3.ProgrammingError: Incorrect number of bindings supplied`.
- **Pakai f-string untuk menyisipkan nilai ke query** → berfungsi,
  tapi rawan SQL injection & jadi kebiasaan buruk sejak dini.
