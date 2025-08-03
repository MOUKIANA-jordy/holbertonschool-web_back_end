#!/usr/bin/env python3
"""Module for filtering and redacting sensitive log information."""
import os
import re
import logging
from typing import List
import mysql.connector
from mysql.connector.connection import MySQLConnection


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message.
    """
    pattern = fr"({'|'.join(fields)})=.*?{separator}"
    return re.sub(
        pattern,
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message
    )


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:

        return filter_datum(
            self.fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR
        )


# Ces deux lignes doivent être en dehors de la classe RedactingFormatter
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """Creates and configures a logger for user data."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Connects to a MySQL database using environment variables.
    Returns:
        A MySQLConnection object.
    """
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def main():
    """Retrieve all rows from users table and log them with PII redacted."""
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users;")
    fields = [col[0] for col in cursor.description]

    logger = get_logger()

    for row in cursor:
        record = "; ".join(f"{field}={value}" for field, value in zip(fields, row)) + ";"
        logger.info(record)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

