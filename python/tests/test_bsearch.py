"""Binary search test"""

from src.bsearch import bsearch_float, bsearch_int


def test_bsearch_int() -> None:
    """Binary search test"""
    bot = 1
    top = 10**100

    def f(x):
        return x < 39098

    m1, m2 = bsearch_int(bot, top, f)

    print(m1, m2)
    assert m1 == 39097
    assert m2 == 39098


def test_bsearch_float() -> None:
    """Binary search test"""
    bot = 1.0
    top = 10000.3
    diff = 0.00001

    def f(x):
        return x < 39098

    m1, m2 = bsearch_float(bot, top, diff, lambda x: x < 399.9)

    print(m1, m2)
    assert m1 < 399.9
    assert m2 >= 399.9
