#!/usr/bin/env python3
"""The function should return a tuple of size two containing a start index and
an end index corresponding to the range of indexes to return in a list for
those particular pagination parameters."""


def index_range(page: int, page_size: int):
    """The function should return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a list
    for those particular pagination parameters."""
    size = page * page_size
    return (size - page_size, size)
