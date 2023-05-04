#!/usr/bin/env python3
""" Basic auth
"""
from base64 import b64encode
from api.v1.auth.auth import Auth
from typing import TypeVar, Tuple
from models.user import User
import base64


class BasicAuth(Auth):
    """ Class inherits from the auth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Basic base64 part
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(' ', 1)[1]

        return encoded

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ Basic base64 decode
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded64 = base64.b64decode(base64_authorization_header)
            return decoded64.decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ That returns the user email and password
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        return decoded_base64_authorization_header.split(':', 1)

    def user_object_from_credentials(
            self,
            user_email:  str, user_pwd: str) -> TypeVar('user'):
        """ That returns the User instance based on his email
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for x in users:
            if x.is_valid_password(user_pwd):
                return x

        return None

    def current_user(self, request=None) -> TypeVar('user'):
        """ That overloads Auth and retrieves the User
        """
        auth = self.authorization_header(request)

        if not auth:
            return None

        encoded = self.extract_base64_authorization_header(auth)

        if not encoded:
            return None

        decoded = self.extract_base64_authorization_header(encoded)

        if not decoded:
            return None

        email, password = self.extract_user_credentials(decoded)

        if not email or not password:
            return None

        users = self.user_object_from_credentials(email, password)

        return users
