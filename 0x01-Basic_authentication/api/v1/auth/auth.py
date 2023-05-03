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
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for x in excluded_paths:
                if x.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if x[-1] == "*":
                    if path.startswith(x[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Returns None request will be the flask
        """

    def current_user(self, request=None) -> TypeVar('user'):
        """ Returns None request will be the flask object
        """
