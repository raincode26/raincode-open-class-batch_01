# Bug 2 · Template Tidak Ditemukan

# Tujuan

Melatih mata mencocokkan nama file yang diminta `render_template()`
dengan nama file yang benar-benar ada di folder `templates/`.

# Yang Dipelajari

Flask mencari file HTML lewat nama yang PERSIS sama, termasuk huruf
besar/kecil dan ejaannya, di dalam folder `templates/`.

# Penjelasan Konsep

`TemplateNotFound` bukan berarti foldernya salah atau Flask-nya
rusak — artinya nama file yang diminta di `render_template("...")`
tidak ada (atau salah ketik) di dalam `templates/`.

# Langkah Pengerjaan

1. Jalankan `python app.py`, buka `localhost:5000`.
2. Baca pesan error yang muncul — perhatikan nama file yang
   disebutkan sebagai "tidak ditemukan".
3. Buka folder `templates/`, lihat nama file yang sebenarnya ada.

# File Yang Diubah

- Perbaiki `app.py`, samakan nama file di `render_template(...)`
  dengan nama file yang sebenarnya ada di `templates/`.

# Checklist

- [ ] `render_template(...)` memanggil nama file yang benar-benar
      ada.
- [ ] Halaman `/` menampilkan daftar transaksi tanpa error.

# Hint

- Pesan error Flask untuk kasus ini sangat jelas — biasanya langsung
  menyebutkan nama file yang dicari beserta folder mana yang sudah
  diperiksa.
- Jangan ganti nama filenya di folder `templates/` — cukup ubah
  nama yang dipanggil di `render_template(...)` supaya cocok.

# Hasil Akhir

Halaman yang berhasil menampilkan HTML-nya, bukan pesan error.

# Kesalahan Yang Sering Terjadi

Kesalahan ini paling sering terjadi setelah rename file HTML (misal
dari `daftar.html` ke `index.html`) tapi lupa mengganti nama yang
dipanggil di `render_template(...)`.
