# encoding:utf8

class BIT:

    def __init__(self, n, operator, zero):
        self.n = n
        self.operator = operator
        self.zero = zero
        self.tree = [zero] * (n+1)

    def update(self, i, x):
        while i <= self.n:
            self.tree[i] = self.operator(self.tree[i], x)
            i += i & -i

    def value(self, i):
        s = self.zero
        while i > 0:
            s = self.operator(s, self.tree[i])
            i -= i & -i
        return s

def test():
    bit = BIT(10, int.__add__, 0)
    bit.update(2, 10)
    bit.update(5, 5)
    print(bit.value(3))
    print(bit.value(6))
    bit.update(3, -6)
    print(bit.value(6))
    print(bit.value(6) - bit.value(3))

def test2():
    bit = BIT(10, int.__mul__, 1)
    bit.update(2, 10)
    bit.update(5, 5)
    print(bit.value(3))
    print(bit.value(6))
    bit.update(3, -6)
    print(bit.value(6))
    print(bit.value(6) - bit.value(3))


def main():
    test()
    test2()

if __name__ == "__main__":
    main()