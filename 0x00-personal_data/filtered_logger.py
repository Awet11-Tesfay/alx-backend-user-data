#!/usr/bin/env python3
""" Regex ing
"""

from typing import List
import logging
import re
import mysql.connector
from os import environ

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, seperator: str) -> str:
    """ A function called filter_datum that the log message
    """
    for y in fields:
        message = re.sub("{y}=.*?{seperator}",
                         "{y}={redaction}{separator}", message)
    return message
