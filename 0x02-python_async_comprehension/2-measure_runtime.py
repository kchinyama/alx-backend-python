#!/usr/bin/env python3

"""demo script that showsrun time measurement of operations
"""


import asyncio
import time

async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures the runtime of 3 asyc_comprehension operations"""

    starts = time.time()
    await asyncio.gather(async_comp(), async_comp(), async_comp())
    ends = time.time()

    run_time = ends - starts
    return run_time
