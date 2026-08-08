# Bug 1 · Route Salah

# Tujuan Belajar

Melatih mata mencocokkan atribut `action` di `<form>` dengan path yang
didaftarkan di `@app.route(...)`.

# Penjelasan

Form HTML tidak tahu apa-apa soal Python — ia cuma tahu "kirim data
ke alamat X". Kalau alamat X itu tidak terdaftar sebagai route di
`app.py`, Flask tidak tahu harus memanggil function mana, dan
menjawab dengan halaman 404 bawaan.

# Diagram

```
templates/create.html                app.py

<form action="/simpan" ...>    ✗    @app.route("/create", ...)
        │                                    │
        └──── TIDAK ADA YANG COCOK ──────────┘
                        │
                        ▼
                 404 Not Found
```

# Langkah Pengerjaan

1. Jalankan `python app.py`, buka `/create`, isi form, klik Simpan.
2. Amati: halaman apa yang muncul?
3. Buka `templates/create.html`, cari atribut `action` di tag
   `<form>`.
4. Buka `app.py`, cari route yang menangani penyimpanan expense baru
   (method POST).
5. Bandingkan keduanya — samakan.

# File Yang Diubah

- `templates/create.html`

# Checklist

- [ ] `action` di `create.html` PERSIS sama dengan path route POST di
      `app.py`.
- [ ] Submit form tidak lagi menampilkan 404.
- [ ] Expense baru berhasil tersimpan & muncul di halaman daftar.

# Hint

- Jangan ubah `app.py` — cukup samakan `action` di HTML dengan path
  yang SUDAH benar di Python.
- 404 dari Flask selalu berarti: "tidak ada `@app.route` yang cocok
  dengan URL + method ini". Ini bukan soal database atau validasi
  sama sekali.

# Hasil yang Diharapkan

Form Add Expense yang berhasil mengirim data ke route yang benar.

# Refleksi

Kalau kamu mengganti path route di `app.py` (bukan `action` di HTML),
apa risikonya kalau ada file LAIN yang juga memakai
`url_for("create")` untuk menghasilkan link ke halaman ini?
