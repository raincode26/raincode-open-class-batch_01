# 02 · Route

# Tujuan

Memahami bahwa satu aplikasi Flask boleh punya banyak alamat
(route), dan alamat itu bisa dibuat dinamis lewat parameter.

# Yang Dipelajari

- `route` = alamat halaman, seperti alamat rumah yang menentukan
  surat diantar ke mana.
- Satu aplikasi = banyak `@app.route(...)`, masing-masing dengan
  function-nya sendiri.
- Route dinamis: `@app.route('/halo/<nama>')` menangkap bagian
  alamat sebagai parameter yang bisa dipakai di dalam function.

# Penjelasan Konsep

Di `01-flask-hello-world` kamu hanya punya satu alamat: `/`. Aplikasi
nyata (termasuk Expense Tracker kita nanti) butuh banyak alamat:
satu untuk halaman utama, satu untuk tambah data, satu untuk edit,
satu untuk hapus. Route dinamis (`<nama>` atau nanti `<id>`) penting
karena `/edit/1` dan `/edit/2` seharusnya TIDAK butuh dua function
terpisah — cukup satu function yang menerima `id` sebagai parameter.

# Langkah Pengerjaan

1. Route `/` sudah lengkap — baca dulu polanya.
2. Ikuti `TODO 1` dan `TODO 2` untuk menambah dua route statis.
3. Ikuti `TODO 3` untuk menambah satu route dinamis.
4. Jalankan `python app.py`, lalu coba buka semua alamatnya satu per
   satu di browser: `/`, `/tentang`, `/kontak`, `/halo/Budi`,
   `/halo/<namamu-sendiri>`.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] `/tentang` menampilkan teks penjelasan aplikasi.
- [ ] `/kontak` menampilkan teks kontak.
- [ ] `/halo/Budi` menampilkan sapaan untuk "Budi".
- [ ] `/halo/<nama-lain>` menampilkan sapaan yang ikut berubah sesuai
      alamatnya — tanpa mengubah kode.

# Hint

- Nama function boleh apa saja, tapi TIDAK BOLEH ada dua function
  dengan nama yang sama dalam satu file — Python akan bingung.
- Parameter di `<nama>` otomatis jadi teks (string) yang bisa
  langsung dipakai di f-string, sama seperti variabel biasa.
- Kalau lupa mengetik `<...>` di route, alamat itu jadi statis dan
  tidak bisa menangkap apa pun dari URL.

# Hasil Akhir

Empat alamat berbeda yang dilayani satu aplikasi Flask — termasuk
satu alamat dinamis yang bisa melayani nama siapa pun tanpa menulis
ulang kode.

# Kesalahan Yang Sering Terjadi

- **Dua route sama persis** (`@app.route('/tentang')` ditulis dua
  kali) → hanya yang pertama yang pernah terpanggil, Flask tak akan
  error, tapi function kedua jadi "mati".
- **Lupa parameter di nama function**, misal
  `@app.route('/halo/<nama>')` tapi `def sapa():` (tanpa `nama`) →
  `TypeError`, function tidak tahu harus menerima apa.
- **Salah ketik alamat saat membuka di browser** (`/Halo/Budi` dengan
  H besar) → Flask, secara default, membedakan huruf besar/kecil di
  alamat, hasilnya 404.
