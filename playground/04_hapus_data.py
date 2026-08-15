"""DELETE: membuat list baru tanpa dictionary yang ID-nya dihapus."""

transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 25000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
    {"id": 3, "nama": "Transport", "total": 15000},
]

id_yang_dihapus = 2
transactions_baru = []
berhasil_dihapus = False

print("SEBELUM DELETE:")
print(transactions)

for transaction in transactions:
    if transaction["id"] == id_yang_dihapus:
        # Dictionary target tidak dimasukkan ke list baru.
        berhasil_dihapus = True
    else:
        transactions_baru.append(transaction)

transactions = transactions_baru

print("\nSESUDAH DELETE:")
print("Data berhasil dihapus." if berhasil_dihapus else "Data tidak ditemukan.")

for transaction in transactions:
    print(transaction["id"], "|", transaction["nama"], "| Rp", transaction["total"])

# Expected: ID 2 tidak tampil lagi.
# 1 | Kopi Susu | Rp 25000
# 3 | Transport | Rp 15000
