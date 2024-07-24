#!/usr/bin/env python3
"""
100-lfu module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.hit_num = OrderedDict()

    def put(self, key, item):
        """
        Put value into cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.hit_num[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lfu_key = min(self.hit_num, key=self.hit_num.get)
                self.cache_data.pop(lfu_key)
                self.hit_num.pop(lfu_key)
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.hit_num[key] = 1

    def get(self, key):
        """
        Get value from cache
        """
        if key not in self.cache_data:
            return None

        self.hit_num[key] += 1
        return self.cache_data[key]
