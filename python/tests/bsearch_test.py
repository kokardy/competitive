def test():
    from main.bsearch import bsearch_int, bsearch_float

    bot = 1
    top = 10 ** 100

    def f(x):
        return x < 39098

    m1, m2 = bsearch_int(bot, top, f)

    print(m1, m2)
    assert m1 == 39097
    assert m2 == 39098

    m1, m2 = bsearch_float(1.0, 10000.3, 0.00001, lambda x: x < 399.9)

    print(m1, m2)
    assert m1 < 399.9
    assert m2 >= 399.9
