"""BIT(Binary Indexed Tree)"""

from typing import Callable


class BIT[T]:
    """Binary Indexed Tree"""

    def __init__(self, n: int, operator: Callable[[T, T], T], zero: T) -> None:
        """
        Initialize

        Args:
        ----
            n (int): Number of elements
            operator (Callable[[int, int], int]): Operator
            zero(T): Zero element
        """
        self.n = n
        self.operator = operator
        self.zero = zero
        self.tree = [zero for _ in range(n + 1)]

    def update(self, i: int, x: T) -> None:
        """
        Update

        Args:
        ----
            i (int): Index
            x (T): Value

        """
        while i <= self.n:
            self.tree[i] = self.operator(self.tree[i], x)
            i += i & -i

    def value(self, i: int) -> T:
        """
        Return value

        Args:
        ----
            i (int): Index
        """
        s = self.zero
        while i > 0:
            s = self.operator(s, self.tree[i])
            i -= i & -i
        return s
