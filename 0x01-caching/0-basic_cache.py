#!/usr/bin/python3
"""Basic Caching implementation"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache class"""
    def put(self, key, item):
        """ Put a key/value pair into the cache"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get a key/value pair from the cache"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
