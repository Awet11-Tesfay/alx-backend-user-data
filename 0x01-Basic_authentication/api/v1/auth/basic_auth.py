#!/usr/bin/env python3
""" Basic auth
"""
from base64 import b64encode
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


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
