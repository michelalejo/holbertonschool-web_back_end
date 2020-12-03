#!/usr/bin/env python3

"""Asynchronous Coroutine Funtion"""
import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous Coroutine Funtion"""
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n

