# 04 · HTML Analysis

# Tujuan Belajar

Membaca `templates/*.html` di `projects/expense-tracker/final/` dan
memahami KENAPA setiap file terlihat seperti itu — bukan menulis ulang
satu baris pun.

# Penjelasan

Ada 7 file HTML: `base.html`, `index.html`, `expenses.html`,
`create.html`, `edit.html`, `summary.html`, dan `errors/404.html` +
`errors/500.html`. Yang menarik: **tidak ada file `detail.html` atau
`delete.html`** — dua hal yang mungkin kamu duga akan ada, ternyata
tidak dibuat sebagai halaman terpisah. Itu keputusan desain, bukan
sesuatu yang "kurang" — kamu akan buktikan alasannya sendiri.

Poin penting yang perlu kamu temukan sambil membaca:

- `base.html` adalah **layout induk** — nav, flash message, DAN modal
  konfirmasi hapus semuanya didefinisikan SEKALI di sini, lalu dipakai
  ulang oleh halaman lain lewat `{% extends "base.html" %}` dan
  `{% block content %}`.
- `expenses.html` (halaman daftar) punya form filter yang memakai
  method `GET`, bukan `POST` — perhatikan kenapa (petunjuk: coba
  refresh halaman hasil filter, apa yang terjadi pada URL-nya?).
- `create.html` punya atribut `novalidate` di tag `<form>` — itu
  SENGAJA mematikan validasi bawaan browser, karena validasi "asli"
  ada di JavaScript (tampilan) DAN di `services/` (yang sesungguhnya
  menentukan).
- `edit.html` memakai pola `form_data.get('field', expense.field)` —
  kalau form baru pertama dibuka, tampilkan data asli dari database;
  kalau user baru saja submit tapi validasi gagal, tampilkan lagi
  apa yang tadi mereka ketik (supaya tidak perlu ngetik ulang dari
  nol).

# Diagram

```
base.html  ──extends──▶  index.html
    │        ──extends──▶  expenses.html
    │        ──extends──▶  create.html
    │        ──extends──▶  edit.html
    │        ──extends──▶  summary.html
    │
    └── berisi SEKALI: <nav>, flash messages, modal hapus
        (semua halaman anak otomatis mewarisi ini)
```

# Langkah Pengerjaan

1. Buka `templates/base.html`. Cari blok `{% block content %}`.
   Semua halaman lain nanti "mengisi" blok kosong ini dengan isinya
   masing-masing.
2. Buka `templates/expenses.html`. Cari tag `<form>` paling atas
   (form filter). Catat: `method="..."` isinya apa? Kenapa BUKAN
   `POST`? (Hint: method `GET` membuat filter/pencarian bisa
   di-bookmark & di-share sebagai link, karena semua parameternya
   terlihat di URL — `POST` menyembunyikannya.)
3. Masih di `expenses.html`, cari tombol Hapus di tiap baris tabel.
   Perhatikan atributnya (`onclick="openDeleteModal(...)"`) — ini
   TIDAK langsung menghapus, ia memanggil JavaScript yang akan kamu
   telusuri lebih lanjut kalau membuka `static/js/app.js`.
4. Buka `templates/create.html`. Cari `{{ form_data.get('title', '')
   }}`. Bandingkan dengan `templates/edit.html` yang punya
   `{{ form_data.title }}` — kenapa `create.html` butuh `.get(...)`
   dengan default kosong, sementara `edit.html` bisa lebih pendek?
   (Hint: expense yang di-edit SUDAH PASTI ada datanya, expense baru
   belum tentu ada input sama sekali di percobaan pertama.)
5. Buka `templates/errors/404.html` dan `errors/500.html`. Ini
   halaman yang tampil saat `app.py` memanggil
   `render_template('errors/404.html')` di dalam `@app.errorhandler`.
   Baca — apakah keduanya menampilkan pesan yang sama, atau beda?

# File Yang Diubah

Tidak ada — folder ini murni membaca.

# Checklist

- [ ] Bisa menyebutkan isi `{% block content %}` di MASING-MASING
      halaman anak (index, expenses, create, edit, summary) dalam
      satu kalimat per halaman.
- [ ] Tahu kenapa form filter di `expenses.html` memakai `GET`.
- [ ] Menemukan bahwa TIDAK ADA halaman `detail.html` atau
      `delete.html` terpisah, dan punya dugaan kenapa (jawabannya ada
      di `05-css-analysis` & saat membaca `static/js/app.js`).

# Hint

- Baca `templates/base.html` DULUAN, sebelum halaman lain — semua
  halaman lain "numpang" ke layout ini, jadi tidak akan masuk akal
  kalau dibaca sendiri-sendiri dulu.
- Jinja2 punya dua jenis tag: `{{ }}` untuk MENAMPILKAN nilai, `{% %}`
  untuk LOGIKA (perulangan, kondisi, extends/block). Kalau bingung
  satu baris HTML "aneh", tanya dulu: itu tag `{{ }}` atau `{% %}`?
- `{% for expense in expenses %}` di `expenses.html` sama persis
  konsepnya dengan `{% for t in data %}` yang kamu tulis sendiri di
  `meet-03/06-create-table` — hanya nama variabelnya beda.

# Hasil yang Diharapkan

Kamu bisa menjawab: "kalau saya ingin tahu HTML apa yang tampil untuk
sebuah expense di halaman daftar, saya baca file mana, baris berapa?"
— dalam hitungan detik, tanpa scroll acak.

# Refleksi

1. Kenapa modal konfirmasi hapus didefinisikan SEKALI di `base.html`,
   bukan diulang di `expenses.html` DAN `edit.html` (dua tempat yang
   sama-sama punya tombol Hapus)? Apa yang akan rusak/merepotkan kalau
   didefinisikan dua kali?
2. Bandingkan `create.html` dan `edit.html` — sebutkan MINIMAL dua
   perbedaan struktural (bukan cuma judul halamannya) dan jelaskan
   alasan tiap perbedaan itu.
