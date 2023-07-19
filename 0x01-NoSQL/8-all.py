#!/usr/bin/env python3
"""a Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    if mongo_collection.count == 0:
        return
    return list(mongo_collection.find())
