"""CREATE: menambahkan dictionary baru ke dalam list."""

transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 25000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
]

print("SEBELUM DITAMBAH:")
print(transactions)

# Satu transaksi baru dibuat sebagai dictionary.
transaction_baru = {
    "id": 3,
    "nama": "Transport",
    "total": 15000,
}

# append() menambahkan dictionary ke bagian akhir list.
transactions.append(transaction_baru)

print("\nSESUDAH DITAMBAH:")
for transaction in transactions:
    print(transaction["id"], "|", transaction["nama"], "| Rp", transaction["total"])

# Expected:
# 1 | Kopi Susu | Rp 25000
# 2 | Makan Siang | Rp 35000
# 3 | Transport | Rp 15000
