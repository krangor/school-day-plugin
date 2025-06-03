from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open("calendar.json") as f:
        data = json.load(f)
    return jsonify(data)
