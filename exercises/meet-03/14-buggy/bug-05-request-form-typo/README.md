# Bug 5 · request.form Typo

# Tujuan

Melatih mata mencocokkan atribut `name` di HTML dengan kunci yang
dipakai di `request.form[...]`.

# Yang Dipelajari

`request.form['sesuatu']` mencari field form yang atribut
`name`-nya PERSIS `"sesuatu"`. Kalau tidak ada field dengan nama itu
di form yang dikirim, Flask menolak requestnya sama sekali dengan
error `400 Bad Request`.

# Penjelasan Konsep

Penyebab aslinya adalah `werkzeug.exceptions.BadRequestKeyError`
(setara `400 Bad Request`) — artinya PYTHON meminta field yang TIDAK
PERNAH dikirim oleh form itu. Tapi karena aplikasi ini jalan dengan
`debug=True`, Flask menampilkan SEMUA error lewat halaman debugger
interaktif dengan kode `500`, apa pun jenis error aslinya — baca
baris PALING BAWAH traceback-nya untuk tahu error yang sesungguhnya
(`BadRequestKeyError`), bukan cuma kode status di judul halaman.

# Langkah Pengerjaan

1. Jalankan `python app.py`, isi form, klik Simpan.
2. Baca traceback di halaman debugger — cari baris
   `BadRequestKeyError` di paling bawah.
3. Buka `templates/index.html`, catat semua atribut `name` di
   `<input>`.
4. Buka `app.py`, bandingkan dengan semua `request.form[...]` yang
   dipakai.

# File Yang Diubah

- `app.py` — samakan kunci di `request.form[...]` dengan atribut
  `name` yang benar-benar ada di form.

# Checklist

- [ ] Semua `request.form[...]` di `app.py` memakai nama yang PERSIS
      sama dengan atribut `name` di `templates/index.html`.
- [ ] Klik Simpan tidak lagi menampilkan error 400.
- [ ] Transaksi baru tersimpan dengan nominal yang benar.

# Hint

- Jangan tergoda mengubah HTML-nya — cukup samakan nama yang dipakai
  di Python.
- `request.form.get('nama')` (pakai `.get()`) tidak akan error kalau
  field tak ditemukan — hasilnya `None`. `request.form['nama']`
  (pakai kurung siku) akan langsung menolak request kalau field-nya
  tidak ada. Keduanya valid, tapi perilakunya beda saat field hilang.

# Hasil Akhir

Form yang berhasil mengirim data dengan field yang benar-benar
dikenali Python.

# Kesalahan Yang Sering Terjadi

Ini sering terjadi setelah mengganti nama variabel di Python
(misalnya dari `jumlah` ke `nominal`) tapi lupa mengecek apakah nama
itu juga dipakai konsisten di semua tempat, termasuk atribut `name`
di HTML.
