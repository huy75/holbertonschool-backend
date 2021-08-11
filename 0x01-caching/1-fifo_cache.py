#!/usr/bin/python3
""" Python caching systems """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.current_keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.current_keys:
                self.current_keys.append(key)
            if len(self.current_keys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.current_keys.pop(0)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
