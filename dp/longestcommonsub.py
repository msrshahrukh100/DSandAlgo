def lcs_recursive(a, b, n, m):

    if n < 0 or m < 0:
        return 0
    
    if a[n] == b[m]:
        return 1 + lcs_recursive(a, b, n-1, m-1)
    
    return max(lcs_recursive(a, b, n, m-1), lcs_recursive(a, b, n-1, m))


def lcs_dp(a, b):

    memo = [[0] * (len(a) + 1)] * (len(b) + 1)
    # return  memo[n][m]
    

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            print(i, j)
            if i == 0 or j == 0:
                memo[i][j] = 0
            elif a[i-1] == b[j-1]:
                memo[i][j] = 1 + memo[i-1][j-1]
            else:
                memo[i][j] = max(
                    memo[i-1][j],
                    memo[i][j-1]
                )
    
    for i in memo:
        print(i)
    
    return memo[len(a)][len(b)]




X = "shahrukh"
Y = "marukh"

# print(lcs_recursive(X, Y, len(X) - 1, len(Y) - 1))

print(lcs_dp(X, Y))