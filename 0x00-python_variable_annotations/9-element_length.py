#!/usr/bin/env python3

"""Type-Annotated Function"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Type-Annotated Function"""
    return [(i, len(i)) for i in lst]
