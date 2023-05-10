#!/usr/bin/env python3
""" This file is for Authentication of the user
"""
from bcrypt import hashpw, gensalt



def _hash_password(password: str) -> bytes:
    """ Takes password arguments and return bytes
    """
    return hashpw(password.encode('Utf-8'), gensalt)
