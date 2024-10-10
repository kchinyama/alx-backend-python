#!/usr/bin/env python3

"""demo of type annotation with lists
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes floats and returns sum of floats"""
    return sum(input_list)