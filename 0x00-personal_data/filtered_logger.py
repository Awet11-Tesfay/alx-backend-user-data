#!/usr/bin/env python3
""" PII and personal data
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
        message = re.sub(f'{y}=.*?{seperator}',
                         f'{y}={redaction}{seperator}', message)
    return message
