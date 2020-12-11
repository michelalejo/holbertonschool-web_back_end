#!/usr/bin/env python3
"""BaseCaching Caching System"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """BaseCaching Caching System"""

    def __init__(self) -> None:
        """BaseCaching Caching System"""
        super().__init__()
        self.tmp = []

    def put(self, key, item):
        """BaseCaching Caching System"""
        if key and item:
            self.cache_data[key] = item
            if key not in self.tmp:
                self.tmp.append(key)
            else:
                self.tmp.append(self.tmp.pop(self.tmp.index(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                firt = self.tmp.pop(0)
                print(f"DISCARD: {firt}")
                del(self.cache_data[firt])

    def get(self, key):
        """BaseCaching Caching System"""
        if key is not None:
            for k, v in self.cache_data.items():
                if k == key:
                    return v
        return None
