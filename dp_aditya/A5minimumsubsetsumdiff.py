# write

def subset_sum(arr):
    n = len(arr)
    s = sum(arr)
    cache = [[False for j in range(s+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(s+1):
            if i == 0 and j != 0:
                cache[i][j] = False
            
            if j == 0:
                cache[i][j] = True
    
    for i in range(1, n+1):
        for j in range(1, s+1):
            if j >= arr[i-1]:
                cache[i][j] = cache[i-1][j-arr[i-1]] or cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j]

    subset_sum_possible = []
    for j in range(s+1):
        if cache[n][j]:
            subset_sum_possible.append(j)
    
    # To find the mininimum subset difference
    # s = s1 + s2
    # minimize abs(s2 - s1)
    # minimize abs(s2 - (s - s2))
    # minimize abs(2s2 - s)
    return min([abs(2*i - s) for i in subset_sum_possible]) 


arr = [1, 6, 11, 5]
print(subset_sum(arr))