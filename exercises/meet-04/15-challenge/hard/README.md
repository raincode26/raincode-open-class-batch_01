# Challenge Hard · Cegah Title Duplikat

# Tujuan Belajar

Menyelesaikan validasi yang melibatkan DUA lapisan sekaligus
(Repository harus mengecek data yang SUDAH ADA, Service harus
memutuskan apakah itu dianggap error) — dan menangani kasus khusus
yang gampang terlewat: edit tanpa mengubah title tidak boleh dianggap
"duplikat dengan dirinya sendiri".

# Penjelasan

Sekarang, dua expense boleh punya title yang PERSIS SAMA (misalnya dua
baris "Kopi pagi"). Tugasmu: cegah itu — title baru (Create) atau
title hasil edit (Update) tidak boleh sama dengan title expense LAIN
yang sudah ada (perbandingan case-insensitive: "Kopi" dan "kopi"
dianggap SAMA).

Bagian tersulit: kalau user MENGEDIT expense "Kopi pagi" tapi cuma
mengubah amount-nya (title tetap "Kopi pagi"), itu BUKAN duplikat —
dia membandingkan dengan dirinya sendiri. Function `title_exists`
karena itu butuh parameter `exclude_id`.

# Diagram

```
CREATE (exclude_id=None)              EDIT (exclude_id=id yang diedit)

title_exists("Kopi", None)            title_exists("Kopi", exclude_id=3)
  → cek SEMUA baris                     → cek SEMUA baris KECUALI id=3
  → True kalau ADA yang sama            → True kalau ADA YANG LAIN sama
```

# Langkah Pengerjaan

1. Jalankan `python app.py`, tambah expense "Kopi pagi". Tambah LAGI
   expense dengan title "Kopi pagi" (persis sama) — buktikan dulu
   bahwa saat ini KEDUANYA berhasil tersimpan (belum ada pencegahan).
2. Buka `repository.py`, cari `TODO 1`. Lengkapi `title_exists(...)`.
3. Buka `service.py`, cari `TODO 2` di dalam `_validate`. Panggil
   `title_exists(title, exclude_id=exclude_id)`, dan `raise
   ValueError(...)` kalau hasilnya `True`.
4. Uji ulang: tambah "Kopi pagi" dua kali → yang kedua harus ditolak.
5. Uji kasus khusus: edit expense "Kopi pagi" yang SUDAH ada, ubah
   HANYA amount-nya (title tetap "Kopi pagi"), klik Update — ini
   HARUS berhasil, TIDAK boleh ditolak sebagai duplikat.

# File Yang Diubah

- `repository.py`
- `service.py`

# Checklist

- [ ] Menambah expense dengan title yang SUDAH ADA (persis sama atau
      beda huruf besar/kecil) ditolak dengan pesan error yang jelas.
- [ ] Mengedit expense TANPA mengubah title-nya tetap berhasil
      (tidak dianggap duplikat dengan dirinya sendiri).
- [ ] Mengedit expense DENGAN mengubah title jadi title yang sudah
      dipakai expense lain tetap DITOLAK.

# Hint

- Kalau lupa mengirim `exclude_id` saat memanggil `title_exists` dari
  `edit_expense`, gejalanya: user TIDAK BISA edit expense apa pun
  tanpa mengubah title-nya — selalu ditolak "duplikat" padahal
  sebenarnya itu dirinya sendiri.
- `LOWER(...)` di SQL membuat perbandingan tidak peduli huruf besar/
  kecil — `LOWER("Kopi") = LOWER("kopi")` bernilai `True` di SQLite.
- Ini pola validasi yang BEDA dari yang lain di `_validate` — validasi
  lain (title kosong, amount) cuma melihat DATA YANG BARU MASUK.
  Validasi ini perlu bertanya ke DATABASE dulu ("apakah sudah ada
  yang seperti ini?") — makanya butuh Repository, bukan cuma Service.

# Hasil yang Diharapkan

Aplikasi yang menolak title duplikat saat Create maupun Edit, TAPI
tetap membiarkan user meng-edit expense-nya sendiri tanpa terjebak
validasi yang salah paham.

# Refleksi

1. Kenapa validasi "title kosong" bisa dicek TANPA menyentuh
   database sama sekali, sementara validasi "title duplikat" TIDAK
   BISA? Apa yang membedakan dua jenis validasi ini?
2. Bayangkan project ini dipakai BANYAK user sekaligus (bukan cuma
   kamu). Apakah pengecekan `title_exists` lalu `create_expense`
   (dua langkah terpisah) BENAR-BENAR menjamin tidak ada duplikat
   kalau dua user menyimpan title yang sama PERSIS di detik yang
   sama? (Tidak perlu menjawab teknis mendalam — cukup sadari
   pertanyaannya ada.)
