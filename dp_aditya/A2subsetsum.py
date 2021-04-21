
def is_subset(arr, s, i):

    if s == 0:
        return True

    if i == 0 and s != 0:
        return False

    if arr[i-1] <= s:
        return is_subset(arr, s-arr[i-1], i-1) or is_subset(arr, s, i-1)
    
    return is_subset(arr, s, i-1)


def is_subset_dp(arr, s, n):

    cache = [[False for j in range(s+1)] for i in range(n+1)]
    # cache[n][s]

    for i in range(n+1):
        for j in range(s+1):
            if i == 0 and j != 0:
                cache[i][j] = False
            if j == 0:
                cache[i][j] = True
            
    for i in range(n+1):
        for j in range(s+1):
            if arr[i-1] <= j:
                cache[i][j] = cache[i-1][j-arr[i-1]] or cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j]
    
    return cache[n][s]


# Driver code
arr = [3, 34, 4, 12, 5, 2]
s = 9
i = len(arr)
if is_subset_dp(arr, s, i):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")