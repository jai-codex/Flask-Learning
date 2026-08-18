from flask import Flask, jsonify, request

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

@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()
    students.append(data)

    return jsonify({
        "message": "Student Added Successfully!",
        "students": students}),201    

if __name__ == "__main__":
    app.run(debug=True)
