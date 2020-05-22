#encoding: utf-8
import math
MOD = 998244353

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



def pow_test():
    pow2 = mod_pow(2,MOD)
    for i in range(1, 20):
        v = pow2(i)
        expected = int(math.pow(2, i))
        #print(f"2^{i}={expected}={v}")
        if v != expected:
            raise Exception(f"2^{i}={expected} but {v}")
    return print("ALL PASSED")

def pow_test2():
    pow2 = mod_pow(2, MOD)
    for i in range(1, 11):
        v = pow2(i)
        print(f"2^{i}={v}")


def modfac_test():
    mod = 998244353
    fac1 = mod_factorial(mod)
    for i in range(6):
        v1 = fac1(i)
        print(f"{i}!={v1}")


def test():
    pow_test()
    pow_test2()
    modfac_test()

if __name__ == '__main__':
    test()