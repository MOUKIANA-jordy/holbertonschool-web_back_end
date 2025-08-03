#!/usr/bin/env python3
"""
Module to securely hash passwords using bcrypt and validate them.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with automatic salting.

    Args:
        password (str): The plain-text password to hash.

    Returns:
        bytes: The salted and hashed password.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if a provided password matches the hashed password.

    Args:
        hashed_password (bytes): The bcrypt hashed password.
        password (str): The plain-text password to verify.

    Returns:
        bool: True if password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

