#!/usr/bin/env python3
"""
3-lru_cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache a caching system
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

        if key in self.cache_data:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                rm_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {rm_key}")

            self.cache_data[key] = item

    def get(self, key):
        """
        get value from cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
