#!/usr/bin/env python3
""" Redis exercise """
import redis
import uuid
from typing import Callable, Union


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

    def get(self, key: str, fn: Callable) -> Union[str, bytes, int, float]:
        """Gets a value from Redis storage"""
        val = self._redis.get(key)
        return fn(val) if fn is not None else val

    def get_str(self, key: str) -> str:
        """Gets a string from Redis storage"""
        val = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Gets an int from Redis storage"""
        val = self._redis.get(key)
        return int(val)
