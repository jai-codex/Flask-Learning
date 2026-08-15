from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM books")

    books = cursor.fetchall()

    conn.close()

    return render_template("index.html", books=books)


app.run(debug=True)
