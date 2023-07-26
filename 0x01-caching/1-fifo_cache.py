#!/usr/bin/env python3
BaseCaching = __import__("baseCaching").BaseCaching
   

class FIFOCache(BaseCaching):
    """

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """ Initialize the cache"""
        super().__init__()

    def put(self, key, item):
        """ Put an item"""

    def get(self, key):
        """ Get an item by key"""