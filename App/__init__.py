from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def create_app():

    from app.Api.Hello import HelloController

    return app