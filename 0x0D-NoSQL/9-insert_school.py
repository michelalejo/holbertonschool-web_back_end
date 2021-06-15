#!/usr/bin/env python3
"""
    Python function
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert new document on a collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
