#!/usr/bin/env python3

"""Type-Annotated Function"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Type-Annotated Function"""
    if lst:
        return lst[0]
    else:
        return None
