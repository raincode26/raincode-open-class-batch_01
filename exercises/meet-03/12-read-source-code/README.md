# 12 · Read Source Code

# Tujuan

Membaca project Flask + SQLite **nyata** (`projects/expense-tracker/final/`)
tanpa panik — membuktikan bahwa aplikasi yang tadinya terlihat rumit
sebenarnya cuma kumpulan konsep yang barusan kamu kuasai sendiri.

# Yang Dipelajari

- Jurus 3 langkah membaca kode asing: (1) cari semua `@app.route`,
  (2) untuk tiap route tanya "ini CRUD yang mana?", (3) baru telusuri
  detailnya.
- Alur satu request menembus lapisan: `Browser → Route → Service →
  Repository → Database`, lalu balik lagi secara terbalik.
- Kenapa project nyata MEMISAH kode ke banyak file, sementara
  punyamu masih satu `app.py`.

# Penjelasan Konsep

Tidak ada kode baru yang ditulis di folder ini — **folder ini murni
tentang membaca**. Programmer, faktanya, jauh lebih sering membaca
kode daripada menulisnya. `projects/expense-tracker/final/` adalah Expense
Tracker yang SAMA seperti yang barusan kamu bangun — CRUD yang sama,
SQLite yang sama — tapi ditulis dengan gaya "rasa industri":

| Yang kamu bangun (`06`-`11`) | Project nyata (`projects/expense-tracker/final`) |
|---|---|
| Satu file `app.py` | Dipisah: `app.py`, `services/`, `repositories/`, `models/` |
| Tabel `transactions` | Tabel `expenses` |
| Kolom `nama`, `nominal`, `kategori`, `tanggal` | Kolom `title`, `amount`, `category`, `notes`, `created_at` |
| `db.execute(...)` langsung di route | Route memanggil Service, Service memanggil Repository |

Nama & struktur file beda, **tapi alur CRUD-nya sama persis**. Kalau
kamu paham punyamu, kamu sudah 80% paham project ini juga.

# Langkah Pengerjaan

Buka folder `projects/expense-tracker/final/` di editor (folder
terpisah dari `exercises/meet-03/`, ada di root repository). Ikuti
urutan ini — JANGAN loncat ke Langkah 4 sebelum Langkah 1-3 selesai.

### Langkah 1 — Peta folder

Buka `projects/expense-tracker/final/` dan lihat isinya. Sebelum membaca
satu baris kode pun, tebak dulu isi tiap folder hanya dari namanya:

- `app.py` — ?
- `models/` — ?
- `services/` — ?
- `repositories/` — ?
- `database/` — ?
- `templates/` — ?
- `static/` — ?
- `utils/` — ?

Cocokkan tebakanmu: `app.py` = titik masuk (menerima request,
memanggil service, mengirim HTML kembali). `services/` = logika &
aturan (validasi). `repositories/` = satu-satunya tempat query SQL
ditulis. `models/` = bentuk data. `templates/` + `static/` =
tampilan. `database/` = koneksi & skema. `utils/` = alat bantu
(logger).

### Langkah 2 — Cari semua `@app.route`

Buka `app.py`. Cari SEMUA baris `@app.route(...)`. Itu daftar
"halaman" aplikasi ini — peta fitur, sebelum kamu paham detailnya.
Untuk tiap route, tanya: **"ini CRUD yang mana?"** — lihat kata
kuncinya: menampilkan (Read), form `POST` (Create), edit (Update),
hapus (Delete).

Isi tabel ini (boleh di kepala, boleh di kertas):

| Route | Method | CRUD apa? |
|---|---|---|
| `/` | ? | ? |
| `/expenses` | ? | ? |
| `/create` | ? | ? |
| `/edit/<int:expense_id>` | ? | ? |
| `/delete/<int:expense_id>` | ? | ? |

### Langkah 3 — Ikuti SATU aksi menembus 3 lapisan

Bayangkan kamu menambah pengeluaran "Kopi pagi, Rp 25.000" lewat
halaman `/create`. Ikuti perjalanan datanya:

1. Buka `templates/create.html` — cari `<form action="..."
   method="...">`. Ke mana data ini dikirim?
2. Buka `app.py`, cari function `create()`. Baca: apakah ia menulis
   SQL sendiri? Atau memanggil sesuatu yang lain?
3. Buka `services/expense_service.py`, cari `create_expense()`.
   Baca `_validate_and_clean()` — aturan apa saja yang dicek sebelum
   data boleh disimpan? (contoh: amount harus lebih besar dari apa?)
4. Buka `repositories/expense_repository.py`, cari `create_expense()`
   di sana. Ini satu-satunya tempat query `INSERT INTO expenses...`
   benar-benar ditulis.

Perjalanan lengkapnya: **user ketik → HTML kumpulkan → POST ke
`/create` → Route ambil data → Service memeriksa → Repository
INSERT → SQLite simpan → redirect → user lihat hasilnya.**

### Langkah 4 — Bandingkan dengan Delete

Buka route `/delete/<int:expense_id>` di `app.py`, lalu telusuri
lagi ke `services/` dan `repositories/`. Bandingkan dengan
`/hapus/<int:id>` yang kamu tulis sendiri di `10-delete-expense` —
apa yang sama, apa yang beda?

# File Yang Diubah

Tidak ada — folder ini tidak berisi kode untuk diedit. Semua
kegiatan ada di `projects/expense-tracker/final/` (dibaca, tidak diubah).

# Checklist

- [ ] Bisa menyebutkan fungsi tiap folder di `expense-tracker/` hanya
      dari namanya.
- [ ] Sudah menandai SEMUA `@app.route` di `app.py` dan tahu masing-
      masing CRUD apa.
- [ ] Bisa menceritakan alur "Kopi pagi" dari form sampai tersimpan,
      lapisan demi lapisan (Route → Service → Repository → Database).
- [ ] Paham kenapa Route TIDAK menulis SQL sendiri, dan Repository
      TIDAK memutuskan aturan bisnis.

# Hint

- Jangan coba paham SEMUA file sekaligus. Ikuti SATU alur (misalnya
  Create) sampai tuntas dulu, baru lanjut ke alur lain.
- `Ctrl+Klik` (atau `Cmd+Klik` di Mac) pada nama function di VS Code
  akan langsung membawamu ke definisinya — cara cepat "melompat" dari
  Route ke Service ke Repository.
- Kalau bingung istilah "layer/lapisan": anggap seperti pembagian
  tugas restoran (Bagian 3 modul) — Route = pelayan (terima pesanan),
  Service = koki kepala (putuskan boleh/tidak, sesuai resep), 
  Repository = orang gudang (satu-satunya yang buka & tutup lemari
  bahan/database).

# Hasil Akhir

Kepercayaan diri untuk membuka project Flask siapa pun tanpa panik —
kamu tahu HARUS mulai dari mana (`app.py`), dan tahu pertanyaan apa
yang harus ditanyakan di tiap file yang kamu buka.

# Kesalahan Yang Sering Terjadi

- **Mencoba membaca semua file dari atas ke bawah secara berurutan**
  (models dulu, lalu database, lalu...) → melelahkan & membingungkan.
  Selalu mulai dari `app.py`, ikuti SATU alur, baru lompat ke file
  lain yang dipanggil.
- **Menganggap "banyak folder = lebih rumit"** → sebenarnya
  sebaliknya: memisah tugas per folder membuat tiap file JADI LEBIH
  PENDEK dan lebih mudah dicari saat ada masalah.
- **Berhenti di Route saja**, tidak menelusuri sampai ke Repository →
  melewatkan bagian paling penting: di situlah SQL sungguhan
  dijalankan.
