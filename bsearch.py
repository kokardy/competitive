def bsearch(bot: int, top: int, f):
    """
    一般化二分探索関数

    Parameters
    ------------------
    bot : int 
        f(bot) = True になる値の初期値
    top : int
        f(bot) = False になる値の初期値
    f : function(int) -> bool
        求めたい境界で、f(bot)=True, f(top)=False になる関数

    Returns
    ----------------------
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

def bsearch_float(bot: float, top: float, diff: float, f):
    """
    一般化二分探索関数 float版

    Parameters
    ------------------
    bot : float 
        f(bot) = True になる値の初期値
    top : float
        f(bot) = False になる値の初期値
    diff : float
        終了条件 top - bot < diff
    f : function(float) -> bool
        求めたい境界で、f(bot)=True, f(top)=False になる関数

    Returns
    ----------------------
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

    return bot, top



def main():
    bot = 1
    top = 10 ** 100

    f = lambda x: x < 39098

    m1, m2 = bsearch(bot, top, f)

    print(m1, m2)

    m1, m2 = bsearch_float(1.0, 10000.3, 0.00001, lambda x: x < 399.9)

    print(m1, m2)


if __name__ == "__main__":
    main()