"""UnionFind test"""

from src.unionfind import UnionFind

unions1 = [1, 2, 3, 4, 9]
unions6 = [6, 5, 8]


class TestUnionFind:
    """UnionFind test"""

    def test_unionfind(self) -> None:
        """UnionFind test"""
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
