# 01 · Flask Hello World

# Tujuan

Menyalakan aplikasi web pertamamu dan memahami bahwa Flask, sekompleks
apa pun nanti, selalu mulai dari kerangka yang sama sederhananya.

# Yang Dipelajari

- Flask = **jembatan** antara HTML dan Python. Tanpanya, form tak tahu
  ke mana harus mengirim data, dan Python tak tahu di mana hasilnya
  harus muncul.
- `Flask(__name__)` — menyalakan aplikasi.
- `@app.route('/')` — decorator, "penempel label" yang bilang
  "function di bawah saya bertugas melayani alamat `/`".
- `app.run(debug=True)` — menghidupkan server lokal di `localhost:5000`.

# Penjelasan Konsep

Bayangkan aplikasi web seperti restoran: **Frontend** (HTML) adalah
pelanggan yang memesan, **Database** adalah gudang bahan, dan
**Flask** adalah pelayan yang mengantar pesanan ke dapur (Python) lalu
membawa hasilnya kembali. Tanpa pelayan ini, HTML dan Python "tidak
saling mengenal" — form dikirim ke mana, Python tak tahu; hasil Python
muncul di mana, HTML juga tak tahu.

# Langkah Pengerjaan

1. Pastikan Flask sudah terpasang: `pip install flask`.
2. Buka `app.py`, ikuti `TODO 1` sampai `TODO 4` berurutan dari atas
   ke bawah — urutannya penting (import dulu, baru nyalakan aplikasi,
   baru daftarkan route, baru jalankan server).
3. Jalankan: `python app.py`.
4. Buka `http://localhost:5000` di browser.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] `from flask import Flask` sudah ditulis di baris paling atas.
- [ ] `app = Flask(__name__)` sudah dibuat.
- [ ] `@app.route('/')` terpasang tepat di atas function `home()`.
- [ ] Function `home()` me-return sebuah teks (string).
- [ ] `app.run(debug=True)` ada di baris PALING BAWAH file.
- [ ] Browser menampilkan teks sambutanmu saat membuka `localhost:5000`.

# Hint

- Urutan menulis penting: Python membaca file dari atas ke bawah, jadi
  `app = Flask(__name__)` harus ada SEBELUM `@app.route(...)` dipakai.
- Terminal menunjukkan `* Running on http://127.0.0.1:5000` kalau
  server berhasil menyala. Kalau tidak muncul apa-apa atau langsung
  error, baca pesan error-nya dulu sebelum menebak.
- Berhenti server dengan `Ctrl+C` di terminal, bukan menutup jendela
  terminalnya langsung.

# Hasil Akhir

Satu halaman web sederhana yang menyapamu di browser — kerangka yang
sama persis akan dipakai lagi untuk Expense Tracker, hanya ditambah
route, form, dan database.

# Kesalahan Yang Sering Terjadi

- **Lupa `app.run(debug=True)`** → terminal langsung selesai tanpa
  menyalakan server apa pun.
- **`app.run()` diletakkan sebelum route didaftarkan** → route yang
  didaftarkan setelah `app.run()` tidak akan pernah terbaca, karena
  `app.run()` "mengunci" & menjalankan server duluan.
- **Lupa `return` di dalam function** → halaman tampil kosong, bukan
  error. Function yang tidak me-return apa pun otomatis dianggap
  me-return kosong.
- **Server sudah jalan di terminal lain** → muncul error
  `Address already in use`. Tutup dulu server sebelumnya dengan
  `Ctrl+C`.
