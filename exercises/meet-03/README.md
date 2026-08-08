# Pertemuan 3 — Membangun Aplikasi Pertama

Flask · SQLite · CRUD. Minggu lalu form-mu hidup di browser tapi datanya
selalu hilang begitu halaman ditutup. Minggu ini, form itu benar-benar
**mengingat** — tersimpan, bisa dilihat lagi, diubah, dihapus. Project
akhirnya: **Expense Tracker**, aplikasi pencatat pengeluaran sungguhan.

Bahannya sudah kamu punya:

| Modal dari... | Dipakai lagi di... |
|---|---|
| Pertemuan 1 — variabel, if-else, function | Logika di dalam route Flask |
| Pertemuan 2 — HTML form, CSS | Halaman yang mengirim & menampilkan data |
| **Baru minggu ini** | Flask (jembatan) + SQLite (ingatan) |

## Model Mental Kunci

Setiap aplikasi, sehebat apa pun, hanya melakukan tiga hal:

```
INPUT (form)  →  PROCESS (Flask + Python)  →  OUTPUT (halaman terisi)
```

Dan seperti restoran: **Frontend** = pelanggan (yang dilihat),
**Flask** = pelayan (jembatan), **Python** = dapur (olah data),
**SQLite** = gudang (simpan data). Data pergi ke database, lalu
**pulang** lagi ke layar — itulah cara semua aplikasi bekerja.

## Urutan Belajar

Setiap folder membangun folder sebelumnya — ini **satu** Expense
Tracker yang tumbuh sedikit demi sedikit, bukan 16 contoh terpisah.

| # | Folder | Yang ditambahkan | Alur |
|---|---|---|---|
| 1 | [01-flask-hello-world](01-flask-hello-world) | Aplikasi Flask 6 baris pertama | Fondasi |
| 2 | [02-route](02-route) | Banyak alamat halaman (`route`) | Fondasi |
| 3 | [03-template-render](03-template-render) | HTML lewat `render_template` + Jinja | Fondasi |
| 4 | [04-form-request](04-form-request) | Menerima data form via `request` | Fondasi |
| 5 | [05-sqlite-basic](05-sqlite-basic) | SQLite tanpa Flask dulu — koneksi & query | Database |
| 6 | [06-create-table](06-create-table) | Tabel `transactions` di dalam Flask | CRUD dimulai |
| 7 | [07-create-expense](07-create-expense) | **C**reate — simpan pengeluaran baru | CRUD |
| 8 | [08-read-expense](08-read-expense) | **R**ead — tampilkan daftar pengeluaran | CRUD |
| 9 | [09-update-expense](09-update-expense) | **U**pdate — edit pengeluaran | CRUD |
| 10 | [10-delete-expense](10-delete-expense) | **D**elete — hapus pengeluaran | CRUD |
| 11 | [11-complete-crud](11-complete-crud) | Full CRUD + kolom kategori & tanggal | CRUD selesai |
| 12 | [12-read-source-code](12-read-source-code) | Membaca `projects/expense-tracker/final` (project nyata) | Membaca kode |
| 13 | [13-debugging](13-debugging) | 6 error umum Flask & cara membacanya | Debugging |
| 14 | [14-buggy](14-buggy) | Cari & perbaiki 6 bug Flask+SQLite realistis | Debugging |
| 15 | [15-challenge](15-challenge) | Easy → Medium → Hard | Uji diri |
| 16 | [16-solution](16-solution) | Kunci jawaban seluruh challenge | Pembanding |

## Cara Menjalankan

Setiap folder dari `06-create-table` seterusnya adalah aplikasi Flask
mandiri (`app.py` + `templates/`). Tidak ada langkah tersembunyi.

1. **Sekali saja** di awal — pasang Flask:
   ```
   pip install flask
   ```
2. Masuk ke folder latihan yang ingin dikerjakan.
3. Jalankan:
   ```
   python app.py
   ```
4. Buka `http://localhost:5000` di browser.
5. Berhenti server dengan `Ctrl+C` di terminal.

File database (`expense_tracker.db`) dibuat **otomatis** saat aplikasi
pertama kali jalan — kamu tidak perlu membuatnya manual.

## Prinsip Belajar

- **Konsep dulu, syntax nanti.** Kamu tidak perlu hafal kode Flask —
  cukup paham alurnya: form → Flask → Python → SQLite → Python →
  HTML → layar.
- **Aplikasi itu tidak ajaib.** Ia hanya menyimpan & menampilkan data.
  Itu saja intinya.
- **Error tetap teman.** Sama seperti Pertemuan 1 & 2 — baca pesannya
  dari baris paling bawah, itu peta menuju solusi, bukan hukuman.
- **`WHERE` adalah aturan emas.** `UPDATE`/`DELETE` tanpa `WHERE`
  mengubah/menghapus **seluruh tabel**. Selalu double-check.
- **`14-buggy` sebelum `15-challenge`.** Kebiasaan membaca &
  memperbaiki kode orang lain adalah bekal sebelum menulis dari nol.

## Checklist Sebelum Lanjut ke Pertemuan 4

- [ ] Paham Flask sebagai jembatan HTML ↔ Python (`route`, `@app.route`, `app.run()`).
- [ ] Bisa membaca & menulis `render_template` + Jinja (`{% for %}`, `{{ }}`, `{% if %}`).
- [ ] Bisa mengambil data form lewat `request.form`.
- [ ] Hafal 4 operasi CRUD & perintah SQL pasangannya (Create=INSERT, Read=SELECT, Update=UPDATE, Delete=DELETE).
- [ ] Paham kenapa `db.commit()` wajib setelah INSERT/UPDATE/DELETE.
- [ ] Bisa membaca alur satu aksi ("klik Simpan") menembus HTML → Flask → SQLite → HTML lagi.
- [ ] Bisa menentukan lapisan mana yang bermasalah saat ada error.

RainCode Open Class · Understand before memorizing.
