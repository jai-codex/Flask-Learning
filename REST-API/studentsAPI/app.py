from flask import Flask
from routes import register_routes
from flask_jwt_extended import JWTManager, create_access_token
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

jwt = JWTManager(app)

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
