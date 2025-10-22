#!/usr/bin/env python3
"""
Exercise: Storing lists with call history in Redis
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
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        # Store input arguments
        self._redis.rpush(inputs_key, str(args))

        # Call the original function
        result = method(self, *args, **kwargs)

        # Store output
        self._redis.rpush(outputs_key, result)
        return result

    return wrapper


class Cache:
    """Cache class to store and retrieve data in Redis"""

    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        """Retrieve a value and convert it to string"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve a value and convert it to int"""
        return self.get(key, fn=int)


# Example usage for verification
if __name__ == "__main__":
    cache = Cache()

    s1 = cache.store("first")
    s2 = cache.store("secont")
    s3 = cache.store("third")

    inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

    print("inputs:", inputs)
    print("outputs:", outputs)

