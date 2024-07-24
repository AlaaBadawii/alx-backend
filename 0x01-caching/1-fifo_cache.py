#!/usr/bin/env python3
"""
1-fifo_cache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class is a caching system
    """
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Put data into cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Get data from the cache
        """
        return self.cache_data.get(key)
