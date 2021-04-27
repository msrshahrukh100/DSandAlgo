def count_of_subset_with_given_diff(arr, given_diff):
    s = sum(arr)
    n = len(arr)

    cache = [[False for j in range(s+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(s+1):
            if j == 0:
                cache[i][j] = True
            if j != 0 and i == 0:
                cache[i][j] = False
    
    for i in range(1, n+1):
        for j in range(1, s+1):
            if arr[i-1] <= j:
                cache[i][j] = cache[i-1][j - arr[i-1]] or cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j]
    
    subset_sum_possible = []

    for j in range(s+1):
        if cache[n][j]:
            subset_sum_possible.append(j)
    print([2*i - s == given_diff for i in subset_sum_possible])
    return sum([2*i - s == given_diff for i in subset_sum_possible])

arr = [1, 1, 2, 3]
given_diff = 1
print(count_of_subset_with_given_diff(arr, given_diff))