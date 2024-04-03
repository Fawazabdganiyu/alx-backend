#!/usr/bin/env python3
"""
LFU Cache module for implementation of LFU caching algorithm
"""
from collections import defaultdict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Definition of LFUCache class that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialization
        """
        super().__init__()
        self.count = defaultdict(int)

    def put(self, key, item):
        """ Put an item in the cache
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    evicted_key = min(self.count, key=self.count.get)
                    self.count.pop(evicted_key)
                    del self.cache_data[evicted_key]
                    print(f"DISCARD: {evicted_key}")

            self.count[key] += 1
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key in self.count:
            self.count[key] += 1

        return self.cache_data.get(key)
