"""median.py のためのテストモジュール。"""

import random
from typing import Self

import pytest

from src.median import median


class CustomInt:
    """比較演算子が定義されたカスタムクラス。テスト用。"""

    def __init__(self, value: int):
        """
        Initialize with an integer value.

        Args:
            value: The integer value to wrap.

        """
        self.value = value

    def __lt__(self, other: Self, /) -> bool:
        """Less than."""
        return self.value < other.value

    def __le__(self, other: Self, /) -> bool:
        """Less than or equal to."""
        return self.value <= other.value

    def __gt__(self, other: Self, /) -> bool:
        """Greater than."""
        return self.value > other.value

    def __ge__(self, other: Self, /) -> bool:
        """Greater than or equal to."""
        return self.value >= other.value

    def __eq__(self, other: object, /) -> bool:
        """Check for equality."""
        if not isinstance(other, CustomInt):
            return NotImplemented
        return self.value == other.value

    def __repr__(self):
        """Return representation."""
        return f"CustomInt({self.value})"


class TestMedian:
    """median 関数のテストスイート。"""

    @pytest.mark.parametrize(
        "items, expected",
        [
            # 整数
            ([3, 1, 2], 2),
            ([1, 2, 3, 4], 3),
            # 浮動小数点数 (float)
            ([1.5, 0.5, 2.5], 1.5),
            ([10.1, 5.5, 20.2, 15.0], 15.0),
            # 文字列
            (["banana", "apple", "cherry"], "banana"),
            (["d", "a", "c", "b"], "c"),
            # カスタムクラス
            ([CustomInt(3), CustomInt(1), CustomInt(2)], CustomInt(2)),
            ([CustomInt(10), CustomInt(5), CustomInt(20), CustomInt(15)], CustomInt(15)),
        ],
        ids=[
            "int_odd",
            "int_even",
            "float_odd",
            "float_even",
            "str_odd",
            "str_even",
            "custom_odd",
            "custom_even",
        ],
    )
    def test_median_types(self, items, expected):
        """様々な型に対して中央値が正しく計算されることを検証する。"""
        assert median(items) == expected

    def test_median_empty(self):
        """空のリストを渡したときに ValueError が発生することを検証する。"""
        with pytest.raises(ValueError, match="Cannot calculate median of an empty list."):
            median([])

    def test_median_randomized(self):
        """ランダムな数値リストに対して、ソート結果の中央値と一致することを検証する。"""
        for _ in range(50):
            size = random.randint(1, 50)
            items = [random.random() * 100 for _ in range(size)]
            expected = sorted(items)[len(items) // 2]
            assert median(items) == expected
