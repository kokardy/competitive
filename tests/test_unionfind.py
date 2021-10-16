from main.unionfind import UnionFind
import pytest


unions1 = [1, 2, 3, 4, 9]
unions6 = [6, 5, 8]

class TestUnionFind:
    def test_unionfind(self):
        union = UnionFind(100)

        for u in unions1:
            union.merge(1, u)

        for u in unions6:
            union.merge(6, u)

        for u in unions1:
            assert union.same(1, u)

        for u in unions6:
            assert union.same(6, u)

        for u in unions1:
            assert not union.same(6, u)
