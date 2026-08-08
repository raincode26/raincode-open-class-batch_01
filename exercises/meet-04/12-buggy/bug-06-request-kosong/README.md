# Bug 6 · Request Kosong

# Tujuan Belajar

Melatih mata mencocokkan atribut `name` di HTML dengan kunci yang
dipakai di `request.form.get(...)` — kesalahan yang gejalanya
menyesatkan karena TIDAK ada error sama sekali, cuma penolakan yang
membingungkan.

# Penjelasan

`request.form.get("title")` mencari field form yang atribut
`name`-nya PERSIS `"title"`. Kalau di HTML atribut itu ternyata
`name="judul"`, Flask TIDAK error — ia cuma mengembalikan string
kosong (karena dipanggil dengan `.get()`, bukan `["title"]`). String
kosong itu lalu ditolak oleh validasi di `service.py` dengan pesan
"Title wajib diisi." — padahal user MERASA sudah mengisinya.

# Diagram

```
templates/create.html                    service.py

<input name="judul" ...>          ✗      form_data.get("title", "")
       (user mengetik "Kopi")                    │
                                                   ▼
                                          "" (string kosong, "title"
                                           tak pernah ditemukan)
                                                   │
                                                   ▼
                                    ValueError("Title wajib diisi.")
```

# Langkah Pengerjaan

1. Jalankan `python app.py`, buka `/create`.
2. Isi Title dengan "Kopi pagi", isi Amount dengan `25000`, pilih
   category, klik Simpan.
3. Amati: pesan apa yang muncul? Padahal Title SUDAH diisi, bukan?
4. Buka `templates/create.html`, catat SEMUA atribut `name` di tiap
   `<input>`.
5. Buka `service.py`, bandingkan dengan semua `form_data.get(...)`
   yang dipakai di `_validate`.

# File Yang Diubah

- `templates/create.html`

# Checklist

- [ ] Atribut `name` di input Title kembali `name="title"`.
- [ ] Mengisi form dengan data valid tidak lagi ditolak dengan pesan
      "Title wajib diisi."
- [ ] Expense baru berhasil tersimpan dengan title yang benar.

# Hint

- Jangan ubah `service.py` — ia SUDAH benar (mencari `"title"`).
  Yang salah adalah atribut `name` di HTML.
- `request.form.get("nama_field")` TIDAK PERNAH error kalau field-nya
  tidak ada — hasilnya selalu string kosong `""`. Ini beda dengan
  `request.form["nama_field"]` (pakai kurung siku) yang akan menolak
  request-nya sama sekali kalau field tidak ditemukan
  (`BadRequestKeyError`).

# Hasil yang Diharapkan

Form Add Expense yang menerima input title dengan benar, bukan selalu
menolaknya sebagai "kosong".

# Refleksi

Bug ini TIDAK menghasilkan error/traceback sama sekali — cuma pesan
validasi yang terasa "salah". Kenapa bug seperti ini justru lebih
sulit ditemukan dibanding bug-bug lain di folder ini yang langsung
menampilkan error 500?
