#!/usr/bin/env python3

"""demo of an async coroutine that retunrs random number
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """function returns random number, incl float"""

    my_float = (random.uniform(0, max_delay))
    await asyncio.sleep(my_float)
    return my_float
