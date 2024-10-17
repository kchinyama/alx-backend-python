#!/usr/bin/env python3

"""demo script that imports wait_random, span it n times
with the psecified delay max_delay
list returned must be ascending
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return list of floats in ascending order"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in tasks:
        delay = await task
        # Insert delay in the correct position to maintain ascending order
        for i, existing_delay in enumerate(delays):
            if delay < existing_delay:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    return delays
