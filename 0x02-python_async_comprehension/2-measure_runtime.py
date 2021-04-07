#!/usr/bin/env python3
"""2-Run time for four parallel comprehensions."""
import asyncio
import random
from typing import List
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it."""
    funtion = []
    start = time.time()
    for i in range(4):
        funtion.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*funtion)
    return time.time() - start