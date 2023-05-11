#!/usr/bin/env python3
""" This file is for Authentication of the user
"""
from bcrypt import hashpw, gensalt
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from bcrypt import checkpw
import uuid


def _hash_password(password: str) -> bytes:
    """ Takes password arguments and return bytes
    """
    return bcrypt.hashpw(password.encode('Utf-8'), gensalt())

def _generate_uuid() -> str:
        """ Implementing generate uuid and use uuid module
        """
        return str(uuid.uuid4())


class Auth:
    """ To implement Auth.register_user
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Takes email and password and return the User
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            new_user = self._db.add_user(email, hashed_pwd)
        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Implementing valid_login takes email and password arguments
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        user_pwd = user.hashed_password
        encoded_pwd = password.encode()

        if checkpw(encoded_pwd, user_pwd):
            return True
        else:
            return False

