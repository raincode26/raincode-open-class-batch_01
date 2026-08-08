# 04 · Form & Request

# Tujuan

Menerima data yang diisi pengunjung lewat HTML form, dan memahami
kenapa data itu masih hilang tiap server restart — motivasi nyata
untuk butuh database di langkah berikutnya.

# Yang Dipelajari

- `request.form['nama-field']` — mengambil isi satu field form,
  dicocokkan lewat atribut `name` di HTML.
- `methods=['POST']` — route hanya menerima kiriman form, bukan
  kunjungan biasa lewat alamat URL.
- `redirect('/')` — memindahkan user kembali ke halaman lain setelah
  aksi selesai, supaya form tidak "terkirim ulang" kalau di-refresh.

# Penjelasan Konsep

Form HTML tidak bisa menyimpan data — ia hanya mengumpulkan lalu
mengirim. Yang mengubah ketikan user jadi data yang benar-benar
tersimpan adalah Python di baliknya, dipicu oleh `action` (ke mana)
dan `method` (bagaimana) pada tag `<form>`. Di latihan ini, Python
memang MENERIMA & MENYIMPAN data — tapi masih ke `list` di memori,
bukan file permanen. Coba tambah satu transaksi, lalu restart server
(`Ctrl+C`, jalankan lagi `python app.py`) — datamu akan hilang. Ini
"masalah" yang sengaja kita rasakan sebelum SQLite menyelesaikannya.

# Langkah Pengerjaan

1. Baca `templates/index.html` — form-nya sudah lengkap.
2. Selesaikan `TODO 1` di `app.py`: buat route `/tambah`.
3. Jalankan `python app.py`, isi form, klik Simpan.
4. Perhatikan: transaksi baru langsung muncul di daftar.
5. (Opsional, untuk merasakan masalahnya) Matikan server, nyalakan
   lagi, refresh halaman — transaksi barumu hilang.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] Route `/tambah` menerima `methods=['POST']`.
- [ ] `request.form['nama']` dan `request.form['nominal']` berhasil
      diambil.
- [ ] Data baru masuk ke list `transaksi` lewat `.append(...)`.
- [ ] Setelah submit, browser kembali ke `/` dan transaksi baru
      langsung terlihat di daftar.

# Hint

- `name="nama"` di HTML dan `request.form['nama']` di Python harus
  dieja SAMA PERSIS — ini pasangan kunci-nilai yang menghubungkan
  keduanya.
- Kalau lupa `methods=['POST']` pada route `/tambah`, Flask akan
  menolak kiriman form dengan error `405 Method Not Allowed`.
- `redirect('/')` HARUS di-`return`, bukan cuma dipanggil begitu
  saja — sama seperti aturan `return` pada function biasa.

# Hasil Akhir

Form yang benar-benar menerima & menampilkan input pengunjung —
tapi masih "berumur pendek". Rasakan dulu keterbatasannya, supaya
manfaat SQLite di langkah berikutnya terasa nyata.

# Kesalahan Yang Sering Terjadi

- **`request.form.get()` vs `request.form[]`** — `request.form['x']`
  akan melempar error `400 Bad Request` kalau field `x` tidak ada
  sama sekali di form (misalnya salah ketik `name`-nya). Ini
  memang disengaja di sini supaya error-nya terlihat jelas.
- **Lupa `redirect`, langsung `return "OK"`** → data tersimpan, tapi
  user terjebak di halaman kosong, bukan kembali ke daftar.
- **Route `/tambah` tanpa `methods=['POST']`** → error
  `405 Method Not Allowed` saat form di-submit.
- **Field `name` di HTML tidak cocok dengan `request.form[...]`
  di Python** → `400 Bad Request` atau `KeyError`.
