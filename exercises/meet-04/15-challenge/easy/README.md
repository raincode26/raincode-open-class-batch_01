# Challenge Easy · Kategori Berwarna

# Tujuan Belajar

Menyelesaikan challenge PERTAMA tanpa tuntunan langkah-demi-langkah
sedetail folder sebelumnya — hanya diberi tujuan akhir & dua TODO
sebagai penunjuk arah.

# Penjelasan

Semua backend (`app.py`, `service.py`, `repository.py`,
`database.py`) di folder ini SUDAH LENGKAP — jangan diubah. Yang
belum selesai murni tampilan: kolom Category di tabel daftar expense
masih polos teks biasa. Tugasmu: buat tiap kategori tampil sebagai
badge berwarna, seperti label di aplikasi to-do list atau issue
tracker.

# Diagram

```
SEBELUM                          SESUDAH

Title | Amount | Category        Title | Amount | Category
Kopi  | 25000  | Food             Kopi  | 25000  | 🟠 Food
```

# Langkah Pengerjaan

1. Buka `templates/index.html`, cari `TODO 1`.
2. Buka `static/style.css`, cari `TODO 2`.
3. Selesaikan keduanya, jalankan `python app.py`, tambah beberapa
   expense dengan kategori berbeda-beda, lihat hasilnya di `/`.

# File Yang Diubah

- `templates/index.html`
- `static/style.css`

# Checklist

- [ ] Kolom Category di tabel menampilkan badge berwarna, bukan teks
      polos.
- [ ] Warna berbeda untuk MINIMAL 3 kategori berbeda.
- [ ] Fitur lain (Add, Edit, Delete, Search, Filter) tetap bekerja
      normal.

# Hint

- Filter Jinja `|lower` mengubah teks jadi huruf kecil semua — dipakai
  supaya nama class CSS konsisten huruf kecil, terlepas dari
  bagaimana `category` tersimpan di database.
- Kalau warnanya tidak muncul, cek dulu: apakah nama class di HTML
  (`kategori-food`) PERSIS sama dengan nama class di CSS
  (`.kategori-food`)? Titik/spasi yang salah bisa membuat browser
  diam-diam mengabaikannya.

# Hasil yang Diharapkan

Tabel daftar expense dengan kategori yang mudah dibedakan sekilas
pandang lewat warna, tanpa mengubah satu baris pun kode backend.

# Refleksi

Kenapa fitur visual seperti ini TIDAK butuh perubahan apa pun di
`service.py` atau `repository.py`? Fitur macam apa yang PASTI butuh
perubahan di kedua file itu?
