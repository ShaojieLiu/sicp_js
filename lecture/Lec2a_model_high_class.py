
def close_enough(old, new):
    return abs(old - new) < 0.001


def fixed_point(f, start):
    # 这个方法来计算不动点:
    # 思路就是不断把得数带入自变量里
    # 前提条件是 这个过程 是收敛的
    def iter(old, new):
        if close_enough(old, new):
            return new
        else:
            return iter(new, f(new))
    return iter(start, f(start))


def sqrt(x):
    # 这个 f 求不动点过程就是收敛的
    # def f(y):
    #     return (y + x / y) / 2
    # return fixed_point(f, 1)
    # 下面这个写法与上3行等价, 但更简洁
    return fixed_point(lambda y: (y + x / y) / 2, 1)


def average_damp(f):
    # 于是用 平均阻尼函数来确保 它 收敛
    return lambda x: (f(x) + x) / 2


def sqrt1(x):
    # 但是有一些函数 求不动点时 不收敛
    return fixed_point(average_damp(lambda y: x / y), 1)


def main():
    print(sqrt(121))
    print(sqrt1(121))


if __name__ == '__main__':
    main()