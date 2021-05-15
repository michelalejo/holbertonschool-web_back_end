#!/usr/bin/env python3
"""
redis.
"""
from functools import wraps
import redis
from typing import Union, Callable, Optional, Any
import uuid


class Cache:
    """Cache Class."""

    def __init__(self):
        """__Init__."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string."""
        uid = str(uuid.uuid4())
        self._redis.set(uid, data)
        return uid

    def get(self, data: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """take a key string argument and
        an optional Callable argument named fn."""
        if data:
            res = self._redis.get(data)
            if fn:
                return fn(res)
            else:
                return res
    
    def get_str(self, data: bytes) -> str:
        """Automatically parametrize Cache.get with
        the correct conversion function."""
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """Automatically parametrize Cache.get with
        the correct conversion function."""
        return int(data)
