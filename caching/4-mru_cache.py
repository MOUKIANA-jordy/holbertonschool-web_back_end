#!/usr/bin/python3
"""MRU caching module."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implement a Most Recently Used caching system."""

    def __init__(self):
        """Initialize the cache and usage order."""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item using the MRU replacement policy."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item

            if key in self.usage_order:
                self.usage_order.remove(key)

            self.usage_order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recent_key = self.usage_order.pop()

            del self.cache_data[most_recent_key]
            print("DISCARD: {}".format(most_recent_key))

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """Return an item and mark it as recently used."""
        if key is None or key not in self.cache_data:
            return None

        if key in self.usage_order:
            self.usage_order.remove(key)

        self.usage_order.append(key)

        return self.cache_data[key]
