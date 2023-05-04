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
