import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    author TEXT)""")

conn.commit()
conn.close()

print("Table created successfully!")