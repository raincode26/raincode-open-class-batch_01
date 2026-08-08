# Solution · Challenge Easy

# Tujuan Belajar

Melihat satu cara valid menyelesaikan badge kategori berwarna.

# Penjelasan

`templates/index.html` membungkus `{{ e.category }}` dengan
`<span class="kategori kategori-{{ e.category|lower }}">`, dan
`static/style.css` mendefinisikan warna untuk tiap kombinasi class
yang mungkin muncul (`kategori-food`, `kategori-transport`, dst).

# Diagram

```
category = "Food"  →  |lower  →  "food"  →  class="kategori-food"
                                                    │
                                                    ▼
                                     CSS: .kategori-food { warna }
```

# Langkah Pengerjaan

1. Jalankan `python app.py`, tambah expense dengan kategori berbeda.
2. Bandingkan hasilnya dengan yang kamu buat sendiri di
   `15-challenge/easy`.

# File Yang Diubah

- `templates/index.html`
- `static/style.css`

# Checklist

- [ ] Badge berwarna sesuai kategori tampil di halaman `/`.

# Hint

Kalau punyamu tampilannya beda (warna berbeda, urutan style berbeda)
tapi badge-nya tetap muncul dengan benar per kategori — itu tetap
valid, tidak perlu sama persis.

# Hasil yang Diharapkan

Tabel expense dengan kategori berwarna, identik secara FUNGSI dengan
punyamu di `15-challenge/easy`.

# Refleksi

Apakah warna yang dipakai di sini penting secara fungsional, atau
murni pilihan estetika? Bagian mana dari solusi ini yang SEBENARNYA
"wajib" secara teknis?
