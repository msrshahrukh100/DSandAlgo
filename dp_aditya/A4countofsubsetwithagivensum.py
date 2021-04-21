
def count_of_subset_sum(arr, i, s):

    if s == 0:
        return 1
    
    if i == 0 and s != 0:
        return 0

    if arr[i-1] <= s:
        return count_of_subset_sum(arr, i-1, s-arr[i-1]) + count_of_subset_sum(arr, i-1, s)
    
    return count_of_subset_sum(arr, i-1, s)


def count_of_subset_sum_dp(arr, n, s):
    cache = [[0 for j in range(s+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(s+1):
            if j == 0:
                cache[i][j] = 1
            elif i == 0 and j != 0:
                cache[i][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, s+1):
            if arr[i-1] <= j:
                cache[i][j] = cache[i-1][j-arr[i-1]] + cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j]
    
    for i in range(n+1):
        print(cache[i])
    
    return cache[n][s]


arr = [ 3, 3, 3, 3 ]
n = len(arr)
s = 6

print(count_of_subset_sum_dp(arr, n, s));