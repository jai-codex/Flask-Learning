from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    is_student = False

    return render_template("index.html", is_student=is_student)


app.run(debug=True)
