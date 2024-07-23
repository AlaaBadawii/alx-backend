#!/usr/bin/env python3
"""
0-basic_cache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system
    """
    def put(self, key, item):
        """
        put data into the cache
        """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        get data from the cache
        """
        if not key or key not in self.cache_data:
            return None
        value = self.cache_data[key]
        return value
