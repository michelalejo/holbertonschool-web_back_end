#!/usr/bin/env python3

"""Type-Annotated Function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Type-Annotated Function"""
    def func(float: float):
        """Type-Annotated Function"""
        return float * multiplier
    return func
