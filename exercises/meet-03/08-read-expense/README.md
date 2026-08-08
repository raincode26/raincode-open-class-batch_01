# 08 · Read Expense

# Tujuan

Membaca SATU baris data spesifik lewat `id`-nya — skill wajib
sebelum Update & Delete bisa dibuat.

# Yang Dipelajari

- `SELECT * FROM transactions WHERE id = ?` — mengambil baris
  tertentu, bukan semuanya.
- `.fetchone()` vs `.fetchall()` — `fetchone()` mengembalikan SATU
  baris (atau `None` kalau tidak ketemu), `fetchall()` selalu
  mengembalikan LIST.
- Route dinamis `<int:id>` — `int:` memastikan Flask hanya menerima
  angka di bagian itu (kalau bukan angka, otomatis jadi `404`).

# Penjelasan Konsep

Kamu sudah bisa membaca SEMUA transaksi sejak `06-create-table`
(lihat lagi route `index()` — itu Read juga!). Tapi Update dan
Delete tidak bisa bekerja dengan "semua data" — mereka butuh tahu
PERSIS baris mana yang dimaksud. Di sinilah `WHERE id = ?` dan
`fetchone()` berperan: mengambil satu baris spesifik berdasarkan
id yang diklik user.

# Langkah Pengerjaan

1. Baca ulang route `index()` — perhatikan tautan `<a
   href="/detail/{{ t.id }}">` yang sudah ditambahkan di
   `templates/index.html`.
2. Selesaikan `TODO 1` di `app.py`: buat route `/detail/<int:id>`.
3. Jalankan `python app.py`, tambah beberapa transaksi, klik salah
   satu nama transaksi di daftar.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] Route `/detail/<int:id>` berhasil dibuat.
- [ ] Query memakai `WHERE id = ?` dan `.fetchone()` (bukan
      `.fetchall()`).
- [ ] Mengklik transaksi di daftar menampilkan detail yang BENAR
      (id, nama, nominal yang cocok).
- [ ] Membuka `/detail/999` (id yang tidak ada) menampilkan pesan
      "tidak ditemukan", bukan crash.

# Hint

- `(id,)` — koma di dalam kurung itu WAJIB. Tanpa koma, Python tidak
  membacanya sebagai tuple, dan `sqlite3` akan komplain.
- `int:` di `<int:id>` bukan sekadar hiasan — coba hapus dan buka
  `/detail/abc`, lihat bedanya dibanding kalau memakai `<int:id>`.
- Kalau `item` bernilai `None` (id tak ditemukan) dan template
  langsung menampilkan `item.nama` tanpa dicek dulu, Jinja TIDAK akan
  crash — ia cuma diam-diam menampilkan teks kosong. Masalahnya
  justru itu: halaman jadi terlihat "rusak" (field-fieldnya kosong)
  tanpa penjelasan apa pun. Makanya `templates/detail.html` tetap
  memakai `{% if item %}` — bukan untuk mencegah error, tapi supaya
  pesan "tidak ditemukan" muncul jelas, bukan halaman kosong yang
  membingungkan.

# Hasil Akhir

Kemampuan membaca satu baris spesifik dari database — modal yang
langsung dipakai lagi di `09-update-expense` (mengisi form edit
dengan data yang sudah ada) dan `10-delete-expense` (memastikan baris
yang tepat yang dihapus).

# Kesalahan Yang Sering Terjadi

- **Pakai `.fetchall()` padahal harusnya `.fetchone()`** → `item`
  jadi sebuah LIST berisi satu Row, bukan Row itu sendiri. Jinja
  TIDAK error karenanya, tapi `item.nama` akan tampil KOSONG (list
  tidak punya field bernama itu) — gejalanya membingungkan karena
  tanpa pesan error sama sekali.
- **Lupa koma di `(id,)`**, menulis `(id)` saja → error
  `Incorrect number of bindings supplied` karena `(id)` bukan tuple.
- **Id tidak ditemukan tapi template tidak dicek dulu** → field-field
  di halaman (nama, nominal) tampil kosong secara diam-diam, tanpa
  pesan yang jelas ke pengunjung. (Beda dengan kalau `item['nama']`
  diakses langsung di kode PYTHON, seperti di `14-buggy/bug-06` —
  di situ Python-nya yang benar-benar crash, bukan Jinja-nya.)
- **Lupa `<int:...>` di route**, hanya `<id>` → `id` datang sebagai
  teks ("3" bukan 3), biasanya masih "kebetulan berfungsi" di SQLite
  tapi bukan kebiasaan yang benar.
