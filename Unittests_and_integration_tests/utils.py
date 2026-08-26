#!/usr/bin/env python3
"""Generic utilities for GitHub organization client."""

import requests
from functools import wraps
from typing import Any, Callable, Dict, Mapping, Sequence


__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access a value in a nested mapping using a sequence of keys."""
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -> Dict:
    """Retrieve and return JSON data from a remote URL."""
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """Memoize the result of an instance method."""
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """Return the cached result or compute and store it."""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
