"""BIT(Binary Indexed Tree)"""

from typing import Callable


class BIT:
    """Binary Indexed Tree"""

    def __init__(self, n: int, operator: Callable[[int, int], int], zero):
        """Initialize"""
        self.n = n
        self.operator = operator
        self.zero = zero
        self.tree = [zero] * (n + 1)

    def update(self, i: int, x: int) -> None:
        """Update"""
        while i <= self.n:
            self.tree[i] = self.operator(self.tree[i], x)
            i += i & -i

    def value(self, i: int) -> int:
        """Return value"""
        s = self.zero
        while i > 0:
            s = self.operator(s, self.tree[i])
            i -= i & -i
        return s
