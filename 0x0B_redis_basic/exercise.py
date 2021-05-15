#!/usr/bin/env python3
"""
redis.
"""
from functools import wraps
from redis.client import Redis
from typing import Union, Callable, Optional, Any
import uuid


class Cache:
    """method that takes a data argument and returns a string."""

    def __init__(self):
        """constructor"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns a string"""
        data = str(uuid.uuid4())
        self._redis.set(data, data)
        return data

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
