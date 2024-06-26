#!/usr/bin/env python3
"""
LIFO/FILO Cache module for implementation of LIFO caching algorithm
"""
from collections import deque

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Definition of LIFOCache class that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialization
        """
        super().__init__()
        self.stack = deque()

    def put(self, key, item):
        """ Put an item in the cache
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    evicted_key = self.stack.pop()
                    del self.cache_data[evicted_key]
                    print(f"DISCARD: {evicted_key}")
                else:
                    self.stack.remove(key)

            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        return self.cache_data.get(key)
