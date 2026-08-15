from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():

    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    conn.close()

    return render_template("index.html", books=books)


@app.route("/add", methods=["POST"])
def add():

    name = request.form["name"]
    author = request.form["author"]

    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books(name, author) VALUES(?, ?)", (name, author))

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/update", methods=["POST"])
def update_book():

    book_id = request.form["id"]
    name = request.form["name"]
    author = request.form["author"]

    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE books SET name=?, author=? WHERE id=?", (name, author, book_id)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete_book():

    book_id = request.form["id"]

    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))

    conn.commit()
    conn.close()

    return redirect("/")


app.run(debug=True)
