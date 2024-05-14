#!/usr/bin/env python3
"""
Module that defines the list_all function
"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    return [d for d in mongo_collection.find()]
