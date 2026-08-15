"""Demo live class: memahami data sementara sebelum masuk database.

Jalankan:
    python playground/initiate_data.py

Tekan Enter untuk berpindah tahap. Jangan langsung menunjukkan seluruh file;
buka dan jalankan satu tahap sambil meminta peserta menebak hasilnya.
"""


MODE_INTERAKTIF = True


def lanjutkan():
    """Memberi waktu untuk bertanya sebelum masuk ke tahap berikutnya."""
    if MODE_INTERAKTIF:
        input("\nTekan Enter untuk lanjut...")


def judul(teks):
    print("\n" + "=" * 58)
    print(teks)
    print("=" * 58)


def tampilkan_transaksi(transactions):
    """READ: tampilkan list of dictionaries sebagai table sederhana."""
    print("\nID | Nama                 | Total")
    print("---+----------------------+------------")

    if not transactions:
        print("   | Belum ada transaksi  |")
        return

    for transaction in transactions:
        print(
            f"{transaction['id']:>2} | "
            f"{transaction['nama']:<20} | "
            f"Rp{transaction['total']:>8}"
        )


# ============================================================
# TAHAP 0 - Kondisi awal setiap program dijalankan
# ============================================================
judul("TAHAP 0 - MEMORY DIMULAI DARI KONDISI AWAL")

transactions = []

print("Isi transactions:", transactions)
print("Jumlah data:", len(transactions))
print("Data ini baru hidup ketika program berjalan.")

lanjutkan()


# ============================================================
# TAHAP 1 - Variable menyimpan satu nilai
# ============================================================
judul("TAHAP 1 - SATU NILAI, SATU VARIABLE")

nama = "Kopi Susu"
total = 25000

print("Nama :", nama)
print("Total:", total)

print("\nPertanyaan: kalau transaksi punya kategori dan tanggal,")
print("apakah kita akan terus menambah variable terpisah?")

lanjutkan()


# ============================================================
# TAHAP 2 - Dua list terpisah mudah kehilangan hubungan
# ============================================================
judul("TAHAP 2 - MASALAH DUA LIST TERPISAH")

daftar_nama = ["Kopi Susu", "Makan Siang"]
daftar_total = [25000, 35000]

print("Nama :", daftar_nama)
print("Total:", daftar_total)
print("\nKopi Susu cocok dengan total hanya karena index-nya sama.")
print("Jika salah satu list berubah sendiri, hubungan datanya bisa rusak.")

lanjutkan()


# ============================================================
# TAHAP 3 - Dictionary menyatukan satu record
# ============================================================
judul("TAHAP 3 - SATU TRANSAKSI MENJADI DICTIONARY")

transaction = {
    "id": 1,
    "nama": "Kopi Susu",
    "total": 25000,
}

print("Satu record:", transaction)
print("Nama saja   :", transaction["nama"])
print("Total saja  :", transaction["total"])

lanjutkan()


# ============================================================
# TAHAP 4 - CREATE dan READ di memory
# ============================================================
judul("TAHAP 4 - CREATE DAN READ DI MEMORY")

transactions.append(transaction)
transactions.append({"id": 2, "nama": "Makan Siang", "total": 35000})
transactions.append({"id": 3, "nama": "Transport", "total": 15000})

tampilkan_transaksi(transactions)

print("\nCREATE = append dictionary ke list")
print("READ   = loop seluruh isi list")

lanjutkan()


# ============================================================
# TAHAP 5 - UPDATE berdasarkan ID
# ============================================================
judul("TAHAP 5 - UPDATE DI MEMORY")

id_yang_diubah = 1

for transaction in transactions:
    if transaction["id"] == id_yang_diubah:
        print("Sebelum:", transaction)
        transaction["total"] = 30000
        print("Sesudah:", transaction)
        break

tampilkan_transaksi(transactions)

lanjutkan()


# ============================================================
# TAHAP 6 - DELETE berdasarkan ID
# ============================================================
judul("TAHAP 6 - DELETE DI MEMORY")

id_yang_dihapus = 2
transactions_setelah_delete = []

for transaction in transactions:
    if transaction["id"] != id_yang_dihapus:
        transactions_setelah_delete.append(transaction)

transactions = transactions_setelah_delete

tampilkan_transaksi(transactions)
print("\nID 2 sudah tidak ada di list.")

lanjutkan()


# ============================================================
# TAHAP 7 - Aha moment: belum persistent
# ============================================================
judul("TAHAP 7 - APAKAH DATA INI SUDAH PERMANENT?")

print("Isi akhir memory:")
tampilkan_transaksi(transactions)

print("\nKita sudah melakukan CREATE, READ, UPDATE, dan DELETE.")
print("Tetapi kita belum menulis data ke file atau database.")
print("Hentikan program, lalu jalankan lagi.")
print("Program akan kembali ke TAHAP 0 dengan list kosong.")
print("\nInilah alasan kita membutuhkan persistent storage seperti MySQL.")
