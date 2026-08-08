# 03 · Template Render

# Tujuan

Memisahkan HTML dari Python, dan belajar menampilkan data Python di
dalam HTML lewat `render_template()` dan Jinja.

# Yang Dipelajari

- `render_template('index.html', data=...)` — mengirim halaman HTML
  sekaligus data Python ke dalamnya.
- `{{ ... }}` — menampilkan nilai variabel di HTML.
- `{% for ... %} ... {% endfor %}` — mengulang blok HTML untuk tiap
  item dalam list (loop), sama seperti `for` di Python.
- Folder `templates/` — wajib bernama persis itu, tempat Flask
  mencari file HTML.

# Penjelasan Konsep

Sampai sekarang, function route selalu me-return teks polos —
cukup untuk latihan, tapi halaman nyata butuh HTML lengkap (judul,
struktur, gaya). Menumpuk HTML sebagai string panjang di dalam
`app.py` akan cepat berantakan. Solusinya: taruh HTML di file
terpisah dalam folder `templates/`, dan gunakan `render_template()`
untuk menampilkannya — sekaligus menyisipkan data Python ke
dalamnya lewat Jinja.

# Langkah Pengerjaan

1. Buka `templates/index.html`, baca komentar di dalamnya.
2. Selesaikan `TODO 2` di `index.html` — tampilkan setiap transaksi
   sebagai `<li>` memakai `{% for %}`.
3. Selesaikan `TODO 1` di `app.py` — ganti return teks polos dengan
   `render_template('index.html', data=transaksi)`.
4. Jalankan `python app.py`, buka `localhost:5000`.

# File Yang Diubah

- `app.py`
- `templates/index.html`

# Checklist

- [ ] `render_template` sudah di-import dari `flask`.
- [ ] Route `/` me-return `render_template(...)`, bukan teks biasa.
- [ ] `templates/index.html` menampilkan 3 transaksi dalam daftar
      `<ul><li>`.
- [ ] Format tiap baris: `nama — Rp nominal`.

# Hint

- Nama variabel yang kamu kirim di `render_template('index.html',
  data=transaksi)` (yaitu `data`) HARUS sama persis dengan nama yang
  dipakai di `{% for t in data %}` pada file HTML — kalau beda, Jinja
  tidak akan menemukan apa-apa dan daftar tampil kosong (tanpa error).
- `{{ t.nama }}` bekerja karena tiap `t` adalah satu dict Python —
  Jinja otomatis mencoba `t['nama']` kalau `t.nama` tidak ditemukan
  sebagai atribut.
- Folder harus bernama persis `templates` (huruf kecil semua) —
  Flask mencarinya dengan nama itu secara otomatis, tidak bisa diganti
  sembarangan tanpa konfigurasi tambahan.

# Hasil Akhir

Halaman HTML sungguhan (bukan teks polos) yang menampilkan daftar
transaksi dari Python — fondasi tampilan untuk seluruh Expense
Tracker yang akan kita bangun selanjutnya.

# Kesalahan Yang Sering Terjadi

- **`TemplateNotFound`** → file HTML tidak ada di folder `templates/`,
  atau nama filenya salah ketik (`Index.html` vs `index.html`).
- **Lupa `{% endfor %}`** → Jinja melempar error saat merender,
  menyebutkan tag yang belum ditutup.
- **Nama variabel tidak cocok** antara `render_template(..., data=...)`
  dan `{% for t in data %}` → halaman tampil, tapi daftarnya kosong,
  tanpa pesan error sama sekali.
- **Menulis `{{ }}` untuk logika atau `{% %}` untuk menampilkan
  nilai** (tertukar) → Jinja error atau tidak menampilkan apa-apa.
