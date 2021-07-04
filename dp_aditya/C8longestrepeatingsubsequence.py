# find the length of the longest repeating subsequence in a string
# to solve this find the lcs between a and a but with the condition of i != j

# since we can't take the same elements in two different subsequences

s = "aabebcdd"
# "abd" and "abd" found twice


def lcs_dp(s1, s2):
    m = len(s2)
    n = len(s1)
    cache = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                cache[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1] and i != j:
                cache[i][j] = 1 + cache[i-1][j-1]
            else:
                cache[i][j] = max(
                    cache[i-1][j],
                    cache[i][j-1]
                )

    return cache[n][m]


print(lcs_dp(s, s))
