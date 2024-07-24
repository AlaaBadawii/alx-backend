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

    def get(self, key):
        """
        get value from cache
        """
        if key is None or key not in self.cache_data:
            return None
