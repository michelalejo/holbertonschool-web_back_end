#!/usr/bin/env python3
"""1-Async Comprehensions."""
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Import async_generator from the previous task and then write a coroutine
    called async_comprehension that takes no arguments.
    The coroutine will collect 10 random numbers using async comprehensing over
    async_generator, then return the 10 random numbers."""
    return [result async for result in async_generator()]
