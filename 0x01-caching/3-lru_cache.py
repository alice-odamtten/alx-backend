#!/usr/bin/env python3
'''a class LRUCache that inherits from
   BaseCaching and is a caching system:'''
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''LRUCache module'''

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.placeholder = OrderedDict()

    def put(self, key, item):
        '''adds item to key'''
        '''super().put(key, item)'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = next(iter(self.placeholder))
            discard = self.cache_data.pop(last)
            del self.placeholder[last]
            print(f'DISCARD: {last}')
        self.cache_data[key] = item
        self.placeholder[key] = True

    def get(self, key):
        '''gets the value of a key'''
        '''super().get(key)'''
        if key is None:
            return None
        if key in self.placeholder:
            del self.placeholder[key]
            self.placeholder[key] = True

        return self.cache_data.get(key)
