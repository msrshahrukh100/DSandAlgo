

def lcs(a, b, i, j):

    if i == 0 or j == 0:
        return 0

    if a[i-1] == b[j-1]:
        return 1 + lcs(a, b, i-1, j-1)

    return max(
        lcs(a, b, i-1, j),
        lcs(a, b, i, j-1)
    )


def lcs_dp(a, b):
    m = len(a)
    n = len(b)

    cache = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                cache[i][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                cache[i][j] = 1 + cache[i-1][j-1]
            else:
                cache[i][j] = max(
                    cache[i-1][j],
                    cache[i][j-1]
                )

    return cache[m][n]


def answer(a, b):
    l = lcs_dp(a, b)
    result = len(b) + len(a) - 2 * l
    return result


a = "heap"
b = "pea"

print(answer(a, b))
