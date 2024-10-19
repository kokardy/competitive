"""Binary search functions"""

from typing import Callable, Tuple

type number = int | float


def bsearch_int(bot: int, top: int, f: Callable[[int], bool]) -> Tuple[int, int]:
    """
    一般化二分探索関数

    Parameters
    ----------
    bot : int
        f(bot) = True になる値の初期値
    top : int
        f(bot) = False になる値の初期値
    f : function(int) -> bool
        求めたい境界で、f(bot)=True, f(top)=False になる関数

    Returns
    -------
    m1 : int
        境界の下側 f(m1) = True
    m2 : int
        境界の上側 f(m2) = False

    """
    while top - bot > 1:
        mid = (bot + top) // 2
        if not f(mid):
            top = mid
        else:
            bot = mid

    return bot, top


def bsearch_float(bot: float, top: float, diff: float, f: Callable[[float], bool]) -> Tuple[float, float]:
    """
    一般化二分探索関数 float版

    Parameters
    ----------
    bot : float
        f(bot) = True になる値の初期値
    top : float
        f(bot) = False になる値の初期値
    diff : float
        終了条件 top - bot < diff
    f : function(float) -> bool
        求めたい境界で、f(bot)=True, f(top)=False になる関数

    Returns
    -------
    m1 : float
        境界の下側 f(m1) = True
    m2 : float
        境界の上側 f(m2) = False

    """
    while top - bot >= diff:
        mid = (bot + top) / 2
        if not f(mid):
            top = mid
        else:
            bot = mid

    return (bot, top)


def bsearch(
    bot: number,
    top: number,
    f,
    middle_func=lambda x, y: (x + y) // 2,
    accuracy=1,
):
    """一般化二分探索関数"""
    while top - bot > accuracy:
        mid = middle_func(bot, top)
        if f(mid):
            bot = mid
        else:
            top = mid

    return bot, top
