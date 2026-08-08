# 11 · Debugging

# Tujuan Belajar

Mendiagnosis lapisan & penyebab kemungkinan sebuah bug HANYA dari
gejala (pesan error, isi log) — SEBELUM membuka satu baris kode pun.
Ini latihan murni membaca gejala; folder `12-buggy` setelah ini baru
kamu benar-benar memperbaiki kode.

# Penjelasan

Modul Pertemuan 4 mengajarkan tabel "Gejala → Lapisan Tersangka":

| Gejala | Lapisan tersangka | Cara periksa |
|---|---|---|
| Halaman "Not Found" (404) | Route (`app.py`) | Ejaan URL & `@app.route` cocok? |
| Halaman error (500) | Service / Repository | Baca traceback, cari baris terakhir |
| Data tak muncul di halaman | Repository / Template | Query dapat data? Variabel dikirim ke `render_template`? |
| Data salah / tak tersimpan | Service / Repository | Validasi menolak? Lupa `commit()`? |
| Tombol / form tak bereaksi | Template / JS | `action`/`method` benar? Console browser (F12)? |
| Tampilan berantakan | Static / CSS | File CSS termuat? Tab Network 404? |

9 skenario di bawah ini masing-masing memberimu GEJALA saja (pesan
error, potongan log, atau deskripsi perilaku). Tugasmu: tebak lapisan
tersangka DAN penyebab spesifiknya, SEBELUM membuka kunci jawaban.

# Diagram

```
Gejala terlihat  →  Tentukan lapisan  →  Baca baris terakhir traceback
                     (pakai tabel di atas)  atau cek kode di lapisan itu
                          │
                          ▼
                   Punya dugaan penyebab
                          │
                          ▼
                   (di 12-buggy nanti: perbaiki & buktikan dugaanmu benar)
```

# Langkah Pengerjaan

Untuk SETIAP skenario, tulis dulu jawabanmu (lapisan tersangka +
dugaan penyebab) SEBELUM membuka `<details>` kunci jawabannya.

---

**Skenario 1 — Klik "Add Expense", muncul halaman putih dengan tulisan
besar "Not Found" dan kode `404`.**

<details>
<summary>Kunci Jawaban 1</summary>

Lapisan tersangka: **Route** (`app.py`). Penyebab paling mungkin:
`action="/create"` di `create.html` tidak cocok dengan path yang
didaftarkan di `@app.route(...)` — mungkin salah ketik (`/creat`,
`/Create`, ada/tidaknya trailing slash). 404 dari Flask HAMPIR SELALU
berarti "tidak ada route yang cocok dengan URL ini", persis kayak
`meet-03/14-buggy/bug-01-route-salah`.
</details>

---

**Skenario 2 — Terminal menunjukkan:**
```
jinja2.exceptions.TemplateNotFound: expense_list.html
```

<details>
<summary>Kunci Jawaban 2</summary>

Lapisan tersangka: **Route**, tepat di baris `render_template(...)`.
Nama file yang diminta (`expense_list.html`) tidak ada di folder
`templates/` — kemungkinan nama file aslinya beda (`expenses.html`),
atau file-nya ada tapi salah lokasi/salah ekstensi.
</details>

---

**Skenario 3 — Terminal menunjukkan:**
```
sqlite3.OperationalError: no such column: ammount
```

<details>
<summary>Kunci Jawaban 3</summary>

Lapisan tersangka: **Repository**. ITU BUKAN error Python biasa — SQL
menolak query karena nama kolom salah ketik (`ammount`, harusnya
`amount`). Karena SEMUA query hidup di `repositories/`, cari di sana
dulu — bukan di `services/` atau `app.py`.
</details>

---

**Skenario 4 — Aplikasi bahkan tidak mau START. Terminal langsung
berhenti dengan:**
```
ImportError: cannot import name 'get_expenses' from 'services.expense_service'
```

<details>
<summary>Kunci Jawaban 4</summary>

Lapisan tersangka: **Import / nama function**. Ini terjadi SEBELUM
aplikasi sempat menerima satu request pun — artinya `app.py` (atau
file lain) mencoba `from services.expense_service import
get_expenses`, tapi function di dalam `expense_service.py` sebenarnya
bernama beda (misalnya `get_all_expenses`). Solusi: samakan nama yang
di-import dengan nama function yang BENAR-BENAR ada.
</details>

---

**Skenario 5 — Klik detail sebuah expense yang BARU SAJA dihapus orang
lain (di tab browser lain). Muncul error 500, traceback baris
terakhir:**
```
TypeError: 'NoneType' object is not subscriptable
```

<details>
<summary>Kunci Jawaban 5</summary>

Lapisan tersangka: **Route atau Service**, tepat SETELAH pemanggilan
`get_expense_by_id(id)`. `.fetchone()` mengembalikan `None` karena
baris itu sudah dihapus, tapi kode SETELAHNYA mencoba mengakses
`expense['title']` atau `expense.title` tanpa mengecek `None` dulu.
Ini persis kasus `meet-03/14-buggy/bug-06-variable-none`.
</details>

