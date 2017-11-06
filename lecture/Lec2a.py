def sum_int(a, b):
    if a > b:
        return 0
    else:
        return sum_int(a + 1, b) + a


def sum_sq(a, b):
    if a > b:
        return 0
    else:
        return sum_sq(a + 1, b) + a * a


def model_sum(term, next):
    def func_sum(a, b):
        if a > b:
            return 0
        else:
            return term(a) + func_sum(next(a), b)
    return func_sum


sum_sq1 = model_sum(lambda x: x * x, lambda x: x + 1)


sum_pi = model_sum(lambda x: 1 / (x * (x + 2)), lambda x: x + 4)


def main():
    print(sum_int(1, 10))
    print(sum_sq(1, 3))
    print(sum_sq1(1, 3))
    print(sum_pi(1 , 3000) * 8)


if __name__ == '__main__':
    main()