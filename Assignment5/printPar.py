from math import inf


def extraSpaces(S, M, i, j):
    L = [len(s) for s in S]
    return M - j + 1 - sum(L[i: j + 1])


def badnessLine(S, M, i, j):
    a = extraSpaces(S, M, i, j)
    if a < 0:
        return inf
    else:
        return a


def minBad(S, M, i):
    if badnessLine(S, M, i, len(S) - 1) != inf:
        return 0
    minimum = inf
    for k in range(i + 1, len(S)):
        end = minBad(S, M, k)
        front = badnessLine(S, M, i, k - 1)
        if end > front:
            maximum = end
        else:
            maximum = front
        if minimum < maximum:
            minimum = minimum
        else:
            minimum = maximum
    return minimum


def minBadDynamic(S, M):
    a = [[0 for x in S] for y in S]
    for i in range(0, len(S)):
        a[i][i] = M - len(S[i])
        for j in range(i + 1, len(S)):
            a[i][j] = badnessLine(S, M, i, j)
    cost = [0 for x in S]
    for i in reversed(range(-1, len(S) - 1)):
        cost[i] = a[i][len(S) - 1]
        for j in reversed(range(i, len(S))):
            if a[i][j - 1] == inf:
                continue
            if cost[i] > cost[j] + a[i][j - 1]:
                cost[i] = cost[j] + a[i][j - 1]
    return cost[len(S) - 1]


def minBadDynamicChoice(S, M):
    a = [[0 for x in S] for y in S]
    for i in range(0, len(S)):
        a[i][i] = M - len(S[i])
        for j in range(i + 1, len(S)):
            a[i][j] = badnessLine(S, M, i, j)
    cost, choices = [0 for x in S], [0 for x in S]
    for i in reversed(range(-1, len(S) - 1)):
        cost[i] = a[i][len(S) - 1]
        choices[i] = len(S)
        for j in reversed(range(i, len(S))):
            if a[i][j - 1] == inf:
                continue
            if cost[i] > cost[j] + a[i][j - 1]:
                cost[i] = cost[j] + a[i][j - 1]
                choices[i] = j
    return cost, choices


def printParagraph(S, M):
    cost, choices = minBadDynamicChoice(S, M)
    if choices[-1] < max(choices):
        choices[-1] = choices[-2]
    i = 0
    j = 0
    paragraph = ''
    while j < len(S):
        j = choices[i]
        for k in range(i, j):
            paragraph = paragraph + S[k] + ' '
        paragraph = paragraph + '\n'
        i = j
    print(paragraph)


def main():
    S = "This is the paragraph we will use to implement the above functions." \
        "These functions will test for the badness of the lines in the paragraph" \
        " and print the line to about the given maximum limit." \
        " Let's check it out"
    S = S.split()
    print(minBadDynamicChoice(S, 50))
    printParagraph(S, 50)


if __name__ == '__main__':
    main()
