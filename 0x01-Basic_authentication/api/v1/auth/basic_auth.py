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
