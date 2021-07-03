
def lcs(s1, s2, i, j):
    if i == 0 or j == 0:
        return 0

    if s1[i-1] == s2[j-1]:
        return 1 + lcs(s1, s2, i-1, j-1)
    else:
        return max(
            lcs(s1, s2, i-1, j),
            lcs(s1, s2, i, j-1)
        )


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
            if s1[i-1] == s2[j-1]:
                cache[i][j] = 1 + cache[i-1][j-1]
            else:
                cache[i][j] = max(
                    cache[i-1][j],
                    cache[i][j-1]
                )

    def print_lcs():
        '''
            Prints the longest common subsequence
        '''
        i = n
        j = m
        longest_common_subsequence = ""
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                longest_common_subsequence += s2[i-1]
                i -= 1
                j -= 1
            else:
                if cache[i-1][j] > cache[i][j-1]:
                    i -= 1
                else:
                    j -= 1

        print(longest_common_subsequence[::-1])

    print_lcs()

    return cache[n][m]


s1 = "abcdgh"
s2 = "abedfhr"

# print(lcs(s1, s2, len(s1), len(s2)))
print(lcs_dp(s1, s2))
