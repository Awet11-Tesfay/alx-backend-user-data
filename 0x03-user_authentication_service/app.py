#!/usr/bin/env python3
""" Basic Flask app
"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Implement login respond post/sessions
    """
    email = request.form.get('email')
    password = request.form.get('password')
    valid_login = AUTH.valid_login(email, password)
    if valid_login:
        session_id = AUTH.create_session(email)
        respo = jsonify({"email": f'{email}', "message": "logged in"})
        respo.set_cookie("session_id", session_id)
        return respo
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ Function to respond to the Delete/Session route
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """ Implement profile using get/profile route
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    else:
        return jsonify({'email': user.email})


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token() -> str:
    """ Funciton to respond to the post
    """
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token})
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password() -> str:
    """ Function in the app module to respond put/reset_password
    """
    new_password = request.form.get('new_password')
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    try:
        AUTH.update_password(reset_token, new_password)
    except Exception:
        abort(403)

    return jsonify({"email": f'{email}', "message": "password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
