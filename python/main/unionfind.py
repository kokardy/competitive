class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.group = [set([i]) for i in range(n)]

    def par(self, m):
        if self.parent[m] == m:
            return m
        else:
            _par = self.par(self.parent[m])
            self.parent[m] = _par
            return _par

    def same(self, m1, m2):
        return self.par(m1) == self.par(m2)

    def merge(self, m1, m2):
        m1 = self.par(m1)
        m2 = self.par(m2)
        m1_length = len(self.group[m1])
        m2_length = len(self.group[m2])
        if m1_length > m2_length:
            _group = self.member(m1)
            self.parent[m1] = m2
            self.group[m2] |= _group
        else:
            _group = self.member(m2)
            self.parent[m2] = m1
            self.group[m1] |= _group

    def member(self, m):
        _par = self.par(m)
        return self.group[_par]
