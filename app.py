from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "Python",
        "author": "Guido"
    },
    {
        "id": 2,
        "title": "Flask",
        "author": "Armin"
    }
]

@app.route("/books")
def get_books():
    return jsonify(books)

@app.route("/books/<int:id>")
def get_book(id):

    for book in books:
        if book["id"] == id:
            return jsonify(book)

    return jsonify({"message": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)