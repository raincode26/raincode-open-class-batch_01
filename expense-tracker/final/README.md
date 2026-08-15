# Expense Tracker — Final

Aplikasi web sederhana untuk mencatat pengeluaran. Project ini memakai **Python**, **Flask**, dan **MySQL**, serta menyediakan fitur tambah, lihat, cari, filter, urutkan, edit, hapus, dan ringkasan pengeluaran.

README ini ditujukan untuk peserta yang baru pertama kali menjalankan project Flask dan MySQL.

## Gambaran alur aplikasi

```text
Browser
  → app.py                         menerima request dan memilih halaman
  → services/expense_service.py    validasi data dan menyiapkan SQL
  → database/db.py                 membuka koneksi dan menjalankan SQL
  → MySQL                          menyimpan atau membaca data
  → templates/                     mengubah data menjadi halaman HTML
  → Browser
```

## Prasyarat

Pastikan komputer sudah memiliki:

- Python 3.10 atau lebih baru;
- `pip` (biasanya ikut terpasang bersama Python);
- MySQL Server yang sedang berjalan;
- MySQL Workbench atau MySQL command-line client untuk membuat database;
- terminal PowerShell, Command Prompt, Bash, atau terminal bawaan VS Code.

Cek Python dan pip:

```bash
python --version
python -m pip --version
```

Jika perintah `python` tidak ditemukan di Windows, coba gunakan `py` sebagai pengganti `python` pada semua perintah di bawah.

## Menjalankan aplikasi langkah demi langkah

Semua perintah berikut dijalankan dari root repository ini.

### 1. Masuk ke folder aplikasi final

```bash
cd expense-tracker/final
```

Pastikan terminal sekarang berada di folder yang berisi `app.py`, `requirements.txt`, dan `.env.example`.

### 2. Buat virtual environment

Virtual environment membuat dependency project terpisah dari package Python milik sistem.

```bash
python -m venv venv
```

Aktifkan virtual environment sesuai terminal yang digunakan:

```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1
```

```bat
:: Windows Command Prompt
venv\Scripts\activate.bat
```

```bash
# macOS / Linux
source venv/bin/activate
```

Jika aktif, biasanya nama `(venv)` muncul di awal baris terminal.

> Jika PowerShell menolak script aktivasi, jalankan `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, lalu ulangi perintah aktivasi. Pengaturan ini hanya berlaku untuk terminal yang sedang dibuka.

### 3. Install dependency

```bash
python -m pip install -r requirements.txt
```

Dependency utama project:

- `Flask`: web framework;
- `python-dotenv`: membaca konfigurasi dari `.env`;
- `mysql-connector-python`: menghubungkan Python dengan MySQL.

### 4. Buat database dan user MySQL

Pastikan MySQL Server sudah aktif. Buka MySQL Workbench, masuk menggunakan akun administrator, lalu jalankan SQL berikut:

```sql
CREATE DATABASE expense_tracker
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

CREATE USER 'expense_app'@'127.0.0.1'
IDENTIFIED BY 'change-this-local-password';

GRANT SELECT, INSERT, UPDATE, DELETE, CREATE
ON expense_tracker.* TO 'expense_app'@'127.0.0.1';
```

Ganti `change-this-local-password` dengan password lokal yang mudah diingat untuk latihan. Database harus dibuat manual, tetapi tabel `expenses` akan dibuat otomatis oleh `init_db()` saat aplikasi dimulai.

Jika database atau user tersebut sudah pernah dibuat, tidak perlu menjalankan `CREATE` lagi. Cukup pastikan nama database, user, dan password sama dengan isi `.env`.

### 5. Buat dan isi file `.env`

Salin template konfigurasi:

```powershell
# Windows PowerShell
Copy-Item .env.example .env
```

```bat
:: Windows Command Prompt
copy .env.example .env
```

```bash
# macOS / Linux
cp .env.example .env
```

Buka `.env`, lalu sesuaikan nilainya. Contoh:

```dotenv
APP_DEBUG=True
SECRET_KEY=ganti-dengan-string-acak

DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=expense_app
DB_PASSWORD=change-this-local-password
DB_NAME=expense_tracker

