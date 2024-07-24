#!/usr/bin/env python3
"""
2-lifo_cache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache a caching system
    """
    def put(self, key, item):
        """
        put item into cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and\
                key not in self.cache_data:
            last_key = next(reversed(self.cache_data))
            self.cache_data.pop(last_key)
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        get item from cache
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
