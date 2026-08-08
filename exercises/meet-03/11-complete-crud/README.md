# 11 · Complete CRUD

# Tujuan

Merangkum seluruh CRUD jadi satu aplikasi utuh, lalu "Level Up" —
menambah kolom kategori & tanggal — persis seperti Latihan 05 & 06
di modul.

# Yang Dipelajari

- Membaca ulang & merangkai empat operasi CRUD yang sebelumnya
  dipelajari terpisah (`07`-`10`) sebagai satu aplikasi yang koheren.
- Menambah kolom baru ke tabel SEBELUM ada data (cukup ubah
  `CREATE TABLE`) — beda dengan menambah kolom ke tabel yang SUDAH
  berisi data (butuh `ALTER TABLE`, lihat catatan Hint).
- `ORDER BY id DESC` — menampilkan transaksi terbaru di paling atas.

# Penjelasan Konsep

Modul menyebut ini "Level Up": setelah CRUD dasar (nama, nominal)
berjalan, aplikasi nyata hampir selalu berkembang — butuh kolom baru.
Di latihan ini kita tambah dua: `kategori` (biar bisa dikelompokkan)
dan `tanggal` (biar bisa diurutkan berdasarkan waktu). Karena tabel
di folder ini masih akan dibuat dari nol (belum ada data lama), cukup
ubah `CREATE TABLE`-nya langsung. Kalau tabelnya SUDAH berisi data
produksi, barulah `ALTER TABLE ... ADD COLUMN ...` dipakai (lihat
Cheat Sheet Grup 3) — supaya data lama tidak hilang.

# Langkah Pengerjaan

1. Baca ulang seluruh `app.py` — semua route CRUD sudah lengkap dan
   bekerja, ini rangkuman dari `06` sampai `10`.
2. Selesaikan `TODO 1`: tambah kolom `kategori` & `tanggal` ke
   `CREATE TABLE`.
3. Selesaikan `TODO 2`: sertakan `kategori` & `tanggal` di route
   `/tambah`.
4. Selesaikan `TODO 3`: sertakan `kategori` & `tanggal` di route
   `/edit/<int:id>`.
5. Jalankan `python app.py`, tambah transaksi lengkap dengan kategori
   & tanggal, lalu coba edit salah satunya.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] Tabel punya kolom `kategori` dan `tanggal` (cek dengan
      menambah transaksi baru — apakah keduanya tersimpan?).
- [ ] Transaksi baru menyimpan kategori & tanggal yang dipilih user,
      bukan kosong.
- [ ] Mengedit transaksi mengubah kategori & tanggal juga, tidak
      cuma nama & nominal.
- [ ] Semua fitur lama (detail, hapus) masih berfungsi normal.

# Hint

- Kalau lupa menambah kolom di `CREATE TABLE` tapi sudah menjalankan
  aplikasinya sekali, `expense_tracker.db` sudah terlanjur dibuat
  dengan skema lama — `CREATE TABLE IF NOT EXISTS` TIDAK akan
  mengubah tabel yang sudah ada. Hapus file `expense_tracker.db` di
  folder ini, lalu jalankan ulang `python app.py` supaya tabel dibuat
  ulang dengan skema baru.
- Jumlah `?` di query harus sama dengan jumlah kolom yang disebutkan
  — 4 kolom = 4 tanda tanya = 4 nilai di tuple.
- `<select>` di form sudah lengkap dengan 6 pilihan kategori — kamu
  tidak perlu mengubah HTML-nya, cukup pastikan Python-nya menangkap
  nilai yang dipilih.

# Hasil Akhir

Expense Tracker mini yang utuh: Create, Read, Update, Delete, plus
kategori & tanggal di setiap transaksi. Ini fondasi yang sama akan
kamu bandingkan dengan project profesional di `12-read-source-code`.

# Kesalahan Yang Sering Terjadi

- **Menjalankan aplikasi SEBELUM menyelesaikan TODO 1**, lalu baru
  mengubah `CREATE TABLE` → tabel lama (tanpa kategori/tanggal)
  sudah kadung dibuat. `CREATE TABLE IF NOT EXISTS` melihat tabel
  itu "sudah ada" dan tidak membuatnya ulang. Solusi: hapus
  `expense_tracker.db`, jalankan lagi.
- **Lupa menambahkan `kategori`/`tanggal` di salah satu route** (misal
  sudah benar di `/tambah` tapi lupa di `/edit`) → data tersimpan
  saat ditambah, tapi hilang/kosong lagi setelah diedit.
- **Urutan `?` di query tidak sesuai urutan tuple** → nilai kategori
  bisa "nyasar" masuk ke kolom tanggal atau sebaliknya.
