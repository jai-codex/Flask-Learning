from flask import Flask, jsonify, request
import sqlite3

app = Flask("__name__")


@app.route("/students")
def get_students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()
    conn.close()

    return jsonify(students)


@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age) VALUES(?, ?)", (data["name"], data["age"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Student Added Sucessfully!"}), 201


@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    data = request.get_json()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=?, age=? WHERE id=?", (data["name"], data["age"], id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Student Updated Successfully!"}), 200


@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Student Deleted Successfully!"}), 200


app.run(debug=True)
