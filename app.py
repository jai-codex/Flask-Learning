from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/welcome", methods=["POST"])
def welcome():
    name = request.form["username"]
    return f"Welcome {name}"

app.run(debug=True)
