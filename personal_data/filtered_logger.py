#!/usr/bin/env python3
"""Masquer certains champs d’un message de log"""
import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str,
    message: str, separator: str
) -> str:
    """
    Obfuscate fields in a log message.

    Args:
        fields (List[str]): List of field names to redact.
        redaction (str): The string used to replace field values.
        message (str): The original log message.
        separator (str): The character separating fields in the message.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    pattern = fr"({'|'.join(fields)})=.*?{separator}"
    return re.sub(
        pattern,
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message
    )
