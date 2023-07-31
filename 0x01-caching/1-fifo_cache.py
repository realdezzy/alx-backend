#!/usr/bin/python3
""" Fifo Cache"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """
        Fifo Cache implementation
    """
    def __init__(self):
        """ Initialize the cache"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not key or not item:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            removed_key = self.queue.popleft()
            self.cache_data.pop(removed_key)
            print('DISCARD: {}'.format(removed_key))

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ Get a key/value pair from the cache"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
