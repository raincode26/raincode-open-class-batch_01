# 07 · Route Analysis

# Tujuan Belajar

Untuk SETIAP route di `projects/expense-tracker/final/`, bisa menjawab
persis: "apa yang terjadi, langkah demi langkah, saat route ini
dipanggil?" — termasuk kasus-kasus yang TIDAK terlihat jelas dari
sekilas baca (seperti: apa yang terjadi kalau id tidak ada?).

# Penjelasan

Ada 6 route + 2 error handler. Tabel ini rangkumannya — tapi JANGAN
hafalkan tabelnya, buktikan sendiri lewat Langkah Pengerjaan.

| Route | Method | Fungsi |
|---|---|---|
| `/` | GET | Dashboard — total, ringkasan kategori, 5 transaksi terbaru |
| `/expenses` | GET | Daftar lengkap, mendukung `?search=`, `?category=`, `?sort=`, `?order=` |
| `/create` | GET, POST | GET = tampilkan form kosong. POST = proses submit |
| `/edit/<int:expense_id>` | GET, POST | GET = tampilkan form terisi. POST = proses update |
| `/delete/<int:expense_id>` | POST saja | Hapus — SENGAJA tidak menerima GET |
| `/summary` | GET | Analitik: total per kategori |

Tiga perilaku yang MUDAH terlewat kalau cuma baca sekilas:

- **`/delete/<id>` menolak GET.** Coba buka `/delete/1` langsung dari
  address bar browser (itu request GET) — akan gagal, karena route-nya
  cuma didaftarkan untuk `methods=["POST"]`. Ini pertahanan supaya
  crawler/prefetch browser tidak SECARA TIDAK SENGAJA memicu hapus data
  cuma karena mengunjungi sebuah link.
- **id yang tidak ada BUKAN 404.** `/edit/99999` (id yang valid secara
  format tapi tidak ada di database) TIDAK menampilkan halaman 404 —
  ia flash pesan "Expense not found." lalu redirect ke `/expenses`.
  Beda dengan `/edit/abc` (id yang bukan angka sama sekali) yang
  MEMANG langsung 404, karena `<int:expense_id>` menolaknya sebelum
  masuk ke function sama sekali.
- **Sukses = redirect, gagal validasi = render ulang form (bukan
  redirect).** Ini pola "Post/Redirect/Get" — kalau submit BERHASIL,
  user diarahkan ke halaman lain (supaya refresh browser tidak
  mengirim ulang form). Kalau GAGAL validasi, form yang SAMA dirender
  ulang dengan data yang tadi diketik, supaya user tidak perlu
  mengetik ulang dari nol.

# Diagram

```
POST /create
   │
   ▼
expense_service.create_expense(data)
   │
   ├─ valid ──▶ tersimpan ──▶ flash("sukses") ──▶ redirect("/expenses")
   │
   └─ invalid (ValueError) ──▶ flash(pesan error) ──▶ render_template("create.html")
                                                        (form_data = input tadi, TIDAK hilang)
```

# Langkah Pengerjaan

1. (Kalau project sedang berjalan dari `01-project-overview`) Buka
   `/` di browser. Baca `app.py` function `index()` sambil melihat
   halamannya — cocokkan tiap angka/tabel yang tampil dengan baris
   kode yang menghasilkannya.
2. Coba akses `/delete/1` langsung dengan MENGETIK URL-nya di address
   bar (ini mengirim request GET). Apa yang terjadi? Buka `app.py`,
   cari baris `methods=[...]` pada route `/delete/<int:expense_id>`
   untuk mengonfirmasi kenapa.
3. Coba akses `/edit/99999` (ganti dengan id yang PASTI tidak ada).
   Baca function `edit()` di `app.py` — cari baris yang mengecek
   `if expense is None:` SEBELUM try/except dimulai. Bandingkan
   dengan mencoba `/edit/abc` (bukan angka) — kenapa hasilnya beda
   (404 vs redirect + flash)?
4. Submit form `/create` dengan `amount` diisi teks bukan angka (mis.
   `"gratis"`). Baca `services/expense_service.py`, cari baris yang
   menangkap kasus ini (`try: float(amount_s) except ValueError:`).
5. Buat satu tabel sendiri (boleh di kertas): untuk MASING-MASING dari
   6 route, tulis "apa yang terjadi kalau input valid" dan "apa yang
   terjadi kalau input TIDAK valid / tidak ditemukan".

# File Yang Diubah

Tidak ada — folder ini murni membaca (dan mengklik-klik, kalau project
sedang dijalankan).

# Checklist

- [ ] Sudah mencoba (atau membaca & membuktikan lewat kode) bahwa
      `/delete/<id>` menolak GET.
- [ ] Paham beda perilaku `/edit/99999` (id valid tapi tidak ada →
      redirect + flash) vs `/edit/abc` (bukan angka sama sekali →
      404 otomatis dari Flask).
- [ ] Tabel "input valid vs tidak valid" untuk 6 route sudah terisi.

# Hint

- `<int:expense_id>` di path route adalah "penjaga gerbang" paling
  awal — Flask menolaknya SEBELUM function kamu bahkan mulai
  dijalankan, kalau bagian itu bukan angka.
- Kalau ingin tahu KENAPA `/delete` sengaja menolak GET, ini prinsip
  keamanan umum (bukan cuma project ini): request GET dianggap "aman"
  (tidak boleh mengubah apa pun) — banyak alat (bot, browser
  prefetch, link preview) mem-fetch URL GET secara otomatis TANPA
  sepengetahuan user. Kalau `/delete` menerima GET, sekadar
  MENGARAHKAN kursor ke sebuah link bisa memicu penghapusan.
- Flash message hanya tampil SATU KALI (di request berikutnya setelah
  di-set), lalu otomatis hilang — itu sebabnya kalau kamu refresh
  halaman yang sudah menampilkan flash, pesannya tidak muncul lagi.

# Hasil yang Diharapkan

Untuk keenam route, kamu bisa menjawab tanpa ragu: "apa yang terjadi
kalau saya panggil route ini dengan data X" — baik untuk kasus normal
maupun kasus aneh (id salah, input kosong, format salah).

# Refleksi

1. Kenapa `/edit/<id_tidak_ada>` TIDAK menampilkan halaman 404,
   padahal secara logika "data tidak ditemukan" terdengar mirip
   dengan "halaman tidak ditemukan"? Menurutmu, mana pengalaman yang
   lebih baik untuk user: 404, atau flash message + redirect?
2. Bayangkan kamu diminta menambah route baru `/duplicate/<int:id>`
   (menyalin sebuah expense jadi entry baru). Route mana yang paling
   mirip untuk ditiru polanya? Apa yang perlu kamu ubah?
