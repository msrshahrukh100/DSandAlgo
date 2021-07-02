# find minimum number of coins requred to make the sum
# we have infinite supply of coins

import sys


def coin_change(arr, i, s):
    if i == 0 and s != 0:
        return sys.maxsize - 1

    if i == 1:
        if s % arr[i] == 0:
            return s // arr[i]
        else:
            return sys.maxsize - 1

    if s == 0:
        return 0

    if arr[i-1] <= s:
        return min(
            1 + coin_change(arr, i, s - arr[i-1]),
            coin_change(arr, i-1, s)
        )

    return coin_change(arr, i-1, s)


def coin_change_dp(arr, i, s):
    n = len(arr)
    cache = [[0 for j in range(s+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(s+1):
            if i == 0 and s != 0:
                cache[i][j] = sys.maxsize - 1
            if s == 0:
                cache[i][j] = 0

            if i == 1:
                if j % arr[i-1] == 0:
                    cache[i][j] = j // arr[i-1]
                else:
                    cache[i][j] = sys.maxsize - 1

    for i in range(1, n+1):
        for j in range(1, s+1):
            if arr[i-1] <= j:
                cache[i][j] = min(
                    1 + cache[i][j - arr[i-1]],
                    cache[i-1][j]
                )
            else:
                cache[i][j] = cache[i-1][j]

    return cache[n][s]
