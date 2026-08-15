import sqlite3

name = input("Enter Book Name: ")
author = input("Author Name: ")

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO books (name, author) VALUES (?, ?)",
    (name, author))

conn.commit()
conn.close()

print("Inserted Successfully!")