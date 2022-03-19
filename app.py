from flask import render_template, jsonify
import random

templates = [
    {
        "inputs": 5,
        "catagory": "Sports",
        "word": "Chess"
    },
    {
        "inputs": 6,
        "catagory": "European Country Name",
        "word": "France"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status": "success",
        "word": random.choice(templates)
    })