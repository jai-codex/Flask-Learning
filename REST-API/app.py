from flask import Flask, jsonify, request

app = Flask(__name__)

students = [{
    "id" : 1,
    "name" : "Jai",
    "age" : 19
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

@app.route("/students/<int:id>", methods=["PUT"])
def update_name(id):

    data = request.get_json()

    for student in students:
        if student["id"] == id:
            student["name"] = data["name"]
            student["age"] = data["age"]

            return jsonify({"message": "Student Updated",
            "student": student}),200
    return jsonify({"message": "Student Not Found"}),404        

if __name__ == "__main__":
    app.run(debug=True)
