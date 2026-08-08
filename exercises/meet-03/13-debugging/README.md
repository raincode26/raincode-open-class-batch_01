# 13 · Debugging

# Tujuan

Mengenal 6 error paling umum di Flask, cara membaca pesannya, dan
melatih "menebak lapisan mana yang bermasalah" — sebelum masuk ke
`14-buggy` untuk memperbaikinya langsung dengan tangan sendiri.

# Yang Dipelajari

- 6 error umum Flask: route tidak ditemukan (404), database tidak
  ada, tabel tidak ada, typo nama kolom, syntax error, indentation
  error.
- Kode status HTTP dasar: `200`, `404`, `500` — sinyal dari server.
- `print()` sebagai "senter kode" — cara termudah melihat isi
  variabel saat curiga ada yang salah.
- Mindset: **error adalah petunjuk, bukan hukuman.**

# Penjelasan Konsep

Sama seperti Pertemuan 1 & 2 — perbedaan programmer berpengalaman
dan pemula bukan soal "tidak pernah error", tapi soal **membaca**
errornya. Baca pesan error dari baris **paling bawah** dulu — di
situ biasanya inti masalahnya. Enam error di bawah ini akan terus
kamu temui, bukan cuma di kelas ini:

| Error | Gejala | Cek |
|---|---|---|
| Route tidak ditemukan | Halaman `404 Not Found` | Alamat form ≠ `@app.route`? Cek ejaan alamatnya. |
| Database tidak ada | `unable to open database file` | File `.db` tak ditemukan — cek nama & lokasi file. |
| Tabel tidak ada | `no such table: transactions` | Belum `CREATE TABLE` — cek apakah `init_db()` sudah dipanggil. |
| Typo nama kolom | `no such column: nominl` | `nominl` ≠ `nominal` — cek ejaan kolom di query. |
| Syntax Error | Aplikasi tak mau jalan sama sekali | Kurang kurung `)` atau titik dua `:` — cek baris di pesan error. |
| Indentation Error | `IndentationError: ...` | Spasi tak rapi — Python cerewet soal ini, cek indentasi dalam function. |

**Kode status HTTP** yang paling sering kamu lihat: `200 OK`
(berhasil), `404 Not Found` (alamat tak ditemukan), `500 Internal
Server Error` (kode Python-mu bermasalah). Pola sederhana: `2xx` =
sukses, `4xx` = salah dari sisi permintaan, `5xx` = salah di kodemu.

# Langkah Pengerjaan

1. Baca tabel 6 error di atas sampai kamu bisa membayangkan masing-
   masing gejalanya.
2. Jalankan `contoh_debug.py` (`python contoh_debug.py`), tambah satu
   transaksi lewat form, lalu buka TERMINAL (bukan browser) — baca
   dua baris `print()` yang muncul di sana.
3. Kerjakan bagian **Latihan Diagnosis** di bawah — untuk tiap
   skenario, tebak dulu error apa yang MUNGKIN muncul & lapisan mana
   yang harus dicek, SEBELUM melihat kunci jawabannya.

# File Yang Diubah

Tidak ada — `contoh_debug.py` sudah lengkap, tinggal dijalankan dan
dibaca. Latihan hands-on ada di `14-buggy`.

# Latihan Diagnosis

Untuk tiap skenario, tebak dulu: error apa yang mungkin muncul, dan
di mana kamu harus mulai mencari?

1. Kamu mengetik alamat form `action="/simpan"`, tapi route di
   `app.py` ditulis `@app.route('/tambah', methods=['POST'])`.
2. Query-mu: `SELECT * FROM transactions WHERE nominl > 10000`.
3. Kamu baru saja `git clone` sebuah project dan langsung menjalankan
   `python app.py` tanpa membuat tabel dulu.
4. Aplikasi tidak mau jalan SAMA SEKALI, terminal langsung
   menunjukkan error sebelum sempat menyalakan server.

<details>
<summary>Kunci jawaban (buka setelah mencoba menebak sendiri)</summary>

1. **404 Not Found** — alamat form dan alamat route tidak cocok.
   Cek ejaan di `action="..."` HTML dan `@app.route(...)` di Python.
2. **`no such column: nominl`** — typo nama kolom di query SQL. Cek
   ejaan kolomnya, cocokkan dengan `CREATE TABLE`.
3. **`no such table: transactions`** — tabel belum pernah dibuat.
   Cek apakah ada `init_db()` (atau sejenisnya) yang dipanggil sebelum
   route pertama diakses.
4. **Syntax Error atau Indentation Error** — sesuatu di kode Python-mu
   tidak valid secara struktur (kurung tak lengkap, titik dua hilang,
   atau spasi tak konsisten). Baca baris & nomor yang disebutkan
   pesan error, itu biasanya persis di lokasi masalahnya.

</details>

# Checklist

- [ ] Bisa menjelaskan 6 error umum Flask dengan bahasa sendiri.
- [ ] Paham beda `404`, `500`, dan `200`.
- [ ] Sudah menjalankan `contoh_debug.py` dan melihat hasil `print()`
      di terminal.
- [ ] Berhasil menjawab (atau menebak dengan alasan yang masuk akal)
      keempat skenario di Latihan Diagnosis.

# Hint

- Error di terminal (tempat `python app.py` dijalankan) dan error di
  browser adalah dua hal berbeda — `500 Internal Server Error` di
  browser selalu punya detail lengkapnya di terminal.
- `print()` boleh diselipkan di MANA SAJA dalam function — sebelum
  query, setelah query, di dalam `if`. Ini alat paling sederhana tapi
  paling sering dipakai bahkan oleh programmer berpengalaman.
- Kalau kamu benar-benar buntu, `debug=True` di `app.run(debug=True)`
  membuat browser menampilkan traceback lengkap saat error terjadi —
  jangan panik melihatnya, baca dari baris paling bawah.

# Hasil Akhir

Kerangka berpikir untuk mendiagnosis error Flask sebelum panik —
bekal yang langsung kamu pakai di `14-buggy` untuk benar-benar
memperbaiki kode yang bermasalah.

# Kesalahan Yang Sering Terjadi

- **Langsung menempel pesan error ke AI/Google tanpa membacanya
  sendiri dulu** → kehilangan kesempatan melatih insting debugging.
  Baca dulu baris paling bawah, coba tebak sendiri, baru cari bantuan.
- **Panik melihat traceback panjang** → traceback selalu diakhiri
  dengan baris paling penting: jenis error & pesannya. Baris-baris di
  atasnya cuma "jejak" bagaimana error itu terjadi.
- **Mengubah banyak hal sekaligus saat debugging** → sulit tahu
  perubahan mana yang sebenarnya memperbaiki masalah. Ubah satu hal,
  simpan, coba lagi, ulangi.
