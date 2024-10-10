#!/usr/bin/env python3

"""demo of type annotations using any
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of all parameters"""
    return sum(mxd_lst)