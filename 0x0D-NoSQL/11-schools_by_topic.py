#!/usr/bin/env python3
"""
    Python function
"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of school with a specific topic"""
    return mongo_collection.find({"topics": topic})
