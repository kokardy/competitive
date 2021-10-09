# encoding: utf-8
from typing import Callable
from typing import List
import math


def mod_factorial(mod: int) -> Callable[[int], int]:
    cache: List[int] = [1, 1, 2]

    def _factorial(n: int):
        if n == 0:
            return 1
        length = len(cache)
        v = cache[-1]
        while n >= length:
            v *= length
            v %= mod
            cache.append(v)
            length += 1
        return cache[n]

    return _factorial
