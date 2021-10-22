# encoding:utf8


class BIT:
    def __init__(self, n, operator, zero):
        self.n = n
        self.operator = operator
        self.zero = zero
        self.tree = [zero] * (n + 1)

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
