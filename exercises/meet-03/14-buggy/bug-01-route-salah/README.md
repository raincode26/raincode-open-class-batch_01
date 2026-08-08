# Bug 1 · Route Salah

# Tujuan

Melatih mata mencocokkan alamat `action` di HTML dengan alamat
`@app.route` di Python.

# Yang Dipelajari

Route hanya menerima request yang alamatnya PERSIS cocok. Alamat
yang hampir sama tetap dianggap alamat yang berbeda.

# Penjelasan Konsep

`404 Not Found` selalu berarti satu hal: Flask tidak punya route
yang cocok dengan alamat yang diminta. Ini bukan error "kode Python
rusak" — kodenya berjalan sempurna, cuma alamatnya tidak
ditemukan.

# Langkah Pengerjaan

1. Jalankan `python app.py`, buka `localhost:5000`.
2. Isi form, klik Simpan.
3. Amati halaman error yang muncul.
4. Buka `templates/index.html` dan `app.py`, bandingkan alamatnya.

# File Yang Diubah

- Perbaiki salah satu: `templates/index.html` (atribut `action`) ATAU
  `app.py` (`@app.route(...)`) — supaya keduanya cocok.

# Checklist

- [ ] Alamat di `action="..."` sama persis dengan alamat di
      `@app.route(...)`.
- [ ] Klik Simpan tidak lagi menampilkan halaman 404.
- [ ] Transaksi baru muncul di daftar setelah disimpan.

# Hint

- Baca alamat di URL bar browser saat halaman error muncul — itu
  alamat yang sebenarnya diminta.
- Cek juga: apakah route yang benar sudah didaftarkan dengan
  `methods=['POST']`? (Kalau alamatnya sudah cocok tapi masih error,
  cek kemungkinan lain: `405 Method Not Allowed`.)

# Hasil Akhir

Form yang berhasil mengirim data ke route yang benar.

# Kesalahan Yang Sering Terjadi

Setelah diperbaiki, pastikan tidak ada route lain di `app.py` yang
kebetulan memakai alamat yang sama — dua route dengan alamat identik
akan membuat Flask bingung (atau salah satu jadi tak terpakai).
