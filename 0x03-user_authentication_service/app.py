#!/usr/bin/env python3
""" Basic Flask app
"""
from flask import Flask, jsonify, request, abort
from auth import Auth
from typing import Tuple, Union

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def index() -> str:
    """ Creating a flask app that has a single get
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> Tuple[str, int]:
    """ Implement the end-point to register
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    opt = {"email": email, "message": "user created"}
    return jsonify(opt)


@app.route('/sessions', methods='POST')
def login() -> str:
    """ Implement login respond post/sessions
    """
    email = request.form.get('email')
    password = request.form.get('password')

    session_id = Auth.create_session(email)
    respo = jsonify({'email': email, 'message': 'logged in'})
    respo.set_cookie('session_id', session_id)
    return respo

    if not AUTH.valid_login(email, password):
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
