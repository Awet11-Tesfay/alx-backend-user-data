#!/usr/bin/env python3
""" Basic Flask app
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def index() -> str:
    """ Creating a flask app that has a single get
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", method="POST")
def users(self, email: str, passowrd: str) -> str:
    """ Implement the end-point to register
    """
    email = request.form.get('email')
    password = request.form.get(password)
    try:
        user = AUTH.register_user(email, password)
        opt = jsonify({"email": email, "message": "user created"})
        return opt

    except ValueError:
        inp = jsonify({"message": "email already registered"})
        return inp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
