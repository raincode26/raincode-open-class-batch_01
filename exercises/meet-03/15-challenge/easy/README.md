# Challenge Easy · Kategori Berwarna

# Tujuan

Menambah sentuhan visual ke daftar transaksi — tiap kategori punya
warna chip yang berbeda, murni lewat CSS & Jinja `class` dinamis,
TANPA mengubah satu baris SQL pun.

# Yang Dipelajari

Memakai nilai dari database (`t.kategori`) untuk MENENTUKAN nama
`class` CSS secara dinamis di Jinja — pola yang sangat umum di
aplikasi nyata untuk styling berbasis data (bandingkan dengan
`CATEGORY_COLORS` di `projects/expense-tracker/final` yang kamu baca di
`12-read-source-code`).

# Penjelasan Konsep

`app.py` di folder ini SUDAH LENGKAP (CRUD + kategori + tanggal,
seperti hasil `11-complete-crud`). Fitur ini murni tampilan: filter
`{{ t.kategori|lower }}` mengubah "Makanan" jadi "makanan" saat
dipakai sebagai bagian nama class CSS (`kategori-makanan`), supaya
kamu bisa menulis satu aturan CSS per kategori.

# Langkah Pengerjaan

1. Selesaikan `TODO 1` di `templates/index.html` — bungkus kategori
   dengan `<span class="kategori kategori-{{ t.kategori|lower }}">`.
2. Selesaikan `TODO 2` di `static/style.css` — beri warna berbeda
   untuk tiap `.kategori-...`.
3. Jalankan `python app.py`, tambah beberapa transaksi dengan
   kategori berbeda-beda, lihat hasilnya.

# File Yang Diubah

- `templates/index.html`
- `static/style.css`

# Checklist

- [ ] Tiap kategori tampil sebagai chip berwarna, bukan teks polos.
- [ ] Warna tiap kategori BERBEDA satu sama lain.
- [ ] Tidak ada perubahan di `app.py` — fitur ini murni CSS & Jinja.

# Hint

- Filter Jinja ditulis dengan tanda `|`, contoh: `{{ nilai|lower }}`
  — mengubah teks jadi huruf kecil semua.
- Nama class CSS sebaiknya tidak mengandung spasi — kalau kategori
  punya spasi (di latihan ini tidak ada), pertimbangkan mengganti
  spasi jadi tanda hubung juga.
- Kalau warnanya tidak muncul, cek dulu di tab **Elements** DevTools:
  apakah class `kategori-makanan` (atau lainnya) benar-benar
  terpasang di elemen `<span>`?

# Hasil Akhir

Daftar transaksi yang jauh lebih mudah dipindai sekilas — kategori
langsung terlihat dari warnanya, tanpa perlu membaca teksnya
satu-satu.
