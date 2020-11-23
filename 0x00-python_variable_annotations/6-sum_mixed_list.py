#!/usr/bin/env python3

"""Type-Annotated Function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Type-Annotated Function"""
    return sum(mxd_lst)
