# Expense Tracker

Aplikasi pencatat pengeluaran menggunakan Flask dan MySQL.

| Folder | Tujuan |
|---|---|
| [starter](starter) | Skeleton latihan yang perlu dilengkapi peserta |
| [final](final) | Implementasi lengkap dengan alur sederhana yang dapat dibandingkan dengan starter |

Kedua versi memakai model mental yang sama:

```text
Route Flask → Service + query → db.execute() → MySQL
```

Query sengaja diletakkan di service agar peserta dapat memasangkan satu fitur
dengan SQL yang dijalankannya. `database/db.py` menjadi satu-satunya tempat yang
mengurus connection, cursor, fetch, commit, rollback, dan close.

Urutan belajar:

1. Pahami `database/db.py`.
2. Cari query CREATE/READ/UPDATE/DELETE di service.
3. Ikuti route yang memanggil function service tersebut.
4. Jalankan aplikasi dan cocokkan aksi di browser dengan query.

Panduan lebih lengkap tersedia di [`../docs`](../docs).

RainCode Open Class · Understand before memorizing.
