#!/usr/bin/env python3
""" Basic Flask app
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index() -> str:
    """ Creating a flask app that has a single get
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
