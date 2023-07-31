#!/usr/bin/python3
""" Lifo Cache"""
from base_caching import BaseCaching
   

class LIFOCache(BaseCaching):
    """ Lifo cache implementation
    """
    def __init__(self):
        """ Initialize the cache"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        if len(self.cache_data) >= self.MAX_ITEMS:
            data_keys = [k for k in self.cache_data.keys()]
            rm_key = data_keys.pop()
            del self.cache_data[rm_key]
            print(f"DISCARD: {rm_key}")
        self.cache_data[key] = item
 
    def get(self, key):
        """ Get a key/value pair from the cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]