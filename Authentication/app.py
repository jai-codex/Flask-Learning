from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/register")
def register():

    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_user():

    username = request.form["username"]
    password = generate_password_hash(request.form["password"])

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(username, password) VALUES(?, ?)",
        (username, password))

    conn.commit()
    conn.close()
    
    return "Registration Successfully!"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_user():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,))

    user = cursor.fetchone()

    conn.close()

    if user and check_password_hash(user[0], password):
        return "Login Successful!"
    else:
        return "Invalid Username or password!" 

if __name__ == "__main__":
    app.run(debug=True)    
