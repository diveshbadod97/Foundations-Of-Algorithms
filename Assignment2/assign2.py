def representingL(A, B):
    # This is the representation of L from the homework
    # which will be later used to calculate Fibonacci sequence in O(log n) complexity
    a = (A[0][0] * B[0][0]) + (A[0][1] * B[1][0])
    b = (A[0][0] * B[0][1]) + (A[0][1] * B[1][1])
    c = (A[1][0] * B[0][0]) + (A[1][1] * B[1][0])
    d = (A[1][0] * B[0][1]) + (A[1][1] * B[1][1])
    A[0][0] = a
    A[0][1] = b
    A[1][0] = c
    A[1][1] = d


def Pow(A, n):
    if n == 0 or n == 1:
        return
    Pow(A, n // 2)
    representingL(A, A)
    B = [[1, 1], [1, 0]]
    if n % 2 != 0:
        representingL(A, B)


def fibPow(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        A = [[1, 1], [1, 0]]
        Pow(A, n - 1)
        return A[0][0]


def main():
    print(fibPow(28))


if __name__ == '__main__':
    main()