RECENT_EXPENSES_LIMIT=5
```

Arti setiap konfigurasi:

| Variabel | Fungsi | Contoh lokal |
|---|---|---|
| `APP_DEBUG` | Mengaktifkan debug dan auto-reload Flask | `True` untuk belajar |
| `SECRET_KEY` | Mengamankan session dan flash message Flask | string acak, jangan dibagikan |
| `DB_HOST` | Alamat MySQL Server | `127.0.0.1` |
| `DB_PORT` | Port MySQL | `3306` |
| `DB_USER` | User aplikasi yang dibuat pada langkah 4 | `expense_app` |
| `DB_PASSWORD` | Password user MySQL tersebut | harus sama dengan SQL |
| `DB_NAME` | Nama database | `expense_tracker` |
| `RECENT_EXPENSES_LIMIT` | Jumlah transaksi terbaru di dashboard | `5` |

Untuk membuat `SECRET_KEY` acak:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Jangan commit `.env` karena file ini dapat berisi password. Project hanya membagikan `.env.example` sebagai template.

### 6. Jalankan aplikasi

Pastikan terminal masih berada di `expense-tracker/final`, virtual environment aktif, dan MySQL Server berjalan:

```bash
python app.py
```

Jika berhasil, terminal menampilkan alamat seperti:

```text
Running on http://127.0.0.1:5000
```

Buka [http://127.0.0.1:5000](http://127.0.0.1:5000) di browser. Hentikan server dengan `Ctrl+C`.

### 7. Uji fitur utama

Lakukan pengecekan singkat berikut:

1. Buka **Add Expense**, isi form, lalu simpan.
2. Pastikan data muncul di halaman **Expenses**.
3. Coba search, filter kategori, dan sorting.
4. Edit data yang baru dibuat.
5. Buka **Summary** dan lihat totalnya berubah.
6. Hapus data dan konfirmasi bahwa data sudah hilang.

## Troubleshooting

### `Access denied for user 'expense_app'`

User atau password MySQL di `.env` tidak cocok. Periksa `DB_USER`, `DB_PASSWORD`, dan host user yang dibuat pada langkah 4.

### `Unknown database 'expense_tracker'`

Database belum dibuat atau `DB_NAME` salah. Jalankan bagian `CREATE DATABASE` pada langkah 4.

### `Can't connect to MySQL server`

Pastikan service MySQL sedang berjalan serta nilai `DB_HOST` dan `DB_PORT` benar. Port default MySQL adalah `3306`.

### `ModuleNotFoundError`

Aktifkan virtual environment lalu ulangi:

```bash
python -m pip install -r requirements.txt
```

### Port `5000` sudah dipakai

Hentikan aplikasi lain yang memakai port tersebut. Untuk percobaan lokal, port juga dapat diganti pada baris terakhir `app.py`, misalnya `app.run(debug=config.DEBUG, port=5001)`, lalu buka `http://127.0.0.1:5001`.

### Perubahan `.env` belum terbaca

Hentikan server dengan `Ctrl+C`, lalu jalankan kembali `python app.py`. Pastikan aplikasi dijalankan dari folder `expense-tracker/final`.

## Struktur folder penting

```text
final/
├── app.py                         route Flask dan entry point aplikasi
├── config.py                      membaca nilai dari .env
├── requirements.txt              daftar package Python
├── .env.example                  contoh konfigurasi
├── database/
│   └── db.py                      koneksi, execute, commit/rollback, schema
├── services/
│   └── expense_service.py         validasi, query SQL, dan format data
├── templates/                     halaman HTML dengan Jinja
│   ├── base.html                  layout utama
│   ├── index.html                 dashboard
│   ├── expenses.html              daftar, search, filter, dan sorting
│   ├── create.html                form tambah
│   ├── edit.html                  form edit
│   └── summary.html               ringkasan per kategori
└── static/
    ├── css/style.css              tampilan aplikasi
    └── js/app.js                  interaksi browser
```

Versi final ini sengaja tidak memakai layer model dan repository terpisah. Hasil MySQL berupa dictionary dan query fitur diletakkan langsung di service agar alurnya mudah diikuti oleh pemula.

## Cara membaca kode secara singkat

Jangan membaca seluruh file dari atas sampai bawah sekaligus. Pilih satu aksi pengguna, lalu ikuti aliran datanya.

### Urutan baca yang disarankan

1. Buka `app.py` untuk melihat URL dan function route.
2. Cari function service yang dipanggil route di `services/expense_service.py`.
3. Lihat validasi, query, dan parameter yang dipakai.
4. Buka `database/db.py` untuk melihat bagaimana query dieksekusi.
5. Kembali ke route, lalu lihat template yang dikirim melalui `render_template()`.
6. Buka file di `templates/` untuk melihat bagaimana data ditampilkan.

