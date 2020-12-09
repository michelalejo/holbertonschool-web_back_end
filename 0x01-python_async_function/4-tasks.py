#!/usr/bin/env python3

"""Asynchronous Coroutine Funtion"""
import random
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous Coroutine Funtion"""
    l: List[float] = [await task_wait_random(max_delay) for i in range(n)]
    return sorted(l)
