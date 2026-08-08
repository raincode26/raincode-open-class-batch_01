# 14 · Buggy

# Tujuan

Mempraktikkan langsung 6 error umum Flask + SQLite dari `13-debugging`
— kali ini bukan cuma membaca tabel referensinya, tapi memperbaiki
aplikasi yang benar-benar rusak dengan tanganmu sendiri.

# Yang Dipelajari

| Folder | Bug | Lapisan |
|---|---|---|
| `bug-01-route-salah` | Alamat form ≠ alamat route | Route |
| `bug-02-template-not-found` | Nama file HTML salah ketik | Template |
| `bug-03-query-typo` | Nama kolom SQL salah ketik | Repository/Query |
| `bug-04-lupa-commit` | Data "tersimpan" tapi hilang lagi | Database |
| `bug-05-request-form-typo` | `name` HTML ≠ `request.form[...]` | Request |
| `bug-06-variable-none` | Data tak ditemukan tapi tak dicek dulu | Python/Logic |

# File Yang Diubah

Setiap folder `bug-0X-...` adalah aplikasi Flask yang BISA dijalankan
(`python app.py`), tapi tampilan atau perilakunya tidak sesuai
harapan. Baca `README.md` di masing-masing folder untuk tahu gejala
& apa yang seharusnya terjadi, lalu perbaiki file yang bersangkutan.

# Langkah Pengerjaan

Untuk setiap bug:
1. Jalankan `python app.py`, coba alurnya, amati gejalanya.
2. Baca pesan error di terminal DAN/ATAU browser.
3. Pakai jurus 4 langkah dari `13-debugging`: baca error dari bawah
   → tentukan lapisan mana → selipkan `print()` kalau perlu →
   perbaiki SATU hal, coba lagi.

# Checklist

- [ ] `bug-01-route-salah` — sudah diperbaiki.
- [ ] `bug-02-template-not-found` — sudah diperbaiki.
- [ ] `bug-03-query-typo` — sudah diperbaiki.
- [ ] `bug-04-lupa-commit` — sudah diperbaiki.
- [ ] `bug-05-request-form-typo` — sudah diperbaiki.
- [ ] `bug-06-variable-none` — sudah diperbaiki.

# Hint

- Jangan menebak-nebak dulu — jalankan, baca errornya, baru perbaiki.
- Bandingkan nama (route, kolom, field form) di berbagai file yang
  saling terhubung — bug paling umum adalah dua nama yang HAMPIR
  sama.

# Hasil Akhir

Enam kebiasaan debugging dasar yang langsung berguna di project
manapun setelah kelas ini selesai — bukan cuma di Expense Tracker.
