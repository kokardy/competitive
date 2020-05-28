import math
mod = 998244353

import numpy as np
def create_modC(n, mod):
    if n == 0:
        return (lambda r: 1)
    b = int(math.log(mod-2, 2)) + 1
    fac = np.zeros((b, n+1), dtype=np.int64)
    #print(fac.shape)
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
        if r == 0 or r == n:
            return 1
        result = fac[n] * inv[n-r]
        result %= mod
        result *= inv[r] % mod
        result %= mod
        return result

    return _modC


def mod_factorial(mod):
    cache = [1,1,2]
    def _factorial(n):
        nonlocal cache
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

def test():
    N, M, K = 3,2,1
    answer = 6
    v = resolve(N, M, K)
    print(f"N={N} M={M} K={K} {v}={answer}")
    N, M, K = 100,100,0
    answer = 73074801
    v = resolve(N, M, K)
    print(f"N={N} M={M} K={K} {v}={answer}")
    N, M, K = 60522,114575,7559
    answer = 479519525
    v = resolve(N, M, K)
    print(f"N={N} M={M} K={K} {v}={answer}")

    N, M, K = 200000,190000,190000
    v = resolve(N, M, K)
    print(f"N={N} M={M} K={K} {v}")

    N, M, K = 1,1,0
    print(f"N={N} M={M} K={K}")
    v = resolve(N, M, K)
    print(f"N={N} M={M} K={K} {v}")

    N, M, K = 200000,200000,190000
    v = resolve(N, M, K)
    print(f"N={N} M={M} K={K} {v}")

    for _ in range(100):
        N, M = np.random.randint(200000), np.random.randint(200000)
        K = np.random.randint(N-1)
        v = resolve(N, M, K)
        print(f"N={N} M={M} K={K} {v}")




def main():
    #test()
    N, M, K = map(int, input().split())
    v = resolve(N, M, K)
    print(v)


def resolve(N, M, K):
    from datetime import datetime
    result = 0
    m1pow = mod_pow(M-1, mod)
    modC = create_modC(N-1, mod)
    
    for k in range(K+1):
        b = m1pow(N-1-k)
        c = modC(k)
        v = b 
        v *= c
        v %= mod
        #if k < 10:
        #    print(f"b={b} c={c} k={k} {v}")
        result += v
        result %= mod
    
    result *= M
    result %= mod

    result = int(result)

    return result

        
if __name__ == '__main__':
    main()