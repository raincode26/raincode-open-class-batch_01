# Solusi · Challenge Medium

# Tujuan

Referensi pembanding untuk `15-challenge/medium`.

# Yang Dipelajari

Cara membangun query `SELECT` yang berubah bentuk tergantung ada
tidaknya filter dari user, dan membaca filter itu dari `request.args`
(bukan `request.form`).

# File Yang Diubah

Tidak ada — folder ini untuk dibaca, bukan diedit.

# Langkah Pengerjaan

1. `request.args.get('kategori')` dipanggil di AWAL function, sebelum
   query apa pun dijalankan — hasilnya bisa `None` atau sebuah teks.
2. `if kategori_filter:` memilih salah satu dari dua bentuk query:
   dengan `WHERE` (kalau ada filter) atau tanpa (kalau tidak).
3. `kategori_filter` tetap dikirim ke `render_template(...)` supaya
   HTML tahu pilihan mana yang harus ditandai `selected` di dropdown.

# Hint

Perhatikan: kedua cabang `if/else` di sini MENGEMBALIKAN bentuk data
yang SAMA (list of Row) — beda hanya query SQL-nya. Ini penting
supaya `templates/index.html` tidak perlu tahu atau peduli apakah
sedang difilter atau tidak.

# Checklist

- [ ] Sudah membandingkan dengan hasil kerjaku sendiri di `15-challenge/medium`.

# Hasil Akhir

Filter kategori yang bekerja lewat URL, memakai `WHERE` dinamis
berdasarkan pilihan user.
