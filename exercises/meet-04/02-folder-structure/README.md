# 02 · Folder Structure

# Tujuan Belajar

Mengenali fungsi PERSIS tiap folder & file penting di
`projects/expense-tracker/final/`, sampai bisa menebak isi file baru hanya
dari lokasinya.

# Penjelasan

Di `01-project-overview` kamu baru menebak-nebak. Sekarang kita buka
tiap folder betulan dan cocokkan. Tabel ini adalah rujukan penuh —
simpan untuk dipakai lagi di folder-folder berikutnya.

| Folder / File | Isinya | Boleh berisi SQL? | Boleh berisi HTML? |
|---|---|---|---|
| `app.py` | Semua `@app.route(...)` — pintu masuk request | Tidak | Tidak |
| `config.py` | Baca `.env`, sediakan satu objek `config` untuk semua file lain | Tidak | Tidak |
| `models/expense_model.py` | Bentuk data `Expense`, daftar `EXPENSE_CATEGORIES` | Tidak | Tidak |
| `services/expense_service.py` | Validasi (`_validate_and_clean`), aturan bisnis, format angka | Tidak | Tidak |
| `repositories/expense_repository.py` | SEMUA query SQL project ini — satu-satunya tempat | **Ya, satu-satunya** | Tidak |
| `database/db.py` | `sqlite3.connect(...)`, `CREATE TABLE` | Ya (skema saja) | Tidak |
| `templates/*.html` | Tampilan (Jinja2) | Tidak | Ya |
| `static/css/style.css` | Warna, jarak, layout | Tidak | Tidak |
| `static/js/app.js` | Modal konfirmasi hapus, live-search, validasi ringan di browser | Tidak | Tidak |
| `utils/logger.py` | Setup logging, dipakai `get_logger(__name__)` di semua file lain | Tidak | Tidak |
| `logs/app.log` | Catatan kejadian aplikasi (dibuat otomatis saat run) | Tidak | Tidak |
| `.env.example` | Contoh isi konfigurasi (disalin manual jadi `.env` kalau perlu) | Tidak | Tidak |

# Diagram

```
Siapa boleh bicara ke siapa (panah = "memanggil"):

app.py ──▶ services/ ──▶ repositories/ ──▶ database/
  │                                              │
  ▼                                              ▼
templates/                                   (SQLite file)

config.py  ◀── dipanggil dari MANA SAJA (app.py, database/, utils/)
utils/logger.py ◀── dipanggil dari MANA SAJA juga
```

`config.py` dan `utils/logger.py` adalah "utility" — semua lapisan
boleh memanggilnya langsung, karena isinya bukan aturan bisnis maupun
data, cuma alat bantu.

# Langkah Pengerjaan

1. Buka `database/db.py` — cari baris yang memanggil
   `sqlite3.connect(...)`. Ini SATU-SATUNYA tempat di seluruh project
   yang melakukan itu. Konfirmasi dengan mencari (Ctrl+Shift+F di VS
   Code) kata `sqlite3.connect` di seluruh folder — harus cuma muncul
   sekali.
2. Buka `repositories/expense_repository.py` — cari semua kata kunci
   SQL (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). Konfirmasi lagi dengan
   pencarian global: kata-kata itu HANYA muncul di file ini (dan
   `database/db.py` untuk `CREATE TABLE`nya saja).
3. Buka `utils/logger.py`, lalu cari (pencarian global) `get_logger(`
   — perhatikan betapa banyak file yang memanggilnya. Itu contoh
   "utility" yang boleh dipakai di mana saja.
4. Buka `.env.example`. Baca isinya — ini daftar semua pengaturan yang
   BISA diubah (nama app, path database, level log) tanpa mengubah
   kode satu baris pun.

# File Yang Diubah

Tidak ada — folder ini murni membaca.

# Checklist

- [ ] Bisa menyebutkan tanpa membuka file lagi: folder mana yang
      boleh menulis SQL, folder mana yang tidak boleh.
- [ ] Sudah membuktikan sendiri (lewat pencarian global) bahwa
      `sqlite3.connect` cuma dipanggil satu kali di seluruh project.
- [ ] Paham bedanya `models/` (bentuk data) vs `services/` (aturan)
      vs `repositories/` (akses data) — tiga hal yang gampang tertukar
      di awal.

# Hint

- Kalau bingung folder mana yang "benar" tempat sesuatu berada,
  tanyakan: "apa YANG dilakukan kode ini?" — kalau jawabannya
  "menerima klik dari browser" → Route. "Menentukan boleh/tidak" →
  Service. "Bicara ke database" → Repository.
- `models/expense_model.py` di project ini sebenarnya TIDAK terlalu
  banyak dipakai — bagian yang benar-benar aktif dipakai cuma daftar
  `EXPENSE_CATEGORIES`-nya. Jangan heran kalau isinya terasa lebih
  "sepi" dibanding folder lain — itu wajar, tidak semua project
  memakai tiap lapisan dengan intensitas yang sama.
- Fitur pencarian global (`Ctrl+Shift+F` di VS Code, atau `Cmd+Shift+F`
  di Mac) adalah alat PALING sering dipakai engineer saat membaca
  project asing — jauh lebih cepat daripada membuka file satu-satu.

# Hasil yang Diharapkan

Kamu bisa menjawab "kalau saya mau tahu SEMUA query SQL yang pernah
dijalankan project ini, saya buka file mana?" dalam hitungan detik,
tanpa ragu.

# Refleksi

1. Kalau besok ada bug "amount tersimpan minus, harusnya ditolak",
   folder mana yang PALING mungkin kamu buka duluan? Kenapa?
2. Apa untungnya `config.py` dan `utils/logger.py` "boleh dipanggil
   dari mana saja", dibanding kalau aturan itu dilanggar bebas untuk
   SEMUA folder (termasuk `repositories/` boleh langsung merender
   HTML)?
