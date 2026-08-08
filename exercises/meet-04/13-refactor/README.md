# 13 · Refactor

# Tujuan Belajar

Merapikan kode yang SUDAH BENAR (tidak ada bug) tapi berbau — function
kepanjangan, kode duplikat, magic number, magic string — TANPA
mengubah perilakunya sedikit pun.

# Penjelasan

`app.py` di folder ini BERFUNGSI 100% benar (sudah dites: Add, Edit,
Delete semua bekerja). Tapi kalau kamu baca isinya, ada 4 bau kode
klasik yang sudah kamu kenali polanya dari `projects/expense-tracker/final/`
(yang TIDAK punya bau-bau ini):

1. **Function terlalu panjang** — `create()` dan `edit()` masing-
   masing melakukan SEMUANYA sendiri: ambil input, validasi, akses
   database, render response. Bandingkan dengan project referensi:
   route di sana HANYA memanggil `service`, tidak pernah menulis SQL
   atau logika validasi sendiri.
2. **Duplicate code** — blok validasi (cek title kosong, amount
   valid, dst.) DITULIS ULANG PERSIS SAMA di `create()` DAN `edit()`.
   Kalau besok aturan validasi berubah (misal: title maksimal 200
   karakter), kamu harus ingat mengubahnya di DUA tempat — gampang
   lupa satu.
3. **Magic number** — angka `0.01` dan `999999999.99` muncul berulang
   tanpa nama, tersebar di beberapa tempat. Pembaca kode tidak tahu
   ANGKA ITU MEWAKILI APA tanpa menebak dari konteks.
4. **Magic string** — daftar `["Food", "Transport", "Bills",
   "Entertainment", "Other"]` diketik ULANG sebanyak 8 KALI di file
   ini. Satu typo di salah satu tempat = bug yang susah dilacak.

# Diagram

```
SEBELUM (sekarang)                     SESUDAH (targetmu)

app.py (1 file, ~200 baris)            app.py       (route saja)
├─ index()   → SQL langsung               │
├─ create()  → validasi + SQL             ▼
│              (DUPLIKAT dari edit)     service.py   (validasi, 1 tempat)
└─ edit()    → validasi + SQL             │
               (DUPLIKAT dari create)     ▼
                                        repository.py (SQL, 1 tempat)
                                           │
                                           ▼
                                        database.py  (koneksi & skema)
```

# Langkah Pengerjaan

1. Jalankan `python app.py` DULU, coba semua fiturnya (Add, Edit,
   Delete, filter). Catat perilakunya — ini "kontrak" yang TIDAK
   boleh berubah setelah refactor.
2. Buat file baru `database.py` — pindahkan `get_db()` dan skema
   `CREATE TABLE` ke sana (lihat `01-11` untuk contoh pola yang
   sama persis dari project referensi, atau folder `12-buggy` untuk
   contoh struktur file yang sudah terpisah).
3. Buat file baru `repository.py` — pindahkan SEMUA query SQL
   (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) ke sana sebagai
   function-function terpisah (`get_all_expenses`,
   `get_expense_by_id`, `create_expense`, `update_expense`,
   `delete_expense`, `get_total`).
4. Buat file baru `service.py` — pindahkan logika validasi ke SATU
   function (`_validate`), lalu panggil function itu dari KEDUA
   `add_expense()` dan `edit_expense()` — bukan ditulis ulang dua
   kali.
5. Di `service.py`, ganti angka `0.01` dan `999999999.99` jadi
   konstanta bernama (`MIN_AMOUNT`, `MAX_AMOUNT`). Ganti daftar
   kategori yang diketik berulang jadi SATU konstanta `CATEGORIES` di
   bagian atas file.
6. Rapikan `app.py` supaya HANYA berisi route — setiap route memanggil
   `service`, tidak pernah menyentuh SQL atau aturan validasi
   langsung.
7. Jalankan lagi, uji ULANG semua fitur dari Langkah 1. Perilakunya
   HARUS identik dengan sebelum refactor.

# File Yang Diubah

- `app.py` (dirapikan, jadi lebih pendek)
- `database.py` (baru)
- `repository.py` (baru)
- `service.py` (baru)

# Checklist

- [ ] `app.py` tidak lagi mengandung `sqlite3` atau query SQL apa pun.
- [ ] Validasi (title/amount/category) HANYA ditulis SATU KALI, dipakai
      ulang oleh `create()` maupun `edit()`.
- [ ] Tidak ada lagi angka `0.01` / `999999999.99` yang "telanjang"
      tanpa nama di dalam kode.
- [ ] Daftar kategori HANYA didefinisikan SATU KALI di seluruh project.
- [ ] Semua fitur (Add, Edit, Delete, filter search & category) masih
      bekerja PERSIS SAMA seperti sebelum refactor.

# Hint

- Refactor TIDAK BOLEH mengubah PERILAKU aplikasi — kalau ada fitur
  yang tadinya bekerja lalu berhenti bekerja setelah kamu rapikan,
  itu bukan refactor yang berhasil, itu bug baru.
- Kerjakan SATU langkah kecil dulu (misalnya cuma pindahkan
  `get_db()` ke `database.py`), jalankan & tes, BARU lanjut ke
  langkah berikutnya. Jangan mengubah semuanya sekaligus lalu baru
  dites di akhir — kalau ada yang salah, kamu tidak akan tahu langkah
  mana penyebabnya.
- Struktur akhir yang kamu tuju SAMA PERSIS dengan yang sudah kamu
  lihat di folder `12-buggy` (app.py + service.py + repository.py +
  database.py) — kalau ragu, buka salah satu folder di sana sebagai
  rujukan pola (bukan untuk disalin persis, ukurannya beda).

# Hasil yang Diharapkan

`app.py` yang jauh lebih pendek, tanpa duplikasi, tanpa angka/string
"telanjang" — dan SEMUA fitur tetap bekerja seperti semula.

# Refleksi

1. Setelah refactor, kalau besok ada permintaan "amount minimum
   dinaikkan jadi 1000, bukan 0.01 lagi", di file mana PERSIS kamu
   akan mengubahnya? Bandingkan dengan seberapa banyak tempat yang
   perlu diubah SEBELUM refactor.
2. Kenapa refactor sebaiknya dilakukan SEDIKIT DEMI SEDIKIT (satu
   perubahan kecil, tes, lanjut), bukan sekaligus menulis ulang semua
   file dari nol?
