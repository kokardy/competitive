def prime_factorization(n):
    result = dict()
    tmp = n
    for p in primes(n):
        while tmp % p == 0:
            result[p] = result.get(p, 0) + 1
            tmp /= p

    return result


# slow
def primes2(n):
    yield 2
    import numpy as np

    nn = (n // 3) + 1
    a = np.arange(1, nn + 1)
    b = a * a.reshape((nn, 1))
    b = b[1:, 1:]
    c = b.reshape(
        (nn - 1) * (nn - 1),
    )
    notprimes = set(c)
    for p in range(3, n + 1, 2):
        if p not in notprimes:
            yield p


# faster than primes2
def primes(n):
    import numpy as np

    numbers = np.full(n + 1, True, dtype=np.bool)

    numbers[0] = False
    numbers[1] = False

    for k in range(1, n + 1):
        if not numbers[k]:
            continue
        yield k
        i = 1
        while k * i < n:
            ki = k * i
            numbers[ki] = False
            i += 1

