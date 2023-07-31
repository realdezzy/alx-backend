#!/usr/bin/python3
""" LRU cache """
from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """
        LRUCache implementation
    """
    def __init__(self):
        """ Initialize the cache"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        if key in self.cache_data:
            self.queue.remove(key)
        if len(self.cache_data) >= self.MAX_ITEMS:
            rm_key = self.queue.popleft()
            del self.cache_data[rm_key]
            print(f"DISCARD: {rm_key}")
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
