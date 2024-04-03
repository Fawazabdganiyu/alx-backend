#!/usr/bin/env python3
"""
LRU Cache module for implementation of LRU caching algorithm
"""
from collections import deque

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Definition of LRUCache class that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialization
        """
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """ Put an item in the cache
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    evicted_key = self.order.popleft()
                    del self.cache_data[evicted_key]
                    print(f"DISCARD: {evicted_key}")
                else:
                    self.order.remove(key)

            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key in self.order:
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key)
