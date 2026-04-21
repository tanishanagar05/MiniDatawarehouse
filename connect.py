import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tanisha",
    database="mini_warehouse"
)

if conn.is_connected():
    print("✅ MySQL Connected Successfully!")
    cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS mini_warehouse")
print("Database created ✅")