from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

import nature

app = Flask(__name__, static_folder="public")
CORS(app) 

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route("/hash", methods=["POST"])
def handle_hash():
    try:
        data = request.get_json()
        print("data", data)
        if not data:
            return jsonify({ "error": "Invalid JSON" }), 400
        text = data.get("text")
        live_0 = data.get("live_0")
        live_1 = data.get("live_1")
        output = nature.hash(text, live_0, live_1)
        print(output)
        return jsonify({ "output": output }), 200
    except Exception as e:
        print(e)
        return jsonify({ "error": "Error" }), 400

