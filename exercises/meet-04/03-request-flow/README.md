# 03 · Request Flow

# Tujuan Belajar

Menghafal SATU diagram — alur satu request menembus semua lapisan —
karena diagram ini adalah kunci untuk membaca APAPUN di folder-folder
setelah ini.

# Penjelasan

Setiap kali user melakukan sesuatu di browser (klik, submit form,
buka halaman), terjadi perjalanan data yang SELALU mengikuti pola yang
sama, apa pun fiturnya:

1. **Browser** mengirim request (GET saat buka halaman, POST saat
   submit form) ke sebuah URL.
2. **Route** (`app.py`) menerima request itu — mencocokkan URL dengan
   `@app.route(...)` yang terdaftar, lalu memanggil function-nya.
3. Route mengambil input (`request.form` atau `request.args`), lalu
   mengoper ke **Service**.
4. **Service** memvalidasi & memutuskan (boleh disimpan? boleh
   dihapus?), lalu memanggil **Repository**.
5. **Repository** menjalankan query SQL ke **Database**.
6. Hasilnya naik LAGI lewat jalur yang sama secara terbalik: Database
   → Repository → Service → Route.
7. Route memanggil `render_template(...)` (kirim HTML) atau
   `redirect(...)` (arahkan ke halaman lain).
8. **Browser** menerima HTML/redirect itu dan menampilkannya ke user.

Data **turun** untuk disimpan, lalu **naik** lagi untuk ditampilkan.
Ini pola yang sama untuk Instagram, Shopee, atau aplikasi apa pun yang
pernah kamu pakai — bedanya cuma detail di tiap kotak.

# Diagram

```
⬇ REQUEST (data turun)              ⬆ RESPONSE (data naik)

🌐 Browser                          😊 User lihat hasil
    │                                    ▲
    ▼                                    │
🚪 Route (app.py)                   🚪 Route (app.py)
    │                                    ▲
    ▼                                    │
🧠 Service (services/)              🧠 Service (services/)
    │                                    ▲
    ▼                                    │
🗄 Repository (repositories/)       🗄 Repository (repositories/)
    │                                    ▲
    ▼                                    │
💾 Database (SQLite) ───────────────────┘
   titik balik — data tersimpan di sini
```

# Langkah Pengerjaan

1. Buka `projects/expense-tracker/final/app.py`, cari function `create()`
   (route `/create`, POST). JANGAN baca isinya detail dulu — cukup
   hitung: ada berapa BARIS di function ini yang benar-benar
   memanggil lapisan lain (`expense_service.something(...)`)?
2. Buka `services/expense_service.py`, cari function yang dipanggil
   dari Langkah 1 (`create_expense`). Cek: apakah function ini
   memanggil `repositories/`? Baris mana?
3. Buka `repositories/expense_repository.py`, cari function yang
   dipanggil dari Langkah 2. Ini seharusnya function TERAKHIR dalam
   rantai — ia langsung bicara ke `database/db.py`.
4. Sekarang lakukan sebaliknya: mulai dari `repositories/`, telusuri
   BALIK ke `services/`, lalu ke `app.py`. Perhatikan: apa yang
   di-`return` di tiap lapisan, dan ke mana nilai itu pergi.
5. Gambar ulang diagram di atas dengan TANGANMU SENDIRI (kertas atau
   catatan), tapi isi tiap kotak dengan nama FILE & FUNCTION asli dari
   `projects/expense-tracker/final/` (bukan lagi nama generik "Route",
   "Service").

# File Yang Diubah

Tidak ada — folder ini murni membaca.

# Checklist

- [ ] Bisa menyebutkan urutan lapisan dari ingatan: Browser → ... →
      Database → ... → Browser, tanpa membuka catatan.
- [ ] Sudah membuktikan sendiri (dengan `Ctrl+Klik` di VS Code, atau
      membaca manual) bahwa `create()` di `app.py` TIDAK menulis SQL
      sendiri — ia memanggil `services/`.
- [ ] Diagram versi tanganmu sendiri (Langkah 5) sudah terisi nama
      file & function yang benar.

# Hint

- `Ctrl+Klik` (Windows/Linux) atau `Cmd+Klik` (Mac) pada nama sebuah
  function di VS Code langsung membawamu ke definisinya — cara
  tercepat "melompat" antar lapisan tanpa scroll manual.
- Kalau bingung fungsi mana yang "dipanggil dari mana", cari
  (`Ctrl+Shift+F`) nama function itu di seluruh project — semua
  tempat yang memanggilnya akan muncul sekaligus.
- Restoran adalah analogi yang dipakai modul: Browser = pelanggan,
  Route = pelayan (terima pesanan, tidak masak), Service = koki
  kepala (putuskan resep/aturan), Repository = orang gudang (satu-
  satunya yang buka-tutup kulkas/database).

# Hasil yang Diharapkan

Kamu bisa menjelaskan ke orang lain — TANPA melihat kode — alur
lengkap "user klik Save" sampai "data tersimpan & user lihat hasilnya"
dalam satu tarikan napas, sambil menyebut nama tiap lapisan dengan
benar.

# Refleksi

1. Kenapa response (data naik) HARUS lewat jalur yang sama dengan
   request (data turun), bukan jalan pintas? Apa yang rusak kalau,
   misalnya, `templates/` mencoba mengambil data langsung dari
   `database/` tanpa lewat `Route` dan `Service`?
2. Diagram ini sama untuk SEMUA fitur (Add, Edit, Delete, Search).
   Bagian mana dari diagram yang berbeda-beda tiap fitur, dan bagian
   mana yang selalu identik?
