"""Combination test"""

from src.combination import create_mod_combinations, mod_combination_all

MOD = 998244353


def test() -> None:
    """Mod combination test"""

    def _test(n) -> None:
        expected = mod_combination_all(n, MOD)
        mod_combinations = create_mod_combinations(n, MOD)
        for i, e in zip(range(0, n + 1), expected):
            result = mod_combinations(i)
            print(f"{n}C{i} result:{result} : expected:{e}")
            assert result == e

    for n in range(3, 9):
        _test(n)


def test_combination() -> None:
    """Combination test"""
    expected = [
        (0,),
        (1, 1),
        (1, 2, 1),
        (1, 3, 3, 1),
        (1, 4, 6, 4, 1),
        (1, 5, 10, 10, 5, 1),
        (1, 6, 15, 20, 15, 6, 1),
    ]

    print("")

    def _test(n) -> None:
        result = tuple(mod_combination_all(n, MOD))
        e = expected[n]
        print(f"{n}: result:{result} expected:{e}")
        assert result == e

    for i in range(1, 7):
        _test(i)
