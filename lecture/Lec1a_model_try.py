def model_try(good_enough, improve):
    # 这是一个公共的模式
    def func_try(guess, x):
        if good_enough(guess, x):
            return guess
        else:
            return func_try(improve(guess, x), x)
    return func_try


def sqrt(x):
    begin = 1
    tolerance = 0.001

    def good_enough(guess, x):
        return abs(guess * guess - x) < tolerance

    def improve(guess, x):
        return (guess + x / guess) / 2

    return model_try(good_enough, improve)(begin, x)


def main():
    print(sqrt(25))


if __name__ == '__main__':
    main()
