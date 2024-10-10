#!/usr/bin/env python3

"""demo of the use of sequence in type annotation
"""

from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Sequence) -> Iterable[Tuple[int]]:
    """returns the type of each variable in the list"""

    return [(i, len(i)) for i in lst]
