# 斐波那契数列
# 0 1 2 3 4 5 6 7  8  9  10
# 0 1 1 2 3 5 8 13 21 34 55


def fib1(n):
    # 这是一个特别糟糕的过程, 计算过程是一棵树
    # 时间复杂度 O(fib(x))
    # 空间复杂度 O(x)
    if n < 2:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    if n < 2:
        return n
    else:
        return fib2(n - 2) * 2 + fib2(n - 3)


def main():
    print(fib1(10))
    print(fib2(4))


if __name__ == '__main__':
    main()