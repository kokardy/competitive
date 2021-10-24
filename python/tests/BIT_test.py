def test_plus():
    print("plus BIT")
    from competitive.BIT import BIT

    n = 10
    bit = BIT(n, lambda x, y: x + y, 0)

    def _test(x, y):
        print(f"{x} => {y}")
        bit.update(x, y)
        for i in range(n):
            print(f"{i}:{bit.value(i):02}", end=" ")
        print()

    x, y = 2, 10
    _test(x, y)

    x, y = 5, 5
    _test(x, y)

    x, y = 3, -6
    _test(x, y)

    assert bit.value(9) == 9
    assert bit.value(0) == 0


def test_mul():
    print("mul BIT")
    from competitive.BIT import BIT

    n = 10
    bit = BIT(n, lambda x, y: x * y, 1)

    def _test(x, y):
        print(f"{x} => {y}")
        bit.update(x, y)
        for i in range(n):
            print(f"{i}:{bit.value(i):02}", end=" ")
        print()

    x, y = 2, 3
    _test(x, y)
    x, y = 5, 7
    _test(x, y)
    x, y = 8, -2
    _test(x, y)

    assert bit.value(0) == 1
    assert bit.value(2) == 3
    assert bit.value(9) == -42
