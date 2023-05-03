#!/usr/bin/env python3
""" Auth class is the template for all authentication system
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ class to manage the api authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False path and excluded paths
        """

    def authorization_header(self, request=None) -> str:
        """ Returns None request will be the flask
        """

    def current_user(self, request=None) -> TypeVar('user'):
        """ Returns None request will be the flask object
        """
