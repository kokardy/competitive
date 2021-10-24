from competitive.primes import primes, prime_factorization


def test__primes():
    n = 20
    print("prime:", end="")
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    for i, ans in zip(primes(n), expected):
        print(f"{i}", end=", ")
        assert i == ans

    print("")


def test__prime_factorization():
    n = 13 * 17 * 11 * 11
    pf = prime_factorization(n)
    ans = {13: 1, 17: 1, 11: 2}
    assert pf == ans
