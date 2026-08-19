from flask import Flask, jsonify, request
import sqlite3

app = Flask("__name__")

@app.route("/students")
def get_students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students")

    students = cursor.fetchall()
    conn.close()
    
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age) VALUES(?, ?)",
        (data["name"], data["age"]))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student Added Sucessfully!"}), 201    

app.run(debug=True)