# 09 · Update Expense

# Tujuan

Mengubah data yang SUDAH ADA — huruf **U** dari CRUD — sambil
mengenal pola satu route yang melayani dua method sekaligus (GET
untuk menampilkan form, POST untuk memprosesnya).

# Yang Dipelajari

- `UPDATE transactions SET nama = ?, nominal = ? WHERE id = ?` —
  pola SQL untuk mengubah baris yang sudah ada.
- Satu route, dua method: `methods=['GET', 'POST']`, dicabang
  dengan `if request.method == 'POST':`.
- Form yang TERISI data lama (`value="{{ item.nama }}"`) — beda dari
  form tambah yang selalu kosong.

# Penjelasan Konsep

**Aturan emas: `WHERE`.** `UPDATE transactions SET nominal = 30000`
TANPA `WHERE id = ?` akan mengubah nominal SEMUA baris jadi 30000 —
bukan cuma satu. `id` di URL (`/edit/3`) menunjuk PERSIS baris mana
yang dimaksud. Ini kenapa `08-read-expense` (belajar `WHERE id = ?`)
harus datang sebelum Update: kamu butuh skill itu untuk mengambil
data lama SEBELUM menampilkan form edit-nya.

# Langkah Pengerjaan

1. Baca `templates/edit.html` — perhatikan atribut `value="..."`
   yang mengisi form dengan data lama.
2. Selesaikan `TODO 1` di `app.py` — satu function `edit(id)` untuk
   dua method (GET & POST).
3. Jalankan `python app.py`, klik "Edit" pada salah satu transaksi.
4. Ubah nilainya, klik "Simpan Perubahan", lihat daftar ter-update.

# File Yang Diubah

- `app.py`

# Checklist

- [ ] Route `/edit/<int:id>` menerima `methods=['GET', 'POST']`.
- [ ] Saat diakses via GET (klik link "Edit"), form tampil TERISI
      data lama.
- [ ] Saat form disubmit (POST), `UPDATE` memakai `WHERE id = ?`.
- [ ] Setelah simpan, daftar di `/` menunjukkan nilai yang sudah
      diubah — HANYA untuk transaksi itu, yang lain tidak ikut
      berubah.

# Hint

- Urutan `?` di query HARUS cocok dengan urutan nilai di tuple:
  `SET nama = ?, nominal = ? WHERE id = ?` berarti tuple-nya
  `(nama, nominal, id)` — id di PALING AKHIR, sesuai urutan `?`-nya.
- `if request.method == 'POST':` adalah cara mengecek "apakah ini
  kiriman form atau sekadar kunjungan biasa?" — persis seperti
  konsep if/else dari Pertemuan 1.
- Kalau form edit selalu tampil kosong (bukan terisi), cek: apakah
  cabang GET benar-benar mengambil data lama lewat `fetchone()`
  sebelum me-render `edit.html`?

# Hasil Akhir

Kemampuan mengedit data yang sudah tersimpan — dua dari empat huruf
CRUD selesai. Satu lagi: Delete, di folder berikutnya.

# Kesalahan Yang Sering Terjadi

- **Lupa `WHERE id = ?` di `UPDATE`** → SEMUA baris ikut berubah
  nilainya. Ini bug paling berbahaya di seluruh modul — selalu
  double-check sebelum menjalankan `UPDATE`.
- **Urutan `?` tidak cocok dengan urutan tuple** → data tersimpan,
  tapi ke kolom yang salah (misal nominal malah masuk ke kolom nama).
- **Form edit tidak diberi `value="{{ item.nama }}"`** → form
  tampil KOSONG padahal seharusnya terisi data lama, memaksa user
  mengetik ulang semuanya dari nol.
- **`action` di form edit mengarah ke alamat yang salah** (misalnya
  tetap `/tambah`) → data malah membuat baris BARU alih-alih
  mengubah yang lama.
