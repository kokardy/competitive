
def primes2(n):
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

def primes(n):
    import numpy as np
    numbers = np.full(n, True, dtype=np.bool)

    numbers[0] = False
    numbers[1] = False

    for k in range(1, n):
        if not numbers[k]:
            continue
        yield k
        i = 1
        while k * i < n: 
            ki = k*i
            numbers[ki] = False
            i += 1

def prime_test(n):
    print("prime:", end="")
    for i in primes(n):
        print(f"{i}", end=", ") 
    print("")
        
    
def prime_test2(n):
    for i, j in zip(primes(n), primes2(n)):
        if i != j:
            raise Exception(f"i={i} j={j}")
    print("PASS TEST")

def test():
    prime_test(1000)
    prime_test2(1000)
    

if __name__ == '__main__':
    test()