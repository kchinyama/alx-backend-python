#!/usr/bin/env python3

"""demo of comprehension from a comprehended function
"""

import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """function creates new float list from async_generator function
    """

    new_floats = [floats async for floats in async_generator()]
    return new_floats
