from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def register():

    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_user():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(username, password) VALUES(?, ?)",
        (username, password))

    conn.commit()
    conn.close()
    
    return "Registration Successfully!"

if __name__ == "__main__":
    app.run(debug=True)    
