#!/usr/bin/env python3
"""
Definition of `BasicCache` module as basic caching algorithm
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Definition of `BasicCache` class that inherits from `BaseCaching`
    """

    def put(self, key, item):
        """ Put an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        return self.cache_data.get(key)
