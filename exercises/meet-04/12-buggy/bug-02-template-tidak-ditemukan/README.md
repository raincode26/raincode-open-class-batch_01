# Bug 2 · Template Tidak Ditemukan

# Tujuan Belajar

Mengenali error `TemplateNotFound` dan tahu persis dua tempat yang
harus dicocokkan: nama file di `render_template(...)` vs nama file
sungguhan di folder `templates/`.

# Penjelasan

`render_template("nama_file.html", ...)` mencari file PERSIS dengan
nama itu di dalam folder `templates/`. Kalau file dengan nama itu
tidak ada (typo, atau memang belum pernah dibuat), Flask menjawab
dengan error 500 dan traceback `jinja2.exceptions.TemplateNotFound`.

# Diagram

```
app.py                              templates/

render_template(               ✗    index.html   (file yang SEBENARNYA ada)
    "expense_list.html", ...
)
        │
        └──── TIDAK ADA FILE INI DI templates/ ────┐
                                                     ▼
                                    500 + TemplateNotFound: expense_list.html
```

# Langkah Pengerjaan

1. Jalankan `python app.py`, buka `/`.
2. Baca halaman debugger Flask — cari baris paling bawah traceback:
   `jinja2.exceptions.TemplateNotFound: ...`.
3. Buka folder `templates/`, lihat nama file yang BENAR-BENAR ada di
   sana.
4. Buka `app.py`, cari `render_template(...)` yang memakai nama file
   yang TIDAK ada itu.
5. Perbaiki.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] Nama file di `render_template(...)` pada route `/` sekarang
      cocok dengan file yang benar-benar ada di `templates/`.
- [ ] Buka `/` tidak lagi menampilkan halaman debugger.

# Hint

- JANGAN buat file baru bernama `expense_list.html` — solusinya
  memperbaiki NAMA yang salah ketik di `app.py`, bukan menyesuaikan
  folder `templates/` ke nama yang salah.
- Nama file di `render_template(...)` HARUS PERSIS sama (termasuk
  huruf besar/kecil di beberapa sistem operasi) dengan nama file di
  disk.

# Hasil yang Diharapkan

Halaman `/` kembali menampilkan dashboard dengan benar.

# Refleksi

Kenapa error `TemplateNotFound` muncul sebagai 500 (bukan 404),
padahal secara konsep terasa mirip "file tidak ditemukan"? Bandingkan
dengan alasan kenapa 404 muncul di `bug-01-route-salah`.
