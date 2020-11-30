def fib(n):
    """
    The smallest number on which this function works slowly is 28
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibItHelper(n, a, b):
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return fibItHelper(n - 1, b, a + b)


def fibIt(n):
    """
    This function doesn't run slowly on the number for which the fib function works slowly
    """
    return fibItHelper(n, 0, 1)


def main():
    print(fib(28))
    print(fibIt(28))


if __name__ == '__main__':
    main()
