"""Factorial test"""

from functools import reduce

from src.factorial import mod_factorial

MOD = 998244353


def test_mod_factorial() -> None:
    """Mod factorial test"""

    def _fac(n):
        return reduce(lambda a, b: a * b, range(1, n + 1))

    fac = mod_factorial(MOD)

    # 0! == 1
    assert fac(0) == 1

    for i in range(1, 6):
        v1 = fac(i)
        v2 = _fac(i)
        print(f"{i}!={v1}")
        assert v1 == v2
