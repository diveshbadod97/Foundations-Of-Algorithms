__author__ = "Divesh Badod"


def r(xs):
    if not xs:
        return []
    return r(xs[1:]) + xs[0: 1]


def prod(m, n):
    if m == 0:
        return 0
    return prod(m - 1, n) + n


def fastPow(b, n):
    if n == 0:
        return b
    if n % 2 == 0:
        k = n // 2
        return powIt(powIt(b, 2), k)
    else:
        k = (n - 1) // 2
        return powIt(powIt(b, 2), k) * b


def prodAccum(m, n, a):
    if m == 0:
        return a
    else:
        return prodAccum(m - 1, n, n + a)


def minChange(a, ds):
    if a == 0:
        return 0
    if ds == [] and a != 0:
        return "Failure"
    if ds[0] > a:
        return minChange(a, ds[1:])
    return minimum(add(1, minChange(a - ds[0], ds)), minChange(a, ds[1:]))


def minimum(a, b):
    if a == "Failure":
        return b
    if b == "Failure":
        return a
    if a < b:
        return a
    else:
        return b


def add(a, b):
    if a == "Failure" or b == "Failure":
        return "Failure"
    else:
        return a + b


def greedyMinChange(a, ds):
    if a == 0:
        return 0
    if ds == [] and a != 0:
        return "Failure"
    if ds[0] > a:
        return greedyMinChange(a, ds[1:])
    return add(quotient(a, ds[0]), greedyMinChange(remainder(a, ds[0]), ds[1:]))


def remainder(a, d):
    return a % d


def quotient(a, d):
    return a // d


def powIt(b, n):
    a = 1
    while n > 0:
        a = b * a
        n = n - 1
    return a


def main():
    print("def r([1,2,3,4,5,6,7,8,9,10]):       " + str(r([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    print("def prod(3,4):                       " + str(prod(3, 4)))
    print("def fastPow(2, 3):                   " + str(fastPow(2, 3)))
    print("def prodAccum(3, 4, 0):              " + str(prodAccum(3, 4, 0)))
    print("def minChange(74, [25, 10, 5, 1]):   " + str(minChange(74, [25, 10, 5, 1])))
    print("def greedyMinChange(10, [7, 5, 1]):  " + str(greedyMinChange(10, [7, 5, 1])))
    print("def powIt(2, 8):                     " + str(powIt(2, 8)))


if __name__ == '__main__':
    main()
