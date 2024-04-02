#!/usr/bin/env python3
""" BasicCache module
"""

from basic_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Definition of BasicCache class that inherits from BaseCaching
    """
    def put(self, key, item):
        """ Put an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if not key:
            return None

        return self.cache_data.get(key)
