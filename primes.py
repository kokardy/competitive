
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
    prime_test(1000)

if __name__ == '__main__':
    test()