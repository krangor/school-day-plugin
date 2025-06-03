from flask import Flask, jsonify, Response
import json

app = Flask(__name__)

# Load and clean data on startup
with open("calendar.json") as f:
    original_data = json.load(f)

# Remove emoji just to test if TRMNL chokes on them
def clean_value(value):
    return value if value.isnumeric() else "X"

cleaned_data = {k: clean_value(v) for k, v in original_data.items()}

@app.route("/")
def index():
    return Response(json.dumps(cleaned_data), mimetype="application/json")

@app.route("/debug")
def debug():
    return jsonify({
        "message": "API is up",
        "sample": cleaned_data.get("2025-06-03")
    })
