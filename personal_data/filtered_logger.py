import logging
import re

def filter_datum(fields, redaction, message, separator):
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

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original, self.SEPARATOR)

