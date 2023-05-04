#!/usr/bin/env python3
""" Session class that inherits from Auth
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """ That inherits from Auth
    """