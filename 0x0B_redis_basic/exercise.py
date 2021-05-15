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
