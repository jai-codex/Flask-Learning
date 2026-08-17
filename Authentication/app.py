from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, render_template, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "mysecretkey123"


@app.route("/")
def home():
    return redirect("/login")


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
        "INSERT INTO users(username, password) VALUES(?, ?)", (username, password)
    )

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

    cursor.execute("SELECT password FROM users WHERE username=?", (username,))

    user = cursor.fetchone()

    conn.close()

    if user and check_password_hash(user[0], password):
        session["username"] = username
        return redirect("/dashboard")
    else:
        return "Invalid Username or password!"


@app.route("/dashboard")
def dashboard():

    if "username" in session:
        return f"Welcome {session['username']}"
    return "Please Login First!"


@app.route("/logout")
def logout_user():

    session.pop("username", None)
    return "Logged Out Successfully!"


if __name__ == "__main__":
    app.run(debug=True)
