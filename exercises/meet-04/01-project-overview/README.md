# 01 · Project Overview

# Tujuan Belajar

Membuka `projects/expense-tracker/final/` untuk PERTAMA kalinya tanpa
panik — dapat gambaran besar sebelum membaca satu baris kode pun.

# Penjelasan

`projects/expense-tracker/` (di root repository, BUKAN di dalam
`exercises/`) punya dua folder: `starter/` (kerangka kosong untuk
tantangan bangun-sendiri, bukan urusan `meet-04`) dan `final/` (versi
lengkap yang jadi bahan bacaan kita). Sepanjang `meet-04`, "project
nyata" yang dimaksud selalu merujuk ke `projects/expense-tracker/final/`.

`final/` adalah aplikasi CRUD pencatat pengeluaran yang sama
konsepnya dengan yang kamu bangun sendiri di `meet-03` — tapi ditulis
dengan gaya "rasa industri" dan sengaja dipisah jadi banyak file, bukan
satu `app.py` raksasa.

Isinya, secara garis besar:

```
projects/expense-tracker/final/
├── app.py              ← titik masuk, route
├── config.py            ← baca pengaturan dari .env
├── database/             ← koneksi & skema SQLite
├── models/               ← bentuk data (Expense, daftar kategori)
├── services/             ← validasi & aturan bisnis
├── repositories/         ← SATU-SATUNYA tempat query SQL
├── templates/             ← HTML (Jinja2)
├── static/                ← CSS & JavaScript
├── utils/                 ← logger
├── logs/                  ← catatan kejadian (dibuat otomatis)
├── requirements.txt
├── .env.example
└── README.md              ← dokumentasi resmi project ini
```

Kenapa dipisah sebanyak ini? Karena aplikasi nyata dirawat oleh banyak
orang, dalam waktu lama, oleh tim yang berubah-ubah. Satu file raksasa
gampang ditulis sendirian, tapi susah dirawat bersama. Memecah kode per
tanggung jawab (Route hanya urus HTTP, Service hanya urus aturan,
Repository hanya urus SQL) membuat satu perubahan hanya menyentuh satu
tempat — itu tema besar yang akan kamu buktikan sendiri di folder-folder
berikutnya.

# Diagram

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Browser    │────▶│  app.py      │────▶│  services/   │
│ (user klik)  │     │  (Route)     │     │ (aturan)     │
└──────────────┘     └──────────────┘     └──────┬───────┘
       ▲                                          │
       │                                          ▼
       │              ┌──────────────┐     ┌──────────────┐
       └──────────────│ templates/   │◀────│repositories/ │
                       │ (HTML)      │     │ (SQL)        │
                       └──────────────┘     └──────┬───────┘
                                                    ▼
                                             ┌──────────────┐
                                             │  database/   │
                                             │  (SQLite)    │
                                             └──────────────┘
```

Setiap kotak = satu folder = satu tanggung jawab. Panah menunjukkan
SIAPA MEMANGGIL SIAPA — perhatikan `templates/` tidak pernah memanggil
`database/` langsung, dan `database/` tidak pernah tahu soal `Browser`.

# Langkah Pengerjaan

1. Buka folder `projects/expense-tracker/final/` di VS Code (folder
   terpisah dari `exercises/`, ada di root repository).
2. JANGAN buka `app.py` dulu. Lihat dulu daftar foldernya saja
   (panel Explorer), dan coba tebak isi tiap folder hanya dari
   namanya — tulis tebakanmu di kertas/kepala.
3. Buka `projects/expense-tracker/final/README.md` — baca bagian "Tech
   Stack" dan "Project Structure"-nya saja (jangan baca semuanya
   dulu, itu dokumen panjang, cukup dua bagian itu).
4. (Opsional tapi disarankan) Jalankan project ini sungguhan supaya
   kamu punya aplikasi hidup untuk diklik-klik sambil membaca kode di
   folder-folder berikutnya:
   ```
   cd projects/expense-tracker/final
   pip install -r requirements.txt
   python app.py
   ```
   Lalu buka `http://localhost:5000` di browser. `python app.py` akan
   otomatis membuat `database/expense_tracker.db` dan folder `logs/`
   kalau belum ada — kamu tidak perlu menyiapkan apa pun secara manual.
5. Bandingkan tebakanmu di Langkah 2 dengan isi README yang barusan
   kamu baca. Sejauh mana tebakanmu benar?

# File Yang Diubah

Tidak ada — folder ini murni membaca. `projects/expense-tracker/final/`
tidak diubah sama sekali.

# Checklist

- [ ] Bisa menyebutkan minimal 6 folder/file utama di
      `projects/expense-tracker/final/` dari ingatan (tanpa membuka lagi).
- [ ] Tahu bahwa `app.py` adalah titik masuk, dan `repositories/`
      adalah satu-satunya tempat SQL ditulis.
- [ ] (Kalau menjalankan project) Berhasil membuka
      `http://localhost:5000` dan melihat halaman dashboard.

# Hint

- Nama folder di project Flask HAMPIR SELALU mengikuti konvensi yang
  sama antar project — sekali kamu hafal pola `models/` `services/`
  `repositories/` di sini, kamu akan langsung mengenalinya di project
  Flask siapa pun lainnya.
- Kalau `pip install -r requirements.txt` gagal karena `pip` tidak
  ditemukan, pastikan kamu memakai perintah yang sama seperti waktu
  instalasi Flask di `meet-03` (`pip` atau `pip3`, tergantung OS-mu).
- Project ini butuh Python 3.10+ (karena memakai sintaks tipe data
  modern seperti `list[str]`). Kalau errornya berkaitan dengan syntax
  aneh di `models/expense_model.py`, itu tandanya versi Python-mu
  terlalu lama.

# Hasil yang Diharapkan

Kamu punya peta kasar di kepala: "project ini punya app.py sebagai
pintu masuk, dan lapisan-lapisan lain di baliknya" — tanpa perlu paham
detail satu pun function-nya dulu.

# Refleksi

1. Dari namanya saja, folder mana yang menurutmu paling PENTING untuk
   dibaca duluan kalau kamu ingin tahu "aplikasi ini punya fitur apa
   saja"?
2. Apa bedanya perasaanmu membuka project ini dibanding waktu pertama
   kali membuka `meet-03/06-create-table` dulu? Lebih menakutkan atau
   sudah lebih familiar?
