# 05 · SQLite Basic

# Tujuan

Berkenalan dengan SQLite secara langsung — koneksi, `CREATE TABLE`,
`INSERT`, `SELECT` — sebelum menggabungkannya dengan Flask.

# Yang Dipelajari

- `sqlite3.connect('nama.db')` — membuka (atau membuat) file database.
- `row_factory = sqlite3.Row` — supaya hasil query bisa dibaca lewat
  nama kolom (`r['nama']`), bukan cuma index angka.
- `CREATE TABLE IF NOT EXISTS` — membuat tabel, aman dijalankan
  berkali-kali.
- `INSERT ... VALUES (?, ?)` — placeholder `?` untuk mencegah SQL
  injection (bukan digabung pakai f-string).
- `db.commit()` — mengunci perubahan supaya permanen.
- `db.execute(...).fetchall()` — mengambil semua hasil `SELECT`.

# Penjelasan Konsep

Database itu berdiri sendiri — ia bukan bagian dari Flask. Flask
hanya salah satu cara "menitipkan" perintah SQL ke database lewat
Python. Modul ini sengaja memisahkan keduanya dulu: kamu belajar
"berbicara" ke SQLite langsung lewat terminal, supaya nanti saat
sqlite3 muncul DI DALAM route Flask (mulai `06-create-table`), kamu
sudah kenal semua bagiannya.

# Langkah Pengerjaan

1. Buka `latihan_sqlite.py`, baca komentarnya dari atas ke bawah.
2. Selesaikan `TODO 1` sampai `TODO 4` berurutan.
3. Jalankan: `python latihan_sqlite.py`.
4. Jalankan SEKALI LAGI, perhatikan apa yang berubah dan apa yang
   tidak (baca bagian "COBA INI SETELAH SELESAI" di file).

# File Yang Diubah

- `latihan_sqlite.py`

# Checklist

- [ ] Tabel `transactions` berhasil dibuat (tidak error saat
      dijalankan berkali-kali).
- [ ] Minimal 2 baris data berhasil di-`INSERT`.
- [ ] `db.commit()` dipanggil setelah `INSERT`.
- [ ] Semua baris berhasil ditampilkan ke terminal lewat `SELECT`.
- [ ] File `latihan.db` muncul di folder ini setelah dijalankan.

# Hint

- Query panjang boleh ditulis pakai tiga tanda kutip (`"""..."""`)
  supaya bisa dibagi ke beberapa baris — lebih mudah dibaca.
- Kalau lupa `db.commit()`, data terlihat "ada" selama program masih
  berjalan, tapi TIDAK benar-benar tersimpan ke file — jalankan
  ulang programnya dan datanya seolah hilang (padahal memang belum
  pernah tersimpan).
- `fetchall()` selalu mengembalikan LIST — walau hasilnya cuma satu
  baris atau kosong sama sekali.

# Hasil Akhir

Script Python murni yang bisa membuat tabel, mengisi, dan membaca
data dari SQLite — tanpa Flask, tanpa browser. Modal ini langsung
dipakai lagi mulai `06-create-table`, kali ini dipicu lewat route.

# Kesalahan Yang Sering Terjadi

- **Lupa `db.commit()`** → data tidak benar-benar tersimpan ke disk.
- **Query SQL pakai f-string** (`f"INSERT ... VALUES ('{nama}')"`)
  alih-alih `?` → rawan SQL injection & sering bikin bug aneh kalau
  datanya mengandung tanda kutip.
- **Lupa `IF NOT EXISTS`** pada `CREATE TABLE` → error
  `table transactions already exists` saat script dijalankan dua kali.
- **Salah jumlah `?` dengan jumlah nilai** di tuple `(...)` →
  `sqlite3.ProgrammingError: Incorrect number of bindings supplied`.
