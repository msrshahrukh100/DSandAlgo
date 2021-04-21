def has_subset(arr, s, i):
    if s == 0:
        return True
    if i == 0 and s != 0:
        return False
    
    if arr[i-1] <= s:
        return has_subset(arr, s-arr[i-1], i-1) or has_subset(arr, s, i-1)
    
    return has_subset(arr, s, i-1)


def has_subset_dp(arr, s, n):
    cache = [[False for j in range(s+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(s+1):
            if j == 0:
                cache[i][j] = True
            if i == 0 and j != 0:
                cache[i][j] = False
    
    for i in range(1, n+1):
        for j in range(1, s+1):
            if arr[i-1] <= j:
                cache[i][j] = cache[i-1][j-arr[i-1]] or cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j]
    
    return cache[n][s]



def has_equal_partition(arr):
    s = sum(arr)
    if s % 2 == 0:
        return has_subset_dp(arr, int(s/2), len(arr))
    
    return False


# Driver code
arr = [3, 1, 5, 9, 12]
 
# Function call
if has_equal_partition(arr):
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")