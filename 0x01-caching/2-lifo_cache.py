#!/usr/bin/env python3
'''a class LIFOCache that inherits from
   BaseCaching and is a caching system:'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''LIFOCache module'''

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.placeholder = []

    def put(self, key, item):
        '''adds item to key'''
        '''super().put(key, item)'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = self.placeholder.pop()
            discard = self.cache_data.pop(last)
            print(f'DISCARD: {last}')
        self.cache_data[key] = item
        self.placeholder.append(key)

    def get(self, key):
        '''gets the value of a key'''
        '''super().get(key)'''
        if key is None:
            return None

        return self.cache_data.get(key)
