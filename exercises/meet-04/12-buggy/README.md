# 12 · Buggy

# Tujuan Belajar

Memperbaiki bug NYATA di project yang bisa dijalankan — bukan cuma
mendiagnosis dari teks seperti di `11-debugging`, tapi benar-benar
membuka kode, mengubahnya, dan MEMBUKTIKAN perbaikannya lewat browser.

# Penjelasan

6 folder di sini masing-masing adalah SALINAN app latihan (arsitektur
sama seperti project referensi: Route → Service → Repository →
Database), dengan SATU bug realistis disisipkan. Setiap subfolder bisa
dijalankan sendiri (`python app.py`) dan berdiri independen dari
subfolder lainnya.

| Folder | Bug | Gejala |
|---|---|---|
| [bug-01-route-salah](bug-01-route-salah) | `action` form tidak cocok dengan route | Submit Add Expense → 404 |
| [bug-02-template-tidak-ditemukan](bug-02-template-tidak-ditemukan) | Nama file di `render_template()` salah | Buka `/` → 500, `TemplateNotFound` |
| [bug-03-sql-typo](bug-03-sql-typo) | Nama kolom salah ketik di query `UPDATE` | Submit Edit → 500, `OperationalError` |
| [bug-04-import-error](bug-04-import-error) | Import nama function yang tidak ada | `python app.py` gagal START sama sekali |
| [bug-05-variable-none](bug-05-variable-none) | Akses field tanpa cek `None` dulu | Edit id yang tidak ada → 500, `TypeError` |
| [bug-06-request-kosong](bug-06-request-kosong) | Atribut `name` HTML tidak cocok dengan Python | Submit Add → selalu ditolak "Title wajib diisi" |

# Diagram

```
Alur kerja tiap bug:

1. python app.py        → server jalan (atau gagal start — itu sendiri petunjuk)
2. Coba fiturnya          → amati gejala persis (pesan error / perilaku aneh)
3. Baca README bug ini    → cocokkan dengan tabel "Gejala → Lapisan" di 11-debugging
4. Buka file yang dicurigai, cari penyebabnya
5. Perbaiki SATU baris    → jalankan ulang → buktikan gejala hilang
```

# Langkah Pengerjaan

1. Masuk ke SATU folder bug (mulai dari `bug-01`, urut lebih mudah).
2. Jalankan `python app.py`, coba fiturnya, amati gejala.
3. Baca README di folder bug itu untuk instruksi spesifik.
4. Perbaiki, buktikan lewat browser, lalu lanjut ke bug berikutnya.

# File Yang Diubah

Bervariasi per bug — lihat README masing-masing folder.

# Checklist

- [ ] Keenam bug sudah diperbaiki, masing-masing dibuktikan lewat
      browser (bukan cuma "kelihatannya benar" dari membaca kode).
- [ ] Untuk tiap bug, bisa menjelaskan lapisan mana penyebabnya, dan
      kenapa gejalanya muncul di TEMPAT yang terlihat (kadang gejala
      muncul jauh dari lokasi bug sebenarnya).

# Hint

- Jalankan HANYA SATU app.py dalam satu waktu — kalau server lama
  masih jalan di port 5000, server baru akan gagal start dengan pesan
  "Address already in use". Matikan dulu (`Ctrl+C`) sebelum pindah
  folder.
- Perbaiki HANYA satu baris yang benar-benar jadi akar masalah. Kalau
  kamu merasa perlu mengubah banyak file sekaligus untuk satu bug,
  kemungkinan kamu sedang memperbaiki gejala, bukan penyebabnya.
- Bug-04 (import error) TIDAK bisa dites lewat browser sama sekali —
  server-nya bahkan tidak akan menyala. Baca pesan error di TERMINAL,
  bukan di browser.

# Hasil yang Diharapkan

6 aplikasi kecil yang tadinya rusak, sekarang berjalan normal — dan
kamu tahu PERSIS baris mana yang kamu ubah untuk masing-masing.

# Refleksi

1. Bug mana yang paling cepat kamu temukan? Bug mana yang paling
   lama? Apa yang membedakan keduanya?
2. Dari 6 bug ini, mana yang KEMUNGKINAN BESAR akan lolos code review
   manual (dibaca sekilas oleh manusia), dan mana yang HARUS ketahuan
   begitu dicoba sekali di browser?
