# Pertemuan 4 — Membaca Aplikasi Nyata

Tidak ada syntax baru minggu ini. Tiga pertemuan lalu kamu **membangun**
Expense Tracker sendiri (`meet-03`) — folder demi folder, dari 6 baris
`app.py` sampai CRUD lengkap. Minggu ini kamu berlatih skill yang jauh
lebih sering dipakai seorang Software Engineer sehari-hari: **membaca
kode orang lain**, memahami alurnya, menemukan bug-nya, dan mengubahnya
sedikit tanpa merusaknya.

Bahan bacaannya: `projects/expense-tracker/final/` — Expense Tracker yang
SAMA seperti punyamu, tapi ditulis dengan gaya "rasa industri" (Route →
Service → Repository, terpisah ke banyak file). Kamu tidak akan
mengubah project itu. Kamu akan membacanya, lalu berlatih di project
kecil terpisah yang meniru arsitektur yang sama.

## Kenapa Ini Penting

> "Engineer menghabiskan lebih banyak waktu membaca kode daripada
> menulisnya." — Modul Pertemuan 4

Kalau kamu bisa membuka repository GitHub siapa pun dan dalam 10 menit
menjawab "aplikasi ini bekerja bagaimana?" — itu skill yang lebih
langka (dan lebih berharga) daripada hafal syntax.

## Urutan Belajar

| # | Folder | Fokus | Sifat |
|---|---|---|---|
| 1 | [01-project-overview](01-project-overview) | Apa itu `projects/expense-tracker/final`, folder apa saja, kenapa dipisah | Baca |
| 2 | [02-folder-structure](02-folder-structure) | Fungsi tiap folder: `templates/`, `static/`, `database/`, dst | Baca |
| 3 | [03-request-flow](03-request-flow) | Alur satu request: Browser → Route → ... → Browser | Baca |
| 4 | [04-html-analysis](04-html-analysis) | Membaca `templates/*.html` — form, table, layout | Baca |
| 5 | [05-css-analysis](05-css-analysis) | Membaca `static/css/style.css` — kenapa class-nya begitu | Baca |
| 6 | [06-python-analysis](06-python-analysis) | Membaca `app.py` baris per baris | Baca |
| 7 | [07-route-analysis](07-route-analysis) | Apa yang terjadi di tiap route: `/`, Add, Edit, Delete | Baca |
| 8 | [08-database-analysis](08-database-analysis) | Skema SQLite, kolom, primary key, semua query | Baca |
| 9 | [09-crud-analysis](09-crud-analysis) | Flow CRUD lengkap sebagai satu diagram | Baca |
| 10 | [10-read-real-feature](10-read-real-feature) | Lacak SATU fitur nyata ujung ke ujung, tanpa menulis kode | Baca |
| 11 | [11-debugging](11-debugging) | Diagnosis 9 skenario error dari gejala & log saja | Diagnosis |
| 12 | [12-buggy](12-buggy) | Perbaiki 6 bug realistis di project latihan yang bisa dijalankan | Perbaiki |
| 13 | [13-refactor](13-refactor) | Rapikan kode berbau (function panjang, magic number/string) | Refactor |
| 14 | [14-mini-feature](14-mini-feature) | Tambah fitur kecil TANPA materi baru | Tambah |
| 15 | [15-challenge](15-challenge) | Easy → Medium → Hard | Uji diri |
| 16 | [16-solution](16-solution) | Kunci jawaban seluruh challenge | Pembanding |

## Dua Project, Dua Peran

- **`projects/expense-tracker/final/`** — project NYATA, dibaca tapi
  **tidak pernah diedit** oleh folder mana pun di `meet-04/`. Ini
  "kode orang lain" yang kamu pelajari cara membacanya (folder 01–11).
- **Project latihan di `12`–`16`** — arsitektur yang SAMA (Route →
  Service → Repository, tabel `expenses`, kolom `title`/`amount`/
  `category`), tapi ukurannya kecil supaya bisa kamu jalankan, rusak,
  dan perbaiki sendiri tanpa risiko merusak project referensi.

## Cara Menjalankan

Folder `01`–`11` murni membaca — tidak ada `app.py` untuk dijalankan
di dalamnya (kecuali kamu ingin menjalankan `projects/expense-tracker/final/`
sendiri, lihat caranya di [01-project-overview](01-project-overview)).

Folder `12`–`16` masing-masing adalah aplikasi Flask mandiri:

1. **Sekali saja** di awal — pasang Flask (kalau belum):
   ```
   pip install flask
   ```
2. Masuk ke folder latihan yang ingin dikerjakan.
3. Jalankan:
   ```
   python app.py
   ```
4. Buka `http://localhost:5000` di browser.
5. Berhenti server dengan `Ctrl+C`.

File database (`expenses.db`) dibuat otomatis saat aplikasi pertama
kali jalan.

## Prinsip Belajar

- **Baca dulu, tulis nanti.** Folder 01–11 sama sekali tidak minta
  kamu menulis kode. Itu disengaja — membaca butuh latihan tersendiri,
  terpisah dari menulis.
- **Jangan baca dari atas ke bawah.** Mulai dari `app.py`, ikuti SATU
  alur (misalnya "Add") sampai tuntas, baru lompat ke file lain yang
  dipanggil. Baca berdasarkan fitur, bukan berdasarkan urutan folder.
- **Error = alamat, bukan hukuman.** `11-debugging` melatihmu membaca
  gejala (pesan error, isi log) untuk menebak lapisan mana yang
  bermasalah — SEBELUM menyentuh kode sama sekali.
- **`12-buggy` sebelum `13`–`16`.** Kebiasaan memperbaiki kode orang
  lain adalah bekal sebelum merefactor atau menambah fitur.
- **Project latihan ≠ project referensi.** Kalau bingung "harusnya
  bagaimana", `projects/expense-tracker/final/` selalu jadi rujukan pola —
  tapi jangan disalin baris per baris, ukurannya sengaja beda.

## Checklist Akhir Kelas

- [ ] Bisa menjelaskan fungsi tiap folder di `projects/expense-tracker/final/`
      hanya dari namanya.
- [ ] Bisa menggambar alur satu request: Browser → Route → Service →
      Repository → Database → balik lagi ke Browser.
- [ ] Bisa menunjuk di baris mana SQL sungguhan ditulis, dan
      menjelaskan kenapa hanya di satu tempat itu.
- [ ] Bisa menebak lapisan mana yang bermasalah hanya dari gejala
      error atau isi log — sebelum membuka kode.
- [ ] Bisa membuka project Flask siapa pun dan dalam 10 menit
      menjelaskan: apa fungsinya, dan di mana "otak"-nya.

RainCode Open Class · Understand before memorizing.
