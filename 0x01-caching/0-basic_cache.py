#!/usr/bin/env python3
'''a class BasicCache that inherits from
   BaseCaching and is a caching system:'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''Basiccache module'''
    
    
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        '''adds item to key'''
        #super().put(key, item)
        if key is None or item is None:
            return

        self.cache_data.update({key: item})

    def get(self, key):
        '''gets the value of a key'''
        #super().get(key)
        if key is None:
            return None

        return self.cache_data.get(key)
