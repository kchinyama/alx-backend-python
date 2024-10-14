#!/usr/bin/env python3

"""demo script that imports wait_random, span it n times
with the psecified delay max_delay
list returned must be ascending
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return list of floats in ascending order"""

    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        # Insert delay in the correct position to maintain ascending order
        for i, existing_delay in enumerate(delays):
            if delay < existing_delay:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    return delays
