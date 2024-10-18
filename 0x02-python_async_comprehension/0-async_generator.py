#!/usr/bin/env python3

"""demo script of async generating random floats btwn 1 and 10
"""


import asyncio
import random


async def async_generator() -> float:
    """function taks no args, generates random floats"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)


async def main():
    """list comprehension of async"""

    results = [item async for item in async_generator()]

    print(results)
