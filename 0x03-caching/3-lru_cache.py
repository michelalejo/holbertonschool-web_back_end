#!/usr/bin/env python3
"""BaseCaching Caching System"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """BaseCaching Caching System"""

    def __init__(self) -> None:
        """BaseCaching Caching System"""
        super().__init__()

    def put(self, key, item):
        """BaseCaching Caching System"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                firt = list(self.cache_data.keys())[0]
                print(f"DISCARD: {firt}")
                del(self.cache_data[firt])

    def get(self, key):
        """BaseCaching Caching System"""
        if key is not None:
            for k, v in self.cache_data.items():
                if k == key:
                    return v
        return None
