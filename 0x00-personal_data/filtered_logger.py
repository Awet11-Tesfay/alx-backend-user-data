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
        loggg = re.sub(f'{y}=.*?{separator}',
                       f'{y}={redaction}{separator}', loggg)
        return loggg


class RedactingFormatter(Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ initialized method
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: LogRecord) -> str:
        """ Filter values in incomming log records
        """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> Logger:
    """ Returns a logging.logger object
    """
    logg = getLogger("user_data")
    logg.setLevel(INFO)
    logg.propagate = False

    handler = StreamHandler()
    habits = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(habits)
    logg.addHandler(handler)

    return logg
