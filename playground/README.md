# Playground — Demo Data Sementara

File utama: `initiate_data.py`.

Demo ini dipakai sebelum memperkenalkan MySQL. Tujuannya bukan membuat aplikasi
sempurna, tetapi membuat peserta melihat bahwa data dapat diolah di memory dan
akan hilang ketika program berhenti.

## Cara menjalankan

Dari root repository:

```powershell
python playground/initiate_data.py
```

Program berhenti pada setiap tahap. Gunakan jeda tersebut untuk meminta peserta
menebak output dan menjelaskan lokasi data.

Jika ingin menjalankan seluruh tahap tanpa jeda, ubah:

```python
MODE_INTERAKTIF = False
```

## Contoh CRUD terpisah

Setelah demo utama, jalankan empat file berikut secara berurutan:

| File | Operation | Konsep utama |
|---|---|---|
| `01_tambah_data.py` | CREATE | Membuat dictionary lalu `append()` ke list |
| `02_get_data.py` | READ | Loop semua data dan mencari satu ID |
| `03_update_data.py` | UPDATE | Mencari ID lalu mengubah value dictionary |
| `04_hapus_data.py` | DELETE | Membuat list baru tanpa ID target |

```powershell
python playground/01_tambah_data.py
python playground/02_get_data.py
python playground/03_update_data.py
python playground/04_hapus_data.py
```

Semua file memiliki data awalnya sendiri. Perubahan pada satu file tidak masuk ke
file lain dan kembali ke kondisi awal saat program dijalankan lagi. Ini menjadi
bukti bahwa data masih berada di memory, belum di database.

## Alur demonstrasi 12–15 menit

| Tahap | Yang dicontohkan | Pertanyaan pengajar |
|---:|---|---|
| 0 | List kosong saat program mulai | “Saat ini datanya ada berapa?” |
| 1 | Variable `nama` dan `total` | “Satu variable menyimpan berapa nilai?” |
| 2 | Dua list terpisah | “Apa yang terjadi jika index kedua list tidak cocok?” |
| 3 | Satu dictionary | “Apa fungsi key `nama` dan `total`?” |
| 4 | List of dictionaries | “List-nya apa? Item di dalamnya apa?” |
| 5 | UPDATE berdasarkan ID | “Mengapa mencari ID, bukan selalu index 0?” |
| 6 | DELETE berdasarkan ID | “Data mana yang hilang dari list?” |
| 7 | Restart program | “Mengapa data kembali ke awal?” |

## Hal yang dapat dicontohkan langsung

### 1. Ubah satu nilai

Ubah `Kopi Susu` menjadi `Es Teh`, jalankan kembali, lalu tunjukkan bahwa output
mengikuti isi variable.

### 2. Rusakkan hubungan dua list

Tambahkan nama baru tanpa menambah total:

```python
daftar_nama.append("Boba")
```

Tanyakan total mana yang menjadi milik Boba. Ini menjadi alasan natural untuk
memakai dictionary.

### 3. Tambahkan field

Tambahkan kategori pada dictionary:

```python
transaction["kategori"] = "Makanan"
```

Tunjukkan bahwa satu record dapat berkembang tanpa membuat list baru untuk setiap
field.

### 4. Tambahkan transaksi

Minta peserta menulis satu `append()` untuk data pilihannya sendiri. Setelah itu,
jalankan `tampilkan_transaksi(transactions)`.

### 5. Salah target UPDATE

Ubah `id_yang_diubah` menjadi ID yang tidak tersedia. Tunjukkan bahwa tidak ada
data berubah. Hubungkan dengan konsep `WHERE id = ...` yang akan muncul di SQL.

### 6. Buktikan temporary

Setelah table akhir terlihat:

1. tanyakan apakah data sudah permanen;
2. tutup program;
3. jalankan lagi;
4. tunjukkan `transactions = []` pada Tahap 0;
5. baru perkenalkan database sebagai tempat penyimpanan persistent.

## Kalimat transisi ke database

> Kita sudah bisa mengontrol data dengan Python: menambah, membaca, mengubah, dan
> menghapus. Masalahnya bukan kemampuan mengolah data, tetapi kemampuan
> mengingatnya setelah program berhenti. Di situlah database mulai dibutuhkan.

## Hindari pada demo awal

- Jangan langsung membuka Flask.
- Jangan langsung menulis query SQL.
- Jangan menjelaskan class atau arsitektur project.
- Jangan mengatakan table terminal berarti database.
- Jangan melewatkan restart program; itu adalah aha moment utama.
