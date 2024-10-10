#!/usr/bin/env python3

"""demo of callable in type annotation
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns function that multiplies floats"""

    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
