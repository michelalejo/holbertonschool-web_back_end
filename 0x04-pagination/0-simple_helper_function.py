#!/usr/bin/env python3

def index_range(page: int, page_size: int):
    size = page * page_size
    return (size - page_size, size)
