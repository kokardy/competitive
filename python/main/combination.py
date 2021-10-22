from typing import Callable, Iterable


def create_mod_combinations(n: int, mod: int) -> Callable[[int], int]:
    """create function: function(r) -> nCr % mod"""
    import math
    import numpy as np

    if n == 0:
        return lambda r: 1
    b = int(math.log(mod - 2, 2)) + 1
    fac = np.zeros((b, n + 1), dtype="int64")
    inv = np.ones(n + 1, dtype="int64")
    fac[0, 0], fac[0, 1] = 1, 1
    for i in range(2, n + 1):
        fac[0, i] = (fac[0, i - 1] * i) % mod
    for i in range(1, b):
        fac[i, :] = (fac[i - 1, :] ** 2) % mod

    indice = []
    n = mod - 2
    i = 0
    while n > 0:
        if n % 2 == 1:
            indice.append(i)
        n = n >> 1
        i += 1

    for i in indice:
        inv *= fac[i, :]
        inv %= mod

    fac = fac[0, :]

    def _mod_combinations(r):
        result = fac[n] * inv[n - r]
        result %= mod
        result *= inv[r] % mod
        result %= mod
        return result

    return _mod_combinations


def mod_combination_all(n: int, mod: int) -> Iterable[int]:
    """return [nC0, nC1, nC2, ..., nCn]"""
    import numpy as np

    result = np.array(np.zeros(n + 1), dtype="int64")
    result[-1] = 1
    result[-2] = 1

    while result[0] == 0:
        result = result + np.roll(result, -1)
        result %= mod
    return tuple(result)
