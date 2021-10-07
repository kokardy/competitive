MOD = 998244353
import math
import numpy as np


def create_modC(n, mod):
    if n == 0:
        return (lambda r: 1)
    b = int(math.log(mod-2, 2)) + 1
    fac = np.zeros((b, n+1), dtype=np.int64)
    inv = np.ones(n+1, dtype=np.int64)
    fac[0, 0], fac[0, 1] = 1, 1
    for i in range(2, n+1):
        fac[0, i] = (fac[0, i-1] * i) % mod
    for i in range(1, b):
        fac[i, :] = (fac[i-1, :] ** 2) % mod

    indice = []
    N = mod - 2
    i = 0
    while N > 0:
        if N % 2 == 1:
            indice.append(i)
        N = N >> 1
        i += 1
    
    for i in indice:
        inv *= fac[i,:]
        inv %= mod
    
    fac = fac[0,:]

    def _modC(r):
        result = fac[n] * inv[n-r]
        result %= mod
        result *= inv[r] % mod
        result %= mod
        return result

    return _modC


def test():
    n = 5
    modC = create_modC(n, MOD)
    for i in range(0, n+1):
        result = modC(i)
        print(f"i={i} {result}")
    
    n = 200000
    modC = create_modC(n, MOD)
    for r in range(n):
        if r % 10000 == 0:
            print(modC(r))

def modCall(n, mod):
    result = np.array(np.zeros(n+1), dtype=np.int64)
    result[-1] = 1
    result[-2] = 1

    while result[0] == 0:
        result = result  + np.roll(result, -1)
        result %= mod
    return result

def test1():
    n = 10
    for i in range(2, n):
        result = modCall(i, MOD)
        print(f"i={i} {result}")
    
    n = 5000
    result= modCall(n, MOD)
    print(f"i={n} {result}")

if __name__ == '__main__':
    test()