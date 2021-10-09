MOD = 998244353


def test():
    from main.combination import create_modC
    from main.combination import modCall

    def _test(n):
        expected = modCall(n, MOD)
        modC = create_modC(n, MOD)
        for i, e in zip(range(0, n + 1), expected):
            result = modC(i)
            print(f"{n}C{i} result:{result} : expected:{e}")
            assert result == e

    for n in range(3, 9):
        _test(n)


def test__combination():
    from main.combination import modCall

    expected = [
        (0,),
        (1, 1),
        (1, 2, 1),
        (1, 3, 3, 1),
        (1, 4, 6, 4, 1),
        (1, 5, 10, 10, 5, 1),
        (1, 6, 15, 20, 15, 6, 1),
    ]

    def _test(n):
        result = tuple(modCall(n, MOD))
        e = expected[n]
        print(f"{n}: result:{result} expected:{e}")
        assert result == e

    for i in range(1, 7):
        _test(i)
