#!/usr/bin/env python3
"""Provide a basic Redis cache."""

import uuid
from typing import Union

import redis


class Cache:
    """Store data in Redis using randomly generated keys."""

    def __init__(self) -> None:
        """Initialize the Redis client and clear its database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return its generated key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
