def knapSack(I, W):
    """
    KnapSack problem using dynamic programming
    :param I: Items
    :param W: Total Weight of tower
    :return: Max knapsack value
    """
    l = len(I)
    v = [[0 for x in range(W + 1)] for y in range(l)]
    for i in range(0, l):
        for w in range(1, W):
            if I[i][1] <= w:
                itemValue = v[i - 1][W]
                temp = I[i][0] + v[i - 1][W - I[i][1]]
                if temp > itemValue:
                    itemValue = temp
                v[i][w] = itemValue
    return v[l - 1][W - 1]


def knapSackContents(I, W):
    """
        KnapSack problem using dynamic programming
        :param I: Items
        :param W: Total Weight of tower
        :return: Max knapsack value and the contents of the knapsack
        """
    l = len(I)
    v = [[0 for x in range(W + 1)] for y in range(l)]
    for i in range(0, l):
        for w in range(1, W):
            if I[i][1] <= w:
                itemValue = v[i - 1][W]
                temp = I[i][0] + v[i - 1][W - I[i][1]]
                if temp > itemValue:
                    itemValue = temp
                v[i][w] = itemValue
    K = []
    for i in range(1, l):
        if v[i][W - 1] != 0:
            K.append(I[i])
    return v[l - 1][W - 1], K


def main():
    W = 70
    I = [(60, 10), (100, 20), (120, 30), (125, 35), (140, 40), (130, 44)]
    print(knapSack(I, W))
    print(knapSackContents(I, W))


if __name__ == '__main__':
    main()
