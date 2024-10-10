#!/usr/bin/env pyhon3

"""demo of type annotatio with tuples
"""



from typing import Union, Tuple



def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns tuple from parameters"""

    return str(k), v ** 2