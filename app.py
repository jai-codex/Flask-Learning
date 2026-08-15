from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    students = ["Jai", "Rahul", "Amit", "Priya"]

    return render_template("index.html", students=students)


app.run(debug=True)
