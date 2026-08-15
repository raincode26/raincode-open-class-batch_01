import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = None,
    database = "raincode_expense"
)


name = "Ongkos Ojek"
price = 130000

# MENAMPILKAN DATA DARI TABLE TRANSACTIONS
cursor = db.cursor()

cursor.execute("INSERT into transactions (name, total) VALUES (%s, %d)", (name, price))

db.commit()