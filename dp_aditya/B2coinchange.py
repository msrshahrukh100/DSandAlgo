# find the number of ways in which you can make up an amount
# same as that of A4

# maximum number of ways in which you can make a sum with infinite
# supply of coins

def coin_chain(arr, i, s):

    if i == 0 and s != 0:
        return 0

    if s == 0:
        return 1

    if arr[i-1] <= s:
        return sum(
            coin_chain(arr, i, s - arr[i-1]),
            coin_chain(arr, i-1, s)
        )

    return coin_chain(arr, i-1, s)


def coin_change_dp(arr, s):
    n = len(arr)
    cache = [[0 for j in range(s+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(s+1):
            if i == 0 and s != 0:
                cache[i][j] = 0
            if s == 0:
                cache[i][j] = 1

    for i in range(1, n+1):
        for j in range(1, s+1):
            if arr[i-1] <= j:
                cache[i][j] = cache[i][j-arr[i-1]] + cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j]

    return cache[n][s]


arr = [1, 2, 3, 4]
s = 4
