# 05 · CSS Analysis

# Tujuan Belajar

Membaca `static/css/style.css` (1400+ baris) tanpa tenggelam —
memahami bagaimana file CSS BESAR sungguhan diorganisir, dan
bagaimana ia "terhubung" balik ke data di Python.

# Penjelasan

1400 baris CSS terdengar menakutkan, tapi file ini TIDAK ditulis
sebagai tumpukan acak — ia punya daftar isi di bagian paling atas
(komentar section header), persis seperti daftar isi buku. Kamu tidak
akan pernah membaca 1400 baris dari atas ke bawah; kamu akan LOMPAT ke
section yang relevan.

Tiga hal penting yang menghubungkan CSS ini ke bagian lain project:

- **CSS Variables** (`:root { --color-primary: ...; }`) di paling
  atas file — semua warna didefinisikan SEKALI sebagai variabel, lalu
  dipakai berulang-ulang lewat `var(--nama-variabel)`. Ganti satu
  variabel, semua tempat yang memakainya ikut berubah.
- **Warna per kategori** (`--cat-food`, `--cat-transportation`, dst.)
  — variabel ini SENGAJA namanya cocok dengan `CATEGORY_COLORS` di
  `models/expense_model.py` DAN di `static/js/app.js`. Tiga file
  berbeda, satu daftar warna yang sama, disebut tiga kali dengan cara
  berbeda (Python dict, CSS variable, JS object).
- **Responsive breakpoints** di bagian paling bawah (`@media
  (max-width: 768px) { ... }`) — aturan yang HANYA berlaku di layar
  kecil, ditulis terpisah dari aturan "normal"-nya.

# Diagram

```
Satu warna kategori, disebut di 3 tempat:

models/expense_model.py          static/css/style.css        static/js/app.js
CATEGORY_COLORS = {              :root {                     CATEGORY_COLORS = {
  "Food": "#f97316",   ◀───────▶   --cat-food: #f97316;  ◀──▶   Food: "#f97316",
  ...                             }                           ...
}                                                              }
```

# Langkah Pengerjaan

1. Buka `static/css/style.css`. Cari (`Ctrl+F`) baris-baris yang
   diawali `/* ─` — itu section header, semacam daftar isi. Baca
   SEMUA judul section-nya saja (jangan baca isi tiap section dulu).
   Berapa banyak section yang ada?
2. Cari blok `:root { ... }` di paling atas. Temukan variabel
   `--color-primary`. Cari (pencarian global di seluruh file CSS)
   berapa kali `var(--color-primary)` dipakai di bawahnya.
3. Cari variabel `--cat-food` (atau kategori lain). Lalu buka
   `models/expense_model.py`, cari `CATEGORY_COLORS`. Bandingkan kode
   warnanya (hex) — apakah sama persis?
4. Cari section CSS untuk `.table` atau `table` (styling tabel di
   halaman daftar expense). Baca aturan yang berlaku untuk baris tabel
   saat mouse di-hover (`:hover`).
5. Scroll ke paling bawah file, cari `@media (max-width: 768px)`.
   Baca 5-10 baris pertama di dalamnya — aturan apa yang berubah di
   layar kecil?

# File Yang Diubah

Tidak ada — folder ini murni membaca.

# Checklist

- [ ] Bisa menyebutkan MINIMAL 5 judul section dari daftar isi CSS
      ini, dari ingatan.
- [ ] Menemukan sendiri bahwa kode warna kategori di CSS, di
      `models/expense_model.py`, dan (kalau sempat dicek) di
      `static/js/app.js` adalah NILAI YANG SAMA, ditulis tiga kali.
- [ ] Paham apa itu `@media (max-width: ...)` — aturan yang HANYA
      aktif di ukuran layar tertentu.

# Hint

- CSS Variables (`--nama: nilai;` lalu dipakai lewat `var(--nama)`)
  adalah pola yang HAMPIR SELALU dipakai di project CSS besar —
  kalau kamu paham konsep ini di sini, kamu akan langsung mengenalinya
  di project lain.
- Jangan coba menghafal isi CSS-nya. Tujuan folder ini adalah paham
  CARA MENCARI di file besar (lewat daftar isi/section header &
  pencarian teks), bukan menghafal aturan CSS satu-satu.
- Kalau bingung kenapa satu warna disebut tiga kali di tiga bahasa
  berbeda (bukan didefinisikan sekali lalu "dibagi"): itu karena
  Python, CSS, dan JavaScript adalah tiga "dunia" terpisah yang
  berjalan di tempat berbeda (server vs browser) — mereka tidak bisa
  saling membaca variabel satu sama lain secara langsung.

# Hasil yang Diharapkan

Kamu tidak lagi takut membuka file CSS ribuan baris — kamu tahu harus
mulai dari daftar isi, lalu `Ctrl+F` ke section yang relevan.

# Refleksi

1. Apa risikonya kalau warna kategori "Food" perlu diganti, dan kamu
   HARUS mengubahnya di tiga file berbeda (CSS, Python, JS) secara
   manual satu-satu? Bug macam apa yang bisa muncul kalau kamu lupa
   mengubah salah satunya?
2. Kenapa aturan CSS untuk layar kecil (`@media`) ditulis TERPISAH di
   bagian bawah file, bukan dicampur langsung di tiap aturan aslinya?
