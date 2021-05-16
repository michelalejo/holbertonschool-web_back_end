#!/usr/bin/env python3
"""
redis.
"""
from functools import wraps
import redis
from typing import Union, Callable, Optional, Any
import uuid


def count_calls(method: Callable) -> Callable:
    """Incrementing values"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper func"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Storing lists"""
    @wraps(method)
    def wrapper(self, *args):
        """wrapper func"""
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        output = method(self, *args)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(output))
        return output
    return wrapper


def replay(fn: Callable) -> str:
    """Retrieving lists"""
    method = fn.__qualname__
    inputs = f"{method}:inputs"
    outputs = f"{method}:outputs"
    inp_list = fn.__self__._redis.lrange(inputs, 0, -1)
    out_list = fn.__self__._redis.lrange(outputs, 0, -1)
    Q = fn.__self__._redis.get(method).decode('utf-8')
    print(f"{method} was called {Q} times:")
    for inp, out in zip(inp_list, out_list):
        print(f"{method}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")


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
