def rodcut_recur(lengths, costs, i, rod_length):
    # return the maximum profit possible
    if (i == 0 and rod_length != 0) or rod_length == 0:
        return 0
    
    if lengths[i-1] <= rod_length:
        return max(
            costs[i-1] + rodcut_recur(lengths, costs, i, rod_length - lengths[i-1]),
            rodcut_recur(lengths, costs, i-1, rod_length)
        )
    return rodcut_recur(lengths, costs, i-1, rod_length)



def rodcut_dp(lengths, costs, rod_length):
    n = len(lengths)
    cache = [[0 for j in range(rod_length+1)] for i in range(n+1)]


    for i in range(n+1):
        for j in range(rod_length+1):
            if i == 0 or j == 0:
                cache[i][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, rod_length+1):
            if lengths[i-1] <= j:
                cache[i][j] = max(
                    costs[i-1] + cache[i][j - lengths[i-1]],
                    cache[i-1][j]
                )
            else:
                cache[i][j] = cache[i-1][j]
    
    return cache[n][rod_length]


lengths = [1, 2, 3, 4, 5, 6, 7, 8]
arr = [1, 5, 8, 9, 10, 17, 17, 20]

size = len(arr)
print("Maximum Obtainable Value is", rodcut_recur(lengths, arr, size, size))

print("Maximum Obtainable Value is", rodcut_dp(lengths, arr, size))