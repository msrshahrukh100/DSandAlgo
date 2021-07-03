import sys

answer = -sys.maxsize


def lcs(s1, s2, i, j, size):
    # TODO: recursive implemention
    if i == 0 or j == 0:
        return 0

    if s1[i-1] == s2[j-1]:
        return 1 + lcs(s1, s2, i-1, j-1)

    return "nil"


def lcs_dp(s1, s2):
    m = len(s1)
    n = len(s2)

    cache = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                cache[i][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):

            if s1[i-1] == s2[j-1]:
                cache[i][j] = 1 + cache[i-1][j-1]
            else:
                cache[i][j] = 0

    return max([max(i) for i in cache])


s1 = "abcde"
s2 = "abfce"

print(lcs_dp(s1, s2))