Peta route utama:

| Aksi di browser | Method dan URL | Route di `app.py` | Service utama | Template/hasil |
|---|---|---|---|---|
| Buka dashboard | `GET /` | `index()` | summary, recent, category totals | `index.html` |
| Lihat/cari data | `GET /expenses` | `expenses()` | `get_expenses()` | `expenses.html` |
| Buka form tambah | `GET /create` | `create()` | `get_categories()` | `create.html` |
| Simpan data | `POST /create` | `create()` | `create_expense()` | redirect ke expenses |
| Buka form edit | `GET /edit/<id>` | `edit()` | `get_expense_by_id()` | `edit.html` |
| Simpan edit | `POST /edit/<id>` | `edit()` | `update_expense()` | redirect ke expenses |
| Hapus data | `POST /delete/<id>` | `delete()` | `delete_expense()` | redirect ke expenses |
| Lihat ringkasan | `GET /summary` | `summary()` | summary dan category totals | `summary.html` |

### Contoh: ikuti proses CREATE

```text
templates/create.html
  → form mengirim POST /create
  → create() di app.py membaca request.form
  → read_expense_form() membuat dictionary
  → service.create_expense(form_data)
  → validate_expense() memeriksa input
  → db.execute(INSERT, params)
  → MySQL menyimpan row dan melakukan commit
  → route melakukan redirect ke /expenses
```

Query dan value dipisahkan:

```python
query = """
    INSERT INTO expenses (title, amount, category, notes)
    VALUES (%s, %s, %s, %s)
"""
params = (data["title"], data["amount"], data["category"], data["notes"])
db.execute(query, params)
```

Placeholder `%s` membuat input diperlakukan sebagai value, bukan syntax SQL. Jangan menggabungkan input user ke SQL menggunakan f-string. Khusus nama kolom sorting, service memakai `allowed_sorts` karena nama kolom tidak dapat dijadikan parameter `%s`.

### Cara memahami `db.execute()`

Untuk query `SELECT`:

```python
row = db.execute(query, params, fetch="one")
rows = db.execute(query, params, fetch="all")
```

Untuk `INSERT`, `UPDATE`, atau `DELETE`:

```python
result = db.execute(query, params)
result["lastrowid"]  # ID hasil INSERT
result["rowcount"]   # jumlah row yang berubah
```

Helper tersebut selalu mengikuti pola:

```text
buka koneksi → buat dictionary cursor → execute
→ fetch untuk SELECT atau commit untuk perubahan data
→ rollback jika terjadi error → tutup cursor dan koneksi
```

## Lokasi query setiap fitur

Semua query fitur berada di `services/expense_service.py`.

| Fitur | Function | SQL utama |
|---|---|---|
| Tambah | `create_expense()` | `INSERT` |
| Daftar/search/filter/sort | `get_expenses()` | `SELECT` |
| Ambil satu data | `get_expense_by_id()` | `SELECT ... WHERE id` |
| Edit | `update_expense()` | `UPDATE ... WHERE id` |
| Hapus | `delete_expense()` | `DELETE ... WHERE id` |
| Transaksi terbaru | `get_recent_expenses()` | `ORDER BY ... LIMIT` |
| Ringkasan | `get_summary()` | `SUM`, `COUNT`, `AVG` |
| Total kategori | `get_category_totals()` | `GROUP BY` |

## Schema database

Schema dibuat otomatis oleh `init_db()` di `database/db.py`:

```sql
CREATE TABLE expenses (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    category VARCHAR(100) NOT NULL DEFAULT 'Other',
    notes TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
```

## Catatan penggunaan

- Aplikasi ini cocok untuk belajar dan development lokal.
- `APP_DEBUG=True` jangan digunakan untuk production.
- Uang disimpan sebagai `DECIMAL`, bukan `float`, untuk menghindari kesalahan pembulatan umum.
- Operasi create, update, dan delete menggunakan method `POST`.
- Project ini belum memiliki login, multi-user, CSRF protection, migration, atau test otomatis.

Cara belajar paling efektif: pilih satu tombol di browser, temukan route-nya, ikuti function service dan query-nya, lalu lihat bagaimana hasilnya kembali ke template.
