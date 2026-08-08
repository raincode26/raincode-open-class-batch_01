# Solusi · Challenge Hard

# Tujuan

Referensi pembanding untuk `15-challenge/hard`.

# Yang Dipelajari

Cara memakai `SUM()` untuk total tunggal (`fetchone()`) dan `SUM()` +
`GROUP BY` untuk total per kelompok (`fetchall()`) dalam satu route
yang sama.

# File Yang Diubah

Tidak ada — folder ini untuk dibaca, bukan diedit.

# Langkah Pengerjaan

1. `SELECT SUM(nominal) AS total FROM transactions` selalu
   menghasilkan SATU baris (bahkan kalau tabel kosong — nilainya
   `None`), makanya dipakai `.fetchone()`.
2. `total_row['total'] or 0` — trik umum Python: kalau nilai di kiri
   `or` adalah `None`/`0`/`""` (dianggap "falsy"), Python memakai
   nilai di kanan `or` sebagai gantinya.
3. Query kedua mengelompokkan baris per `tanggal` lewat `GROUP BY`,
   menghasilkan BANYAK baris (satu per tanggal unik), makanya dipakai
   `.fetchall()`.

# Hint

Bandingkan dua query di route ini: yang pertama TIDAK punya
`GROUP BY` (hasilnya satu angka untuk SELURUH tabel), yang kedua
PUNYA `GROUP BY tanggal` (hasilnya satu angka PER tanggal). Ini
perbedaan paling penting untuk dipahami dari `SUM()`.

# Checklist

- [ ] Sudah membandingkan dengan hasil kerjaku sendiri di `15-challenge/hard`.

# Hasil Akhir

Halaman ringkasan yang menghitung total & breakdown harian langsung
lewat SQL, tanpa satu baris `for` loop penjumlahan manual di Python.
