# Solution · Challenge Medium

# Tujuan Belajar

Melihat satu cara valid mengaktifkan fitur search.

# Penjelasan

`repository.py` menambahkan kondisi `title LIKE ?` ke dalam list
`conditions` saat `search` terisi — pola yang PERSIS sama dengan
kondisi `category = ?` yang sudah ada di sampingnya.

# Diagram

```
search="kopi"  →  conditions.append("title LIKE ?")
                   params.append("%kopi%")
                            │
                            ▼
      WHERE title LIKE '%kopi%' [AND category = ?]
```

# Langkah Pengerjaan

1. Jalankan `python app.py`, coba search dengan & tanpa filter
   kategori aktif secara bersamaan.
2. Bandingkan dengan hasil kerjamu di `15-challenge/medium`.

# File Yang Diubah

- `repository.py`

# Checklist

- [ ] Search berfungsi sendiri maupun digabung dengan filter kategori.

# Hint

Kalau kamu menulis kondisinya dengan urutan `if` yang berbeda
(`category` dulu baru `search`), hasilnya tetap sama benarnya — SQL
`AND` tidak peduli urutan penulisan kondisinya.

# Hasil yang Diharapkan

Fitur search yang bekerja identik secara fungsi dengan punyamu di
`15-challenge/medium`.

# Refleksi

Fitur ini HANYA butuh perubahan di satu file (`repository.py`). Fitur
apa, kira-kira, yang PASTI butuh perubahan di `service.py` juga —
bukan cuma `repository.py`?
