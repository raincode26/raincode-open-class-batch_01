# 15 · Challenge

# Tujuan Belajar

Menguji seluruh skill membaca & mengubah kode dari `meet-04` lewat
tiga tingkat kesulitan — dengan tuntunan yang semakin sedikit di
setiap tingkat.

# Penjelasan

| Tingkat | Nama | Yang dikerjakan | Lapisan yang disentuh |
|---|---|---|---|
| [easy](easy) | Kategori Berwarna | Badge warna per kategori | Template, CSS saja |
| [medium](medium) | Aktifkan Search | Lengkapi satu query yang belum aktif | Repository saja |
| [hard](hard) | Cegah Title Duplikat | Validasi yang bertanya ke database dulu | Repository + Service |

Ketiganya berdiri sendiri (masing-masing app Flask independen,
`python app.py` di folder masing-masing) — tidak perlu dikerjakan
berurutan, tapi disarankan easy → medium → hard karena tuntunannya
memang dirancang semakin longgar.

# Diagram

```
easy    → sentuh 1 lapisan   (Template/CSS)
medium  → sentuh 1 lapisan   (Repository)
hard    → sentuh 2 lapisan   (Repository + Service, saling terhubung)
```

# Langkah Pengerjaan

1. Masuk ke `easy/`, baca README-nya, selesaikan.
2. Lanjut ke `medium/`, baca README-nya, selesaikan.
3. Lanjut ke `hard/`, baca README-nya, selesaikan.
4. Kalau macet di salah satu, boleh intip `16-solution/` — tapi coba
   dulu minimal 15 menit sendiri sebelum membuka kunci jawaban.

# File Yang Diubah

Bervariasi per tingkat — lihat README masing-masing folder.

# Checklist

- [ ] Ketiga tingkat (easy, medium, hard) sudah diselesaikan dan
      dites lewat browser.
- [ ] Untuk masing-masing, bisa menjelaskan lapisan mana yang
      disentuh dan kenapa.

# Hint

- Semakin tinggi tingkatnya, semakin sedikit contoh kode yang
  diberikan di README — itu disengaja, meniru situasi nyata di mana
  tiket kerja jarang menjelaskan detail implementasi.
- Kalau benar-benar buntu, folder `12-buggy` dan `13-refactor` adalah
  rujukan pola struktur file yang sama persis (app.py + service.py +
  repository.py + database.py).

# Hasil yang Diharapkan

Tiga aplikasi kecil yang masing-masing punya SATU fitur baru berhasil
ditambahkan olehmu sendiri, dengan tingkat tuntunan yang berbeda-beda.

# Refleksi

Dari ketiga tingkat, mana yang terasa paling dekat dengan "tugas kerja
sungguhan" — instruksi singkat, tuntunan minim, kamu yang harus
menelusuri sendiri di mana perubahan perlu dilakukan?
