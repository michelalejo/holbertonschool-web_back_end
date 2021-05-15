#!/usr/bin/env python3
"""
redis.
"""
from functools import wraps
from redis.client import Redis
from typing import Union, Callable, Optional, Any
import uuid


class Cache:
    """Cache Class."""

    def __init__(self):
        """__Init__."""
        self.__redis = Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string."""
        data = str(uuid.uuid4())
        self.__redis.set(data, data)
        return data

    def get(self, data: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """take a key string argument and
        an optional Callable argument named fn."""
        if data:
            res = self.__redis.get(data)
            if fn:
                return fn(res)
            else:
                return res
