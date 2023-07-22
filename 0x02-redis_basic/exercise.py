#!/usr/bin/env python3
"""Writingstrings to Redis """
import redis
import uuid
from typing import Union, Callable
import functools


def call_history(method: Callable) -> Callable:
    """ Decorator to store the history of input """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = "{}:inputs".format(method.__qualname__)
        outputs_key = "{}:outputs".format(method.__qualname__)

        self._redis.rpush(inputs_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(outputs_key, output)

        return output

    return wrapper


def replay(method: Callable):
    """ function to display the history of calls for a function"""
    inputs_key = "{}:inputs".format(method.__qualname__)
    outputs_key = "{}:outputs".format(method.__qualname__)

    inputs = method._redis.lrange(inputs_key, 0, -1)
    outputs = method._redis.lrange(outputs_key, 0, -1)

    print("{} was called {} times".format(method.__qualname__, len(inputs)))

    for inp, out in zip(inputs, outputs):
        inp_str = inp.decode("utf-8")
        out_str = out.decode("utf-8")
        print("{}(*{}) -> {}".format(method.__qualname__, inp_str, out_str))


class Cache:
    """ """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes, int, None]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)
