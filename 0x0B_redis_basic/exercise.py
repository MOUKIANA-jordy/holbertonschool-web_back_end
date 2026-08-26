#!/usr/bin/env python3
"""Provide a Redis cache with call-counting support."""

import uuid
from functools import wraps
from typing import Callable, Optional, Union

import redis


def count_calls(method: Callable) -> Callable:
    """Count how many times the decorated method is called."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment the call counter and call the original method."""
        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Store and retrieve data from Redis."""

    def __init__(self) -> None:
        """Initialize the Redis client and clear its database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return its generated key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None,
    ):
        """Retrieve data and optionally convert it using a callable."""
        data = self._redis.get(key)

        if data is None:
            return None

        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data from Redis as a UTF-8 string."""
        return self.get(
            key,
            fn=lambda data: data.decode("utf-8"),
        )

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data from Redis as an integer."""
        return self.get(key, fn=int)
