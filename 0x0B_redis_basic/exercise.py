#!/usr/bin/env python3
"""Provide a Redis cache with call counting and history."""

import uuid
from functools import wraps
from typing import Callable, Optional, Union

import redis


def count_calls(method: Callable) -> Callable:
    """Count how many times the decorated method is called."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment the counter and execute the method."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the inputs and outputs of the decorated method."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Record the inputs and output of one method call."""
        inputs_key = "{}:inputs".format(method.__qualname__)
        outputs_key = "{}:outputs".format(method.__qualname__)

        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output)

        return output

    return wrapper


def replay(method: Callable) -> None:
    """Display the call history of a decorated method."""
    redis_client = method.__self__._redis
    method_name = method.__qualname__

    count = redis_client.get(method_name)
    call_count = int(count) if count is not None else 0

    print("{} was called {} times:".format(
        method_name,
        call_count,
    ))

    inputs = redis_client.lrange(
        "{}:inputs".format(method_name),
        0,
        -1,
    )
    outputs = redis_client.lrange(
        "{}:outputs".format(method_name),
        0,
        -1,
    )

    for input_data, output_data in zip(inputs, outputs):
        decoded_input = input_data.decode("utf-8")
        decoded_output = output_data.decode("utf-8")

        print("{}(*{}) -> {}".format(
            method_name,
            decoded_input,
            decoded_output,
        ))


class Cache:
    """Store and retrieve data from Redis."""

    def __init__(self) -> None:
        """Initialize the Redis client and clear its database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        """Retrieve data and optionally convert it."""
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
