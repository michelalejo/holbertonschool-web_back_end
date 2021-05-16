#!/usr/bin/env python3
"""Track how many times a particular URL was accessed."""
from exercise import count_calls
from redis.client import Redis
import requests


redis = Redis()
count = 0



def get_page(url: str) -> str:
    """Track how many times a particular URL was accessed."""
    data = f"count:{url}"
    count += 1
    redis.set(data, count)
    res = requests.get(url)
    redis.incr(data)
    redis.setex(data, 10, redis.get(data))
    return res.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
