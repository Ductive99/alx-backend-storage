#!/usr/bin/env python3
""" Redis exercise """
import redis
import uuid
from typing import Union

class Cache:
    """ Stores data using Redis """

    def __init__(self) -> None:
        """Initiliazation"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Storage"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
