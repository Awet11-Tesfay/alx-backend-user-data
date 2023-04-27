#!/usr/bin/env python3
""" PII and personal data
"""

from typing import List
from logging import Formatter, Logger, LogRecord, getLogger
from logging import INFO, StreamHandler
import logging
import re
import mysql.connector
from os import environ

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ A function called filter_datum that the log message
    """
    for y in fields:
        message = re.sub(f'{y}=.*?{separator}',
                         f'{y}={redaction}{separator}', message)
    return message


class RedactingFormatter(Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """ initialized method
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: LogRecord) -> str:
        """ Filter values in incomming log records
        """
        message = filter_datum(self.fields, self.REDACTION,
                               record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self.format(record))


def get_logger() -> Logger:
    """ Returns a logging.logger object
    """
    logg = getLogger("user_data")
    logg.setLevel(INFO)
    logg.propagate = False

    handler = StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logg.addHandler(handler)

    return logg
