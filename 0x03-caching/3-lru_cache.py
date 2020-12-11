#!/usr/bin/env python3
"""BaseCaching Caching System"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """BaseCaching Caching System"""

    def __init__(self) -> None:
        """BaseCaching Caching System"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """BaseCaching Caching System"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """BaseCaching Caching System"""
        if key is not None:
            for k, v in self.cache_data.items():
                if k == key:
                    return v
        return None
