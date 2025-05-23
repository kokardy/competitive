"""Prime number related functions"""

import math
import numpy as np
from typing import Dict, Generator


def prime_factorization(n: int) -> Dict[int, int]:
    """Prime factorization"""
    result: Dict[int, int] = dict()
    tmp: int = n
    for p in primes(int(math.sqrt(n))):
        while tmp % p == 0:
            result[p] = result.get(p, 0) + 1
            tmp //= p

    if not result:
        result[n] = 1
    return result


# slow
def primes2(n: int) -> Generator[int, None, None]:
    """Slow prime generator"""
    yield 2

    nn = (n // 3) + 1
    a = np.arange(1, nn + 1)
    b = a * a.reshape((nn, 1))
    b = b[1:, 1:]
    c = b.reshape(
        (nn - 1) * (nn - 1),
    )
    not_primes = set(c)
    for p in range(3, n + 1, 2):
        if p not in not_primes:
            yield p


# faster than primes2
def primes(n: int) -> Generator[int, None, None]:
    """Fast prime generator"""

    numbers = np.full(n + 1, True, dtype="bool")

    numbers[0] = False
    numbers[1] = False

    for k in range(1, n + 1):
        if not numbers[k]:
            continue
        yield k
        i = 1
        while k * i < n:
            ki = k * i
            numbers[ki] = False
            i += 1
