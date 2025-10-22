#!/usr/bin/env python3
"""
Exercise: Incrementing values with Redis
"""
from typing import Callable, Optional, Union
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called.
    Stores the count in Redis using method.__qualname__ as the key.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)  # Increment the counter in Redis
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class to store and retrieve data in Redis"""

    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int]) -> str:
        """
        Store a value in Redis and return a generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """
        Retrieve a value from Redis and optionally convert it using fn.
        Returns None if key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a value and convert it to string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve a value and convert it to int.
        """
        return self.get(key, fn=int)


# Example usage for verification
if __name__ == "__main__":
    cache = Cache()

    # Call store multiple times
    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))  # Should print b'1'

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))  # Should print b'3'
