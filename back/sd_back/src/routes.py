from flask import request, jsonify
from src import app

@app.route("/")
def hello():
    return "Hello World! ;)"
