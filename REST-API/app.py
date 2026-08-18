from flask import Flask, jsonify

app = Flask(__name__)

students = [{
    "id" : 1,
    "name" : "Jai",
    "ahe" : 19
}]

@app.route("/")
def home():
    return "Students API is Running!"

@app.route("/students")
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)
