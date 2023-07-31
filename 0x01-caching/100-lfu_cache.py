#!/usr/bin/python3
""" LFUCache cache"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
        LFUCache implementation
    """
    def __init__(self):
        """ Initialize the cache"""
        super().__init__()
        self.queue = dict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key is None or item is None):
            return

        if (len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS
           and key not in self.cache_data.keys()):
            discard_key = min(self.queue, key=self.queue.get)
            del self.cache_data[discard_key]
            del self.queue[discard_key]
            print("DISCARD: {}".format(discard_key))
        if (key in self.cache_data.keys()):
            self.queue[key] += 1
        else:
            self.queue[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if (key is None or key not in self.cache_data.keys()):
            return
        self.queue[key] += 1
        return self.cache_data.get(key)
