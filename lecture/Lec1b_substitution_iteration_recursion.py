# 代换模型 substitution model


def sum1 (x, y):
    # 时间复杂度 O(x)
    # 空间复杂度 O(1)
    # 线性迭代过程 Iteration
    # 空间上不扩展, 尾递归
    if x == 0:
        return y
    else:
        return sum1(x - 1, y + 1)


def sum2 (x, y):
    # 时间复杂度 O(x)
    # 空间复杂度 O(x)
    # Recursion
    # 线性递归函数(时间和空间复杂度是 x 的一次)
    if x == 0:
        return y
    else:
        return 1 + sum2(x - 1, y)


def sos (x, y):
    # sum of square
    return x * x + y * y


def main():
    print(sos(3, 4))
    print(sum1(5, 7))
    print(sum2(5, 7))


if __name__ == '__main__':
    main()