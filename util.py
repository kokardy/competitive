#encoding: utf-8
import math

MOD = 998244353

def C(n, r):
    return int(factorial(n) * inverse_fac(n-r) * inverse_fac(r))

def cached_modC(n, mod):
    factorial = mod_factorial(mod)
    nf = factorial(n)
    def modC(r):
        nonlocal n, mod
        nrf = factorial(n-r)
        rf = factorial(r)
        nr_pow = mod_pow(nrf, mod)
        r_pow = mod_pow(rf, mod)
        v = nf * nr_pow(mod-2) * r_pow(mod-2)
        return v % mod
    return modC

def mod_factorial(mod):
    cache = [1,1,2]
    def _factorial(n):
        if n == 0:
            return 1
        length = len(cache)
        v = cache[-1]
        while n >= length:
            v *= length 
            v %= mod
            cache.append(v)
            length +=1
        return cache[n]
    return _factorial

def cached_factorial():
    nn = [1, 2]
    inv = [1, 1/2]
    def expand(n):
        while len(nn) < n:
            nn.append(nn[-1] * (len(nn) + 1))
            inv.append(None)
            inv[-1] = 1 / nn[-1] 
        for i in range(len(nn) - 2, 0, -1):
            if inv[i]:
                break
            inv[i] = inv[i+1] * i 

    def _factorial(n):
        if n == 0:
            return 1
        expand(n)
        return nn[n-1]

    def _invfac(n):
        if n == 0:
            return 1
        expand(n)
        return inv[n-1]
        

    return _factorial, _invfac

factorial, inverse_fac = cached_factorial()

def mod_pow(x, mod):
    xx = [1, x]
    def _pow(y, x=x):
        nonlocal xx
        if y == 0:
            return 1
        while len(xx) <= math.log(y, 2)+1:
            v = xx[-1] * xx[-1]
            v %= mod
            xx.append(v)
        i = 1
        result = 1
        while y > 0:
            if y % 2 == 1:
                result *= xx[i]
                result %= mod
            y = y >> 1
            i += 1
        return result
    return _pow


def cached_pow(x):
    xx = [1, x]
    def _pow(y, x=x):
        if y == 0:
            return 1
        while len(xx) <= math.log(y, 2)+1:
            xx.append(xx[-1] * xx[-1])
        i = 1
        result = 1
        while y > 0:
            if y % 2 == 1:
                result *= xx[i]
            y = y >> 1
            i += 1
        return result
    return _pow


def pow_test():
    pow2 = cached_pow(2)
    for i in range(1, 20):
        v = pow2(i)
        expected = int(math.pow(2, i))
        #print(f"2^{i}={expected}={v}")
        if v != expected:
            raise Exception(f"2^{i}={expected} but {v}")
    return print("ALL PASSED")

def pow_test2():
    pow2 = cached_pow(2)
    for i in range(1, 11):
        v = pow2(i)
        print(f"2^{i}={v}")

def fac_test():
    for i in range(6):
        v = factorial(i)
        print(f"{i}!={v}")

def modfac_test():
    mod = 998244353
    fac1 = mod_factorial(mod)
    for i in range(6):
        v1 = fac1(i)
        print(f"{i}!={v1}")


def comb_test():
    n = 5
    p = 23
    modC = cached_modC(n, p)
    for i in range(n+1):
        v = C(n,i)
        v2 = modC(i)
        print(f"{n}C{i}={v} --- {v2} (mod {p})")



def primes(n):
    yield 2
    import numpy as np
    nn = (n // 3) + 1
    a = np.arange(1, nn+1)
    b = a * a.reshape((nn, 1))
    b = b[1:,1:]
    c = b.reshape((nn-1)*(nn-1), )
    notprimes = set(c)
    for p in range(3, n+1, 2):
        if p not in notprimes:
            yield p
    
def prime_test(n):
    print("prime:", end="")
    for i in primes(n):
        print(f"{i}", end=", ") 
    print("")

def test():
    #pow_test()
    #pow_test2()
    fac_test()
    modfac_test()
    #comb_test()

    #n=10000
    #prime_test(n)

if __name__ == '__main__':
    test()