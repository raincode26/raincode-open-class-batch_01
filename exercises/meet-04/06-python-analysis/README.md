# 06 · Python Analysis

# Tujuan Belajar

Membaca `app.py` di `projects/expense-tracker/final/` baris per baris —
memahami tiap `import`, tiap pemanggilan setup, dan pola yang berulang
di SETIAP route.

# Penjelasan

`app.py` (444 baris) terlihat panjang, tapi sebenarnya cuma 6 route +
2 error handler yang mengikuti pola YANG SAMA berulang-ulang. Kalau
kamu paham SATU route, kamu paham hampir semuanya.

Bagian atas file (sebelum route pertama) isinya setup, dijalankan
SEKALI saat aplikasi start:

```python
from flask import Flask, flash, redirect, render_template, request, url_for
from config import config
from database.db import init_db
from services.expense_service import ExpenseService
from utils.logger import get_logger

logger = get_logger(__name__)
app = Flask(__name__)
app.secret_key = config.SECRET_KEY
init_db()
expense_service = ExpenseService()
logger.info(f"Application started | name={config.APP_NAME} env={config.APP_ENV}")
```

Baca ini seperti resep: "siapkan logger, buat aplikasi Flask, pasang
secret key (dibutuhkan untuk fitur flash message), pastikan tabel
database ada, siapkan satu object `expense_service` yang akan dipakai
SEMUA route di bawahnya."

Pola yang berulang di SETIAP route (Create & Edit khususnya):

```python
try:
    hasil = expense_service.lakukan_sesuatu(data)
    flash("berhasil!")
    return redirect(...)          # sukses → redirect (PRG pattern)
except ValueError as ve:
    flash(str(ve))                # gagal validasi → render ulang FORM
    return render_template(...)   #   dengan pesan error & data yang tadi diketik
except Exception as e:
    logger.error(f"...: {e}")     # gagal SISTEM (bukan input user)
    flash("Terjadi kesalahan.")   #   → pesan generik, jangan bocorkan detail teknis
    return redirect(...)
```

Perhatikan: ada DUA jenis `except` berbeda, karena DUA jenis kegagalan
berbeda butuh respons berbeda — `ValueError` (kesalahan INPUT user,
aman ditampilkan pesannya) vs `Exception` umum (kesalahan SISTEM,
pesan detailnya disembunyikan dari user demi keamanan, tapi dicatat ke
log untuk developer).

# Diagram

```
app.py dibaca top-to-bottom sekali saat start:

┌─────────────────────────┐
│ import ...               │  ← 1x saat start
│ setup logger, app, dll   │  ← 1x saat start
│ init_db()                │  ← 1x saat start
└─────────────────────────┘
           │
           ▼  (lalu Flask "tidur", menunggu request)
┌─────────────────────────┐
│ @app.route("/")          │  ← dijalankan SETIAP ADA request ke "/"
│ def index(): ...         │
├─────────────────────────┤
│ @app.route("/expenses")  │  ← dijalankan SETIAP ADA request ke "/expenses"
│ def expenses(): ...      │
├─────────────────────────┤
│         ... (dst)        │
└─────────────────────────┘
```

# Langkah Pengerjaan

1. Buka `app.py`. Baca HANYA baris `import` di paling atas (baris 1
   sampai sekitar baris 10). Untuk tiap `import`, tebak: dari file
   mana asalnya, dan untuk apa dipakai?
2. Baca blok setup (sebelum route pertama). Cari baris `init_db()` —
   ini dipanggil DI LUAR function mana pun, artinya dijalankan sekali
   saat file ini di-import/dijalankan, BUKAN setiap ada request.
3. Buka function `create()` (route `/create`). Hitung: ada berapa
   blok `try/except` di dalamnya? Baca isi tiap blok `except` — apa
   bedanya penanganan `ValueError` dengan `Exception` biasa?
4. Bandingkan `create()` dengan `edit()` — keduanya punya struktur
   `try/except` yang MIRIP. Sebutkan satu perbedaan penting antara
   keduanya (petunjuk: `edit()` perlu mengecek sesuatu SEBELUM masuk
   ke try/except sama sekali).
5. Cari dua function paling bawah: `page_not_found` dan
   `internal_server_error`, yang didekorasi `@app.errorhandler(404)`
   dan `@app.errorhandler(500)`. Baca — kapan Flask memanggil function
   ini secara OTOMATIS (tanpa kamu perlu memanggilnya manual)?

# File Yang Diubah

Tidak ada — folder ini murni membaca.

# Checklist

- [ ] Bisa menjelaskan fungsi 5 baris pertama `app.py` (import +
      setup) dalam bahasamu sendiri, tanpa membuka file lagi.
- [ ] Paham kenapa `init_db()` dipanggil SEKALI di luar function,
      bukan di dalam tiap route.
- [ ] Bisa menjelaskan beda `except ValueError` vs `except Exception`
      di `create()` — kapan masing-masing dipicu, dan kenapa
      responsnya berbeda.

# Hint

- Jangan baca `app.py` dari baris 1 sampai baris 444 secara linear.
  Baca blok setup dulu (± 20 baris), lalu pilih SATU route, baca
  tuntas, baru pindah ke route lain.
- Kalau ada nama yang asing (`flash`, `url_for`) — itu semua fungsi
  bawaan Flask, bukan buatan project ini. Kamu sudah kenal `redirect`
  dan `render_template` dari `meet-03`; `flash` dan `url_for` adalah
  teman baru yang polanya sama: dipanggil, mengembalikan sesuatu yang
  dipakai Flask.
- `except Exception as e:` selalu diletakkan SETELAH `except
  ValueError as ve:` (lebih spesifik dulu, baru yang umum) — kalau
  urutannya dibalik, blok `ValueError` tidak akan pernah tercapai.
  Ini bukan kebetulan; itu aturan Python.

# Hasil yang Diharapkan

Kamu bisa membaca route Flask APA PUN (bukan cuma di project ini) dan
langsung mengenali pola: bagian ambil input → bagian panggil lapisan
lain → bagian tangani sukses/gagal → bagian kirim response.

# Refleksi

1. Kenapa pesan error dari `except ValueError` boleh ditampilkan
   langsung ke user (`flash(str(ve))`), tapi pesan dari `except
   Exception` TIDAK (`flash("Terjadi kesalahan.")` — pesan generik)?
   Apa risikonya kalau keduanya diperlakukan sama?
2. `logger.error(...)` dipanggil di dalam `except Exception`, tapi
   TIDAK dipanggil di dalam `except ValueError`. Menurutmu kenapa?
