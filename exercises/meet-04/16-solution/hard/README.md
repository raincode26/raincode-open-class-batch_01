# Solution · Challenge Hard

# Tujuan Belajar

Melihat satu cara valid mencegah title duplikat, termasuk menangani
kasus "edit tanpa ubah title".

# Penjelasan

`repository.py` menambahkan `title_exists(title, exclude_id=None)` —
query `SELECT id FROM expenses WHERE LOWER(title) = LOWER(?)`, dengan
tambahan `AND id != ?` kalau `exclude_id` diisi. `service.py`
memanggil ini di akhir `_validate`, dan `edit_expense` mengoper
`expense_id`-nya sendiri sebagai `exclude_id` supaya tidak dianggap
duplikat dengan dirinya sendiri.

# Diagram

```
add_expense(data)
   → _validate(data, exclude_id=None)
      → title_exists(title, exclude_id=None)
         → True kalau ADA expense manapun dengan title sama

edit_expense(id=3, data)
   → _validate(data, exclude_id=3)
      → title_exists(title, exclude_id=3)
         → True kalau ADA expense LAIN (id != 3) dengan title sama
```

# Langkah Pengerjaan

1. Jalankan `python app.py`. Tambah "Kopi pagi" dua kali — yang
   kedua harus ditolak.
2. Edit expense "Kopi pagi" tanpa mengubah title-nya (cuma ubah
   amount) — harus berhasil.
3. Bandingkan dengan hasil kerjamu di `15-challenge/hard`.

# File Yang Diubah

- `repository.py`
- `service.py`

# Checklist

- [ ] Title duplikat pada Create ditolak.
- [ ] Edit tanpa ubah title tetap berhasil (tidak dianggap duplikat).
- [ ] Edit YANG mengubah title jadi title yang sudah dipakai expense
      lain tetap ditolak.

# Hint

Kalau `exclude_id` di punyamu diberi nama parameter lain (misalnya
`current_id`) tapi logikanya sama — itu tetap valid, nama parameter
bukan bagian dari kontrak fungsionalnya.

# Hasil yang Diharapkan

Validasi title duplikat yang bekerja identik secara fungsi dengan
punyamu di `15-challenge/hard`.

# Refleksi

`title_exists` dipanggil dari `service.py`, tapi query SQL-nya
ditulis di `repository.py`. Kenapa `service.py` TIDAK boleh menulis
query `SELECT ... WHERE LOWER(title) = ...` itu sendiri, walau
sebenarnya "cuma satu baris SQL saja"?
