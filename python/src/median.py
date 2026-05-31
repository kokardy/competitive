"""高速な中央値の計算を行うためのクイックセレクションアルゴリズム"""

import random
from typing import Protocol, Self


class Comparable(Protocol):
    """比較演算が可能なオブジェクトを表すプロトコル。"""

    def __lt__(self, other: Self, /) -> bool:
        """Less than."""
        ...

    def __le__(self, other: Self, /) -> bool:
        """Less than or equal to."""
        ...

    def __gt__(self, other: Self, /) -> bool:
        """Greater than."""
        ...

    def __ge__(self, other: Self, /) -> bool:
        """Greater than or equal to."""
        ...


def _quick_selection[T: Comparable](
    items: list[T],
    pivot: T,
) -> tuple[list[T], list[T], list[T]]:
    """
    値をピボットに基づいて3つのグループ（未満、等しい、超える）に分割する。

    Args:
        items: 分割対象の要素リスト。
        pivot: 基準となる値。

    Returns:
        (未満のリスト, 等しいリスト, 超えるのリスト) のタプル。

    """
    less = []
    equal = []
    greater = []

    for item in items:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)
        else:
            equal.append(item)

    return less, equal, greater


def _select[T: Comparable](items: list[T], k: int) -> T:
    """
    k番目に小さい要素を選択する（0-indexed）。

    Args:
        items: 要素リスト。
        k: 選択したい要素のインデックス。

    Returns:
        k番目に小さい要素。

    Raises:
        ValueError: リストが空の場合。

    """
    if not items:
        raise ValueError("List is empty")

    # ピボットをランダムに選択（最悪計算量を防ぐため）
    pivot = items[random.randint(0, len(items) - 1)]
    less, equal, greater = _quick_selection(items, pivot)

    if k < len(less):
        return _select(less, k)
    elif k < len(less) + len(equal):
        return pivot
    else:
        return _select(greater, k - len(less) - len(equal))


def median[T: Comparable](items: list[T]) -> T:
    """
    リストの中央値を計算する。

    要素数が偶数の場合は、中央の2つのうち大きい方の値を返す。
    計算量は平均 O(N)、最悪 O(N^2)。ランダムピボットにより最悪ケースを回避する。

    Args:
        items: 比較可能な要素のリスト。

    Returns:
        リストの中央値。

    Raises:
        ValueError: リストが空の場合。

    """
    if not items:
        raise ValueError("Cannot calculate median of an empty list.")

    return _select(items, len(items) // 2)
