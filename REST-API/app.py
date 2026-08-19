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

app.run(debug=True)