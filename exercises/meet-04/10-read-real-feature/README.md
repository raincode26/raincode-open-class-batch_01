# 10 · Read Real Feature

# Tujuan Belajar

Melacak SATU fitur nyata ujung ke ujung SENDIRIAN — tanpa diagram
jawaban disediakan di depan seperti di `09-crud-analysis`. Ini "ujian
praktik" dari semua skill membaca yang sudah dilatih di folder 01–09.

# Penjelasan

Di `09-crud-analysis`, kamu melacak flow CREATE dengan diagram yang
SUDAH disediakan — tugasmu cuma mencocokkan. Kali ini terbalik: kamu
pilih SATU fitur di bawah, lalu BUAT SENDIRI diagramnya dari nol,
persis seperti seorang engineer yang baru gabung ke sebuah tim dan
diminta "pahami dulu fitur X sebelum mulai kerja."

Pilih SATU (tidak perlu keduanya):

- **Fitur Search & Filter** — `GET /expenses?search=kopi&category=Food`
- **Fitur Category Summary** — `GET /summary` (total per kategori)

Kedua fitur ini SENGAJA belum pernah dibahas detail di folder
sebelumnya (folder 03–09 fokus ke Create/Read-tunggal/Update/Delete).
Kamu akan menemukan sendiri bagaimana fitur BARU tetap mengikuti pola
Route → Service → Repository yang sama.

# Diagram

```
Isi sendiri — kosongkan dulu, ini yang akan kamu lengkapi:

┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Browser     │────▶│  Route      │────▶│  Service    │────▶│ Repository  │
│  ?           │     │  (fungsi?)  │     │  (fungsi?)  │     │  (fungsi?)  │
└─────────────┘     └─────────────┘     └─────────────┘     └──────┬──────┘
                                                                     │
                                                                     ▼
                                                              ┌─────────────┐
                                                              │  Query SQL? │
                                                              └─────────────┘
```

# Langkah Pengerjaan

1. Pilih SATU fitur (Search & Filter, atau Category Summary).
2. Kalau project sedang berjalan (dari `01-project-overview`), coba
   fiturnya langsung di browser dulu. Untuk Search & Filter: buka
   `/expenses`, ketik sesuatu di kotak search, lihat perubahan di
   URL. Untuk Summary: buka `/summary`, lihat angka-angkanya.
3. Buka `app.py`. Cari route yang menangani fitur pilihanmu
   (`expenses()` untuk Search & Filter, `summary()` untuk Summary).
   Baca — parameter apa yang diambil dari `request.args`?
4. Ikuti pemanggilan function dari route itu turun ke `services/`,
   lalu ke `repositories/`. Catat NAMA function di tiap lapisan
   (jangan hafal — tulis).
5. Di `repositories/`, cari query SQL yang PERSIS menjalankan logic
   fitur ini. Untuk Search & Filter: cari `LIKE` dan `WHERE`. Untuk
   Summary: cari `GROUP BY` dan `SUM(...)`.
6. Gambar ulang diagram di atas dengan hasil temuanmu — isi setiap
   kotak dengan nama function/query ASLI, bukan generik lagi.
7. Tulis dalam 3-5 kalimat: "Fitur [nama fitur] bekerja dengan cara
   ..." — seolah menjelaskan ke teman satu tim yang belum pernah baca
   project ini.

# File Yang Diubah

Tidak ada — folder ini murni membaca (dan mengklik-klik).

# Checklist

- [ ] Diagram versimu sendiri (Langkah 6) sudah terisi lengkap dengan
      nama function & query SQL asli.
- [ ] Ringkasan 3-5 kalimat (Langkah 7) sudah ditulis, TANPA melihat
      kode lagi saat menulisnya (tes: bisa kamu jelaskan dari ingatan?).
- [ ] Kalau memilih Search & Filter: paham kenapa `category` dan
      `search` BOLEH kosong sekaligus (tanpa error) — cek bagaimana
      `services/`/`repositories/` menangani kondisi "tidak ada filter
      sama sekali".
- [ ] Kalau memilih Summary: paham dari mana angka "percentage" per
      kategori dihitung, dan bagaimana pembagian oleh nol (kalau
      belum ada data sama sekali) tidak menyebabkan crash.

# Hint

- Jangan mulai dari `repositories/`. SELALU mulai dari `app.py` (titik
  masuk request), baru turun ke bawah — sama seperti jurus 3 langkah
  yang sudah kamu pakai di `meet-03/12-read-source-code`.
- Kalau kamu memilih Summary dan bingung soal pembagian oleh nol, cari
  kata `if count > 0 else` atau `if grand_total > 0 else` di
  `services/expense_service.py` — itu pola umum menghindari error
  "ZeroDivisionError".
- Boleh sekali mengintip folder `03-request-flow` atau
  `09-crud-analysis` kalau benar-benar buntu — tapi coba dulu tanpa
  membuka keduanya. Ujian sesungguhnya baru berarti kalau dicoba
  sendiri dulu.

# Hasil yang Diharapkan

Sebuah diagram & ringkasan tertulis, hasil kerjamu sendiri, yang bisa
kamu tunjukkan ke orang lain sebagai bukti: "saya bisa membaca fitur
BARU di project asing tanpa dituntun."

# Refleksi

1. Waktu melacak fitur ini sendirian (dibanding waktu dituntun di
   `09-crud-analysis`), bagian mana yang terasa paling sulit? Kenapa?
2. Kalau besok kamu harus melacak fitur KETIGA yang belum pernah
   dibahas sama sekali di modul ini, langkah pertama apa yang akan
   kamu lakukan?
