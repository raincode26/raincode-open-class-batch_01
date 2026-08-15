"""READ: mengambil seluruh data dan satu data berdasarkan ID."""

transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 25000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
    {"id": 3, "nama": "Transport", "total": 15000},
]

# READ ALL: loop seluruh dictionary di dalam list.
print("SEMUA TRANSAKSI:")
for transaction in transactions:
    print(transaction["id"], "|", transaction["nama"], "| Rp", transaction["total"])

# READ ONE: cari satu dictionary berdasarkan ID.
id_yang_dicari = 2
data_ditemukan = None

for transaction in transactions:
    if transaction["id"] == id_yang_dicari:
        data_ditemukan = transaction
        break

print("\nHASIL PENCARIAN ID", id_yang_dicari)

if data_ditemukan is not None:
    print("Nama :", data_ditemukan["nama"])
    print("Total:", data_ditemukan["total"])
else:
    print("Data tidak ditemukan.")

# Expected:
# Nama : Makan Siang
# Total: 35000
