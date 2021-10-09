from main.factorial import mod_factorial

MOD = 998244353

def test__modfac():
    from functools import reduce

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
