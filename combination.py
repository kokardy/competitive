
MOD = 998244353
import numpy as np
def modC(n, mod):
    result = np.array(np.zeros(n+1), dtype=np.int64)
    result[-1] = 1
    result[-2] = 1

    while result[0] == 0:
        result = result  + np.roll(result, -1)

    return result

def test():
    n = 10
    for i in range(2, n):
        result = modC(i, MOD)
        print(f"i={i} {result}")
    
    n = 2500
    result= modC(n, MOD)
    print(f"i={n} {result}")
if __name__ == '__main__':
    test()