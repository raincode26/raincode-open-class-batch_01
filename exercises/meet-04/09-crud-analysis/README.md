# 09 · CRUD Analysis

# Tujuan Belajar

Menggabungkan SEMUA yang sudah dipelajari di folder 03–08 jadi satu
gambar utuh: flow CREATE lengkap, dari klik tombol sampai commit ke
database, sebagai satu diagram yang bisa kamu jelaskan tanpa membuka
kode.

# Penjelasan

Ini folder "penyatuan", bukan folder baru. Kamu sudah baca HTML-nya
(`04`), Python-nya (`06`), route-nya (`07`), dan database-nya (`08`)
secara terpisah — sekarang kita rangkai jadi SATU alur, dari sisi
CREATE saja (fitur paling sering dipakai untuk lacak-melacak).

```
title="Kopi pagi", amount=25000, category="Food"

1. templates/create.html
   <form action="/create" method="POST">
   <input name="title">  <input name="amount">  <select name="category">
                                │
                                ▼ (klik "Add Expense")
2. app.py → def create():
   if request.method == "POST":
       try:
           expense_service.create_expense(request.form)
                                │
                                ▼
3. services/expense_service.py → create_expense(data)
   cleaned = self._validate_and_clean(data)
     ├─ title kosong? → raise ValueError
     ├─ amount < 0.01? → raise ValueError
     └─ category tidak di EXPENSE_CATEGORIES? → raise ValueError
   return self.repository.create_expense(**cleaned)
                                │
                                ▼
4. repositories/expense_repository.py → create_expense(...)
   sql = "INSERT INTO expenses (title, amount, category, notes) VALUES (?, ?, ?, ?)"
   conn.execute(sql, (title, amount, category, notes))
   conn.commit()          ← titik BALIK, data resmi tersimpan
                                │
                                ▼
5. app.py (lanjutan create(), setelah return dari langkah 3)
   flash("Expense added successfully!")
   return redirect(url_for("expenses"))
                                │
                                ▼
6. Browser mengikuti redirect → GET /expenses
   → app.py def expenses() → service.get_expenses() → repository.get_expenses()
   → SELECT ... FROM expenses ORDER BY ... → render_template("expenses.html", ...)
                                │
                                ▼
7. User melihat "Kopi pagi" muncul di tabel daftar expense.
```

# Diagram

```
   Tambah                Route              Request            SQL
┌─────────┐  submit  ┌─────────┐  request  ┌─────────┐  panggil  ┌──────────┐
│  Form    │ ───────▶ │ create()│ ────────▶│.form.get│ ────────▶│  Service │
└─────────┘           └─────────┘           └─────────┘           └────┬─────┘
                                                                       │
                                                                       ▼
   Render               Redirect            Commit              Repository
┌─────────┐  sukses  ┌─────────┐  simpan  ┌─────────┐  jalankan ┌──────────┐
│expenses  │ ◀────────│ flash + │◀─────────│ commit()│◀──────────│  INSERT  │
│  .html   │           │redirect │          └─────────┘           └──────────┘
└─────────┘           └─────────┘
```

# Langkah Pengerjaan

1. Cetak atau salin diagram tujuh langkah di atas ke kertas/catatan.
2. Untuk SETIAP nomor (1–7), buka file yang disebut, dan tunjuk
   BARIS PERSIS yang melakukan hal itu. Tulis nomor barisnya di
   sebelah tiap langkah di catatanmu.
3. Ulangi proses yang SAMA, tapi kali ini untuk flow **UPDATE**
   (`edit()`). Apa yang beda dari flow CREATE? (Petunjuk: ada satu
   langkah TAMBAHAN di awal yang tidak ada di CREATE — mengambil data
   lama dulu sebelum menampilkan form.)
4. Ulangi sekali lagi untuk flow **DELETE**. Kali ini flow-nya jauh
   lebih pendek — kenapa? (Tidak ada validasi input sama sekali,
   cuma perlu tahu `id`-nya.)
5. Bandingkan ketiga diagram (Create, Update, Delete) berdampingan.
   Bagian mana yang SELALU sama di ketiganya, bagian mana yang
   berbeda?

# File Yang Diubah

Tidak ada — folder ini murni membaca & merangkai apa yang sudah dibaca
sebelumnya.

# Checklist

- [ ] Diagram 7 langkah CREATE sudah kamu tandai dengan nomor baris
      asli dari kode.
- [ ] Diagram UPDATE dan DELETE versimu sendiri sudah selesai dibuat.
- [ ] Bisa menjawab: "bagian apa dari flow CRUD yang SELALU identik,
      tidak peduli operasinya Create/Read/Update/Delete?"

# Hint

- Ini folder untuk MERANGKAI, bukan membaca file baru. Kalau kamu
  masih ragu di satu langkah, itu tandanya perlu kembali sebentar ke
  folder `06` atau `07`, bukan menebak-nebak di sini.
- Perhatikan: `commit()` HANYA muncul di flow Create, Update, Delete
  — TIDAK PERNAH di flow Read (`SELECT`). Itu karena `commit()`
  cuma dibutuhkan untuk perubahan permanen data, sedangkan `SELECT`
  cuma MEMBACA, tidak mengubah apa pun.
- Kalau kesulitan menulis diagram Update/Delete versimu sendiri,
  ambil format yang sama persis dengan diagram Create di atas, lalu
  ganti isi tiap kotak sesuai kode `edit()`/`delete()`.

# Hasil yang Diharapkan

Kamu punya TIGA diagram (Create, Update, Delete) hasil kerjamu
sendiri, dan bisa menjelaskan ketiganya ke orang lain tanpa membuka
kode sama sekali.

# Refleksi

1. Kenapa flow DELETE jauh lebih pendek daripada CREATE/UPDATE (tidak
   ada validasi `_validate_and_clean`)? Apakah itu berarti DELETE
   "lebih aman", atau justru sebaliknya?
2. Bayangkan kamu perlu menambah fitur "Duplicate Expense" (klik satu
   tombol, expense yang sama tersalin jadi baris baru). Dari diagram
   Create/Read yang sudah kamu buat, langkah mana saja yang bisa kamu
   PAKAI ULANG, dan langkah mana yang perlu ditulis baru?
