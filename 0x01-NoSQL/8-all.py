#!/usr/bin/env python3
""" List all documents in Python """


def list_all(mongo_collection):
    """ a Python function that lists all documents in a collection"""
    if mongo_collection.count() == 0:
        return []
    return list(mongo_collection.find({}))

