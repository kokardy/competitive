"""UnionFind"""


class UnionFind:
    """UnionFind class"""

    def __init__(self, n: int) -> None:
        """Initialize"""
        self.n = n
        self.parent = list(range(n))
        self.group = [set([i]) for i in range(n)]

    def par(self, m: int) -> int:
        """Return parent"""
        if self.parent[m] == m:
            return m
        else:
            _par = self.par(self.parent[m])
            self.parent[m] = _par
            return _par

    def same(self, m1: int, m2: int) -> bool:
        """Return if m1 and m2 are in the same group"""
        return self.par(m1) == self.par(m2)

    def merge(self, m1: int, m2: int) -> None:
        """Merge m1 and m2"""
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

    def member(self, m) -> set[int]:
        """Return the group of m"""
        _par = self.par(m)
        return self.group[_par]
