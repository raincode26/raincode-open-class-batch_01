# Solusi · Challenge Easy

# Tujuan

Referensi pembanding untuk `15-challenge/easy`.

# Yang Dipelajari

Cara memakai nilai dari database untuk membangun nama `class` CSS
secara dinamis lewat Jinja, tanpa menyentuh SQL sama sekali.

# File Yang Diubah

Tidak ada — folder ini untuk dibaca, bukan diedit.

# Langkah Pengerjaan

1. `{{ t.kategori|lower }}` mengubah "Makanan" jadi "makanan" saat
   dirender, sehingga cocok dengan penamaan `.kategori-makanan` di
   CSS.
2. Setiap kategori diberi satu aturan CSS terpisah — warna latar
   (`background`) dan warna teks (`color`) yang kontras satu sama
   lain.

# Hint

Bandingkan pendekatan ini dengan `CATEGORY_COLORS` di
`projects/expense-tracker/final/models/expense_model.py` — polanya mirip
(satu warna per kategori), meski project nyata menyimpannya sebagai
dictionary Python, bukan CSS class per kategori.

# Checklist

- [ ] Sudah membandingkan dengan hasil kerjaku sendiri di `15-challenge/easy`.

# Hasil Akhir

Chip kategori berwarna yang membuat daftar transaksi lebih mudah
dipindai sekilas.
