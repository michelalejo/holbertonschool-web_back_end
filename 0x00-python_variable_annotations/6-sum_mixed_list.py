#!/usr/bin/env python3

"""Type-Annotated Function"""
from typing import Callable


def sum_mixed_list(mxd_lst: Callable[[float, int], float]) -> float:
    """Type-Annotated Function"""
    return sum(mxd_lst)
