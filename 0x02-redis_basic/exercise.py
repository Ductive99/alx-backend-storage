#!/usr/bin/env python3
""" Redis exercise """
import redis
import uuid
from typing import Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Counts the number of Cache methods are called """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Stores the history of inputs and outputs for a function """
    inputKey = method.__qualname__ + ":input"
    outputKey = method.__qualname__ + ":output"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        self._redis.rpush(inputKey, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputKey, output)
        return output

    return wrapper


def replay(fn: Callable) -> None:
    """ Displays the history of calls of a function """
    r = redis.Redis()
    fname = fn.__qualname__
    val = r.get(fname)
    try:
        val = int(val.decode("utf-8"))
    except Exception:
        value = 0

    print("{} was called {} times:".format(fname, val))
    inputs = r.lrange("{}:inputs".format(fname), 0, -1)
    outputs = r.lrange("{}:outputs".format(fname), 0, -1)

    for input_data, output in zip(inputs, outputs):
        try:
            input_data = input_data.decode("utf-8")
        except Exception:
            input_data = ""

        try:
            output = output.decode("utf-8")
        except Exception:
            output = ""

        print(f"{fname}(*{input_data}) -> {output}")


class Cache:
    """ Stores data using Redis """

    def __init__(self) -> None:
        """Initiliazation"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Storage"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """Gets a value from Redis storage"""
        val = self._redis.get(key)
        return fn(val) if fn is not None else val

    def get_str(self, key: str) -> str:
        """Gets a string from Redis storage"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Gets an int from Redis storage"""
        return self.get(key, lambda x: int(x))
