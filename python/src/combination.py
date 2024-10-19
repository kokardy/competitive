"""Combination functions"""

from typing import Callable, Iterable, List

import numpy as np


def create_mod_combinations(n: int, mod: int) -> Callable[[int], int]:
    """Create function: function(r) -> nCr % mod"""
    fac: List[int] = [1]
    inv: List[int] = [1]
    for i in range(1, n + 1):
        _fac = (fac[-1] * i) % mod
        _inv = pow(_fac, -1, mod)
        fac.append(_fac)
        inv.append(_inv)

    def _mod_combinations(r):
        result = fac[n] * inv[n - r]
        result %= mod
        result *= inv[r]
        result %= mod
        return result

    return _mod_combinations


def mod_combination_all(n: int, mod: int) -> Iterable[int]:
    """Return [nC0, nC1, nC2, ..., nCn]"""
    result = np.array(np.zeros(n + 1), dtype="int64")
    result[-1] = 1
    result[-2] = 1

    while result[0] == 0:
        result = result + np.roll(result, -1)
        result %= mod
    return tuple(result)
