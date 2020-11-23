#!/usr/bin/env python3

"""Type-Annotated Function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Type-Annotated Function"""
    return k, v * v
