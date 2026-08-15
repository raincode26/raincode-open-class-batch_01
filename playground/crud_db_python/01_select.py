import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = None,
    database = "raincode_expense"
)

# MENAMPILKAN DATA DARI TABLE TRANSACTIONS
cursor = db.cursor(dictionary=True)

cursor.execute("SELECT * FROM transactions")

data = cursor.fetchall()

print(data)