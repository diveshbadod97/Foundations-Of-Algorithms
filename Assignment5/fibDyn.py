def fibDyn(n):
    """
    Fibonacci Sequence with dynamic programming
    :param n: Till what number you want the sequence
    :return: Return teh value of the sequence at that number
    """
    a = {}
    if n < 2:
        a[n] = n
        return n
    if n - 2 in a:
        fib = a[n - 2]
    else:
        a[n - 2] = fibDyn(n - 2)
        fib = a[n - 2]
    if n - 1 in a:
        fib1 = a[n - 1]
        return fib + fib1
    else:
        a[n - 1] = fibDyn(n - 1)
        fib1 = a[n - 1]
        return fib + fib1


def main():
    print(fibDyn(10))


if __name__ == '__main__':
    main()
