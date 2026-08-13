from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🏠 Home Page"

@app.route("/about")
def about():
    return "ℹ️ About Page"

@app.route("/contact")
def contact():
    return "📞 Contact Page"

@app.route("/services")
def services():
    return "Services"

@app.route("/profile")
def profile():
    return "Welcome to my profile!"

app.run(debug=True)