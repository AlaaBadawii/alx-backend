#!/usr/bin/env python3
"""
2-lifo_cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    LIFOCache a caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        put item into cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        get item from cache
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
