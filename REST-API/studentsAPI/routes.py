from flask import jsonify, request
from database import get_connection
from flask_jwt_extended import create_access_token, jwt_required


def register_routes(app):

    @app.route("/register", methods=["POST"])
    def register():

        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({
                "message": "Username and Password are required"
            }), 400

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users(username, password) VALUES(?, ?)",
                (username, password)
            )

            conn.commit()

            return jsonify({
                "message": "User Registered Successfully"
            }), 201

        except Exception:
            return jsonify({
                "message": "Username already exists"
            }), 400

        finally:
            conn.close()

    @app.route("/login", methods=["POST"])
    def login():

        data = request.get_json()

        username = data.get("username") 
        password = data.get("password")

        if not username or not password:
            return jsonify({
                "message": "Username and Password is required"
            }), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,))

        user = cursor.fetchone()

        conn.close()

        if user is None:
            return jsonify({
                "message": "User not found!"
            }), 404

        if user[2] != password:
            return jsonify({
                "message": "Incorrect password!"
            }), 401 

        token = create_access_token(identity=username)

        return jsonify({
            "message": "Login SuccessfullY!",
            "token": token
        }), 200    

    @app.route("/students", methods=["GET"])
    @jwt_required()
    def get_students():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")

        rows = cursor.fetchall()

        conn.close()

        students = []

        for row in rows:
            students.append({"ID": row[0], "Name": row[1], "Age": row[2]})

        return jsonify(students)

    @app.route("/students", methods=["POST"])
    def add_student():

        data = request.get_json()

        if "name" not in data:
            return jsonify({"message": "Name is required"}), 400

        if "age" not in data:
            return jsonify({"message": "Age is required"}), 400

        try:

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO students(name, age) VALUES(?, ?)",
                (data["name"], data["age"]),
            )

            conn.commit()
            conn.close()

            return jsonify({"message": "Student Added Successfully!"}), 201

        except Exception as e:

            return jsonify({"message": "Something went wrong", "error": str(e)}), 500

    @app.route("/students/<int:id>", methods=["PUT"])
    def update_student(id):

        data = request.get_json()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE students SET name=?, age=? WHERE id=?",
            (data["name"], data["age"], id),
        )

        conn.commit()
        conn.close()

        return jsonify({"message": "Student Updated Successfully!"}), 200

    @app.route("/students/<int:id>", methods=["DELETE"])
    def delete_student(id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM students WHERE id=?", (id,))

        conn.commit()
        conn.close()

        return jsonify({"message": "Student Deleted Successfully!"}), 200
