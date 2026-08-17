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

if __name__ == "__main__":
    app.run(debug=True)