---

**Skenario 6 — Form Add Expense disubmit, tapi field `notes` yang
diisi user TIDAK PERNAH sampai ke database (selalu kosong).**

<details>
<summary>Kunci Jawaban 6</summary>

Lapisan tersangka: **Template atau Route**. Kemungkinan besar
`<textarea>` di `create.html` tidak punya atribut `name="notes"` yang
benar (atau salah ketik), sehingga `request.form.get("notes")` di
`app.py`/`services/` selalu mendapat nilai kosong — bukan karena
database menolaknya.
</details>

---

**Skenario 7 — Tombol "Delete" di halaman `/expenses` diklik, tapi
TIDAK terjadi apa-apa sama sekali (tidak error, tidak redirect, tidak
ada modal muncul).**

<details>
<summary>Kunci Jawaban 7</summary>

Lapisan tersangka: **Static/JS**, BUKAN Python sama sekali. Tombol ini
memicu `onclick="openDeleteModal(...)"` (JavaScript), bukan langsung
submit form. Buka Console browser (F12) — kemungkinan ada error
JavaScript (`openDeleteModal is not defined`, biasanya karena
`static/js/app.js` gagal dimuat — cek tab Network apakah file-nya
404).
</details>

---

**Skenario 8 — `logs/app.log` menunjukkan baris ini berulang-ulang
setiap kali server start:**
```
CRITICAL | database.db | Database initialization failed: unable to open database file
```

<details>
<summary>Kunci Jawaban 8</summary>

Lapisan tersangka: **Database / konfigurasi**. `sqlite3.connect(...)`
gagal karena folder tempat file database seharusnya dibuat tidak bisa
diakses/dibuat — bisa karena `DATABASE_PATH` di `.env` menunjuk ke
folder yang tidak ada izin tulis, atau path-nya salah ketik total.
`CRITICAL` (bukan `ERROR`) menandakan ini kegagalan FATAL — aplikasi
tidak bisa jalan sama sekali sampai ini diperbaiki.
</details>

---

**Skenario 9 — User mengetik `/edit/lima` di address bar (bermaksud
mengedit expense nomor 5, tapi mengetik kata "lima").**

<details>
<summary>Kunci Jawaban 9</summary>

Lapisan tersangka: **Route**, tapi ini BUKAN bug — ini perilaku yang
BENAR. `<int:expense_id>` menolak apa pun yang bukan angka SEBELUM
function `edit()` sempat dijalankan, otomatis menghasilkan 404 dari
Flask sendiri. Ini beda dengan `/edit/99999` (angka valid tapi id
tidak ada di database) yang JUSTRU tidak 404, seperti sudah dibahas
di `07-route-analysis`.
</details>

---

# File Yang Diubah

Tidak ada — folder ini murni diagnosis dari teks, tanpa kode untuk
dijalankan.

# Checklist

- [ ] Sudah menjawab (menulis dugaan) SEMUA 9 skenario SEBELUM
      membuka kunci jawabannya masing-masing.
- [ ] Skor sendiri: dari 9, berapa yang tebakan lapisannya BENAR
      (walau detail penyebabnya belum tepat)?
- [ ] Paham perbedaan Skenario 3 (SQL typo, di Repository) vs
      Skenario 6 (field HTML salah nama, di Template/Route) — dua hal
      yang gejalanya bisa terasa mirip ("data tidak masuk") tapi
      penyebabnya di lapisan BEDA.

# Hint

- Baca pesan error dari baris PALING BAWAH dulu — itu prinsip yang
  sama dari `meet-03/13-debugging`, dan berlaku juga di sini.
- `CRITICAL` di log SELALU lebih serius dari `ERROR` — kalau kamu
  lihat `CRITICAL`, curigai sesuatu yang mencegah aplikasi START sama
  sekali, bukan cuma satu request yang gagal.
- Kalau bingung antara "bug di Python" vs "bug di JavaScript/CSS",
  ingat: error Python SELALU muncul di terminal tempat `python app.py`
  dijalankan. Error JavaScript SELALU muncul di Console browser (F12)
  — dua tempat yang berbeda, jangan tertukar saat mencari.

# Hasil yang Diharapkan

Dari gejala/pesan error SAJA (tanpa kode), kamu bisa mempersempit
kemungkinan penyebab ke SATU atau DUA lapisan spesifik — bukan
menebak-nebak ke seluruh project.

# Refleksi

1. Skenario mana yang paling mengecoh buatmu? Kenapa gejalanya
   membuatmu curiga ke lapisan yang salah pada awalnya?
2. Kalau kamu adalah engineer yang baru gabung tim dan menerima
   laporan bug tanpa traceback sama sekali (cuma "aplikasinya error"),
   pertanyaan APA yang akan kamu tanyakan balik ke pelapor supaya bisa
   mendiagnosis seperti di folder ini?
