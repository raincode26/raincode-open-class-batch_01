# Bug 4 · Import Error

# Tujuan Belajar

Mengenali `ImportError`/`ImportError: cannot import name` — kelas
bug yang mencegah aplikasi START sama sekali, sebelum sempat menerima
satu request pun.

# Penjelasan

`from repository import (a, b, c)` di `service.py` memberi tahu Python
"ambil function bernama a, b, c dari file `repository.py`". Kalau
salah SATU nama itu tidak benar-benar ada di `repository.py` (typo,
atau memang belum pernah dibuat), Python berhenti total saat mencoba
menjalankan baris import itu — TIDAK PEDULI apakah function tersebut
akan dipakai atau tidak.

# Diagram

```
service.py                          repository.py

from repository import (      ✗     def get_total(): ...
    ...,
    get_totals    ← salah ketik            (yang benar-benar ada: get_total,
)                                            TANPA huruf 's' di akhir)
        │
        ▼
ImportError: cannot import name 'get_totals' from 'repository'
   → app.py GAGAL start sama sekali
```

# Langkah Pengerjaan

1. Coba jalankan `python app.py`.
2. Perhatikan: server bahkan TIDAK sempat menampilkan pesan
   "Running on http://127.0.0.1:5000" — ia langsung berhenti dengan
   traceback.
3. Baca baris PALING BAWAH traceback — cari `ImportError`.
4. Buka `service.py`, cari baris `from repository import (...)`.
5. Buka `repository.py`, cari nama function yang BENAR-BENAR ada di
   sana.
6. Samakan.

# File Yang Diubah

- `service.py`

# Checklist

- [ ] Semua nama yang di-import di `service.py` dari `repository.py`
      sekarang cocok dengan nama function yang benar-benar ada.
- [ ] `python app.py` berhasil start, menampilkan
      "Running on http://127.0.0.1:5000".

# Hint

- Bug ini TIDAK BISA dites lewat browser — server-nya belum menyala
  sama sekali. Satu-satunya tempat melihat errornya adalah terminal.
- Jangan ubah nama function di `repository.py` — funcion itu SUDAH
  benar (`get_total`). Yang salah adalah nama yang dipakai untuk
  meng-import-nya di `service.py`.

# Hasil yang Diharapkan

`python app.py` berjalan normal tanpa error apa pun di terminal.

# Refleksi

Kenapa `ImportError` mencegah SELURUH aplikasi start, padahal cuma
SATU function (`get_totals`) yang bermasalah — bukan cuma fitur yang
memakai function itu saja yang gagal?
