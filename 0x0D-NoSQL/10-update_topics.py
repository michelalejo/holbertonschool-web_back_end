#!/usr/bin/env python3
"""
    Python function
"""


def update_topics(mongo_collection, name, topics):
    """Changes topic of a school document based on name"""
    return mongo_collection.update_many({
        "name": name},
        {"$set": {"topics": topics}}
    )
