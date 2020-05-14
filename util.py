#encoding: utf-8

import math

def C(n, r):
    return int(factorial(n) * inverse_fac(n-r) * inverse_fac(r))

def modC(n, r, mod):
    factorial = mod_factorial(mod)
    nf = factorial(n) 
    nrf = factorial(n-r)
    rf = factorial(r)
    nr_pow = cached_pow(nrf)
    r_pow = cached_pow(rf)
    
    v = nf * nr_pow(mod-2) * r_pow(mod-2)
    print(f"DEBUG {n}C{r}={v}")
    return v % mod

def mod_factorial(mod):
    nn = [1, 2]
    def expand(n):
        while len(nn) < n:
            v = nn[-1] * (len(nn) + 1)
            v %= mod
            nn.append(v)
    def _factorial(n):
        if n == 0:
            return 1
        expand(n)
        return nn[n-1]
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

def cached_pow(x):
    xx = [1, x]
    def _pow(y, x=x):
        while len(xx) <= math.log(y, 2)+1:
            xx.append(xx[-1] * xx[-1])
            x *= x
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

    #i = 100000
    #v = pow2(i)
    #print(f"2^{i}={v}")

def fac_test():
    for i in range(6):
        v = factorial(i)
        print(f"{i}!={v}")

def comb_test():
    n = 5
    p = 23
    for i in range(n+1):
        v = C(n,i)
        v2 = modC(n, i, p)
        print(f"{n}C{i}={v} --- {v2} (mod {p})")

    n = 50000
    r = 25001
    v = modC(n, r, 10090)
    print(f"{n}C{r}={v}")


def test():
    pow_test()
    pow_test2()
    fac_test()
    comb_test()

if __name__ == '__main__':
    test()