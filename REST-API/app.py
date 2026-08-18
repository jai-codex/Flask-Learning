from flask import Flask, request, jsonify

app = Flask(__name__)

books = []

@app.route("/books", methods=["POST"])
def add_book():

    data = request.get_json()

    books.append(data)

    return jsonify({
        "message": "Book Added",
        "books": books
    }), 201

if __name__ == "__main__":
    app.run(debug=True)