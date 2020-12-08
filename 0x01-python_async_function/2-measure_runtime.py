#!/usr/bin/env python3

"""Asynchronous Coroutine Funtion"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Asynchronous Coroutine Funtion"""
    pro = time.time()
    asyncio.run(wait_n(n, max_delay))
    return time.time() - pro / n
