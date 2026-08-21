from flask import Flask
from routes import register_routes
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "mysecretkey"

jwt = JWTManager(app)

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
