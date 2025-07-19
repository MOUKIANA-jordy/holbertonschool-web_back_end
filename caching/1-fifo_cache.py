#!/usr/bin/env python3
""" FifoCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system that inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        Add an item in the cache using FIFO policy
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the first item (FIFO)
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key, None)
