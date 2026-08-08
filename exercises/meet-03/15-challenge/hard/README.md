# Challenge Hard · Ringkasan Harian + Total Pengeluaran

# Tujuan

Menghitung total & ringkasan lewat SQL — bukan lewat Python (`for`
loop + penjumlahan manual). Level tersulit karena memakai fungsi SQL
(`SUM`, `GROUP BY`) yang di modul hanya disebut sebagai "petunjuk",
belum diajarkan detail sintaksnya.

# Yang Dipelajari

- `SUM(nominal)` — fungsi agregasi SQL, menjumlahkan satu kolom dari
  banyak baris jadi satu angka.
- `GROUP BY tanggal` — mengelompokkan baris-baris dengan tanggal
  yang sama, lalu `SUM()` dihitung PER KELOMPOK, bukan seluruh tabel.
- Kenapa hasil `SUM()` bisa `None` (kalau tabel kosong), dan cara
  amannya menangani itu.

# Penjelasan Konsep

Modul cuma memberi petunjuk singkat: *"Jumlahkan semua nominal di
bawah daftar. Petunjuk: SQL punya `SUM()`."* dan *"Kelompokkan total
per tanggal. Kamu akan kaget betapa mudahnya dengan SQL."* — di
challenge ini kamu membuktikan sendiri betapa mudahnya, dibanding
kalau harus menjumlahkan manual pakai `for` loop di Python.
`GROUP BY` adalah kuncinya: ia membagi baris-baris jadi kelompok
(berdasarkan `tanggal` yang sama), lalu `SUM()` dihitung UNTUK
TIAP KELOMPOK secara terpisah.

# Langkah Pengerjaan

1. Selesaikan `TODO 1` di `app.py` — buat route `/ringkasan`.
2. Jalankan `python app.py`, tambah beberapa transaksi di tanggal
   yang BERBEDA-BEDA (dan ada yang SAMA), termasuk kategori berbeda.
3. Buka `/ringkasan` (atau klik tautan "Lihat Ringkasan" di halaman
   utama).
4. Cek manual: apakah total keseluruhan benar? Apakah total per
   tanggal benar?

# File Yang Diubah

- `app.py`

# Checklist

- [ ] Route `/ringkasan` menampilkan total keseluruhan yang benar.
- [ ] Ringkasan per tanggal menampilkan SATU baris untuk tiap
      tanggal berbeda (bukan satu baris per transaksi).
- [ ] Kalau ada 2 transaksi di tanggal yang sama, totalnya
      TERGABUNG jadi satu angka untuk tanggal itu.
- [ ] Halaman `/ringkasan` tidak error walau tabel masih kosong
      (total tampil sebagai 0, bukan crash).

# Hint

- `SUM(nominal) AS total` — kata `AS` memberi NAMA pada hasil
  perhitungan, supaya bisa diambil lewat `row['total']` (tanpa `AS`,
  namanya jadi rumit dan sulit ditebak).
- Kalau tabel kosong, `SELECT SUM(nominal) FROM transactions` tetap
  mengembalikan SATU baris — tapi nilainya `None`, bukan `0`. Pola
  `total_row['total'] or 0` menyulap `None` jadi `0` dengan aman.
- `GROUP BY` HARUS dipasangkan dengan kolom yang sama di `SELECT`
  (di sini: `tanggal`) — kalau tidak, SQLite bisa memberi hasil yang
  membingungkan.

# Hasil Akhir

Halaman ringkasan yang menghitung total & breakdown per tanggal
secara instan lewat SQL — fitur yang di aplikasi keuangan sungguhan
(lihat lagi `get_category_totals()` di `projects/expense-tracker/final`)
dipakai dengan pola SQL yang sama persis.
