from flask import Flask, render_template, request, redirect
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

@app.route("/add", methods=["POST"])
def add():

    name = request.form["name"]
    author = request.form["author"]

    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO books(name, author) VALUES(?, ?)", (name, author))
    
    conn.commit()
    conn.close()

    return redirect("/")
    
app.run(debug=True)
