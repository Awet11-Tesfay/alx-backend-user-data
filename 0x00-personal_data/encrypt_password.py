#!/usr/bin/env python3
""" Encripting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Function that expects onet string and return a hashed password
    """
    en_pass = password.encode()
    hashed = bcrypt.hashpw(en_pass, bcrypt.gensalt())
    
    return hashed
