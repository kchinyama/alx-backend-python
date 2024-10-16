#!/usr/bin/env python3

"""demo of how to retunr a task object in async
"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a task object"""

    return asyncio.create_task(wait_random(max_delay))
