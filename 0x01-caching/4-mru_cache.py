#!/usr/bin/env python3
"""
4-mru_cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache a caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        put value into cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                rm_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(rm_key)
                print(f"DISCARD: {rm_key}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        get value from cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key, last=True)
        return self.cache_data[key]
