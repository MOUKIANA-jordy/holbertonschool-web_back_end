#!/usr/bin/env python3
"""Masquer certains champs d’un message de log à l’aide d’une expression régulière"""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    pattern = fr"({'|'.join(fields)})=.*?{separator}"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message)
