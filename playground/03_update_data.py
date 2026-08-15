"""UPDATE: mencari dictionary berdasarkan ID lalu mengubah value."""

transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 25000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
    {"id": 3, "nama": "Transport", "total": 15000},
]

id_yang_diubah = 1
total_baru = 30000
berhasil_diubah = False

print("SEBELUM UPDATE:")
print(transactions)

for transaction in transactions:
    if transaction["id"] == id_yang_diubah:
        transaction["total"] = total_baru
        berhasil_diubah = True
        break

print("\nSESUDAH UPDATE:")
print("Data berhasil diubah." if berhasil_diubah else "Data tidak ditemukan.")

for transaction in transactions:
    print(transaction["id"], "|", transaction["nama"], "| Rp", transaction["total"])

# Expected untuk ID 1:
# 1 | Kopi Susu | Rp 30000
