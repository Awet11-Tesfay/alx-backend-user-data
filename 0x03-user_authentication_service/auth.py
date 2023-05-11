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
from typing import Union


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

    def create_session(self, email: str) -> str:
        """ Implementing create_session takes str return session id
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ Implement get user from session id
        """
        if session_id is None:
            return None

        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Takes user_id and returns None
        """
        if user_id:
            return self._db.update_user(user_id, session_id=None)
        else:
            return None