#!/usr/bin/python3
""" Python caching systems """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRU caching system
    """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.cache_data = OrderedDict()
        self.last_visited = ""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.last_visited = key
                else:
                    the_key = self.last_visited
                    del self.cache_data[the_key]
                    print("DISCARD: {}".format(the_key))
                    self.cache_data[key] = item
                    self.last_visited = key
            else:
                self.cache_data[key] = item
                self.last_visited = key

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.last_visited = key
            return self.cache_data[key]
