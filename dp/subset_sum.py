

def subset_sum_recur(l, sum, cur_index):
    if cur_index < 0 or sum < 0:
        return False

    if sum == 0:
        return True
    
    return subset_sum_recur(l, sum, cur_index - 1) or subset_sum_recur(l, sum - l[cur_index], cur_index - 1)



def subset_sum_dp(l, sum):
    n = len(l)
    subset = [ [False for i in range(sum + 1)] for i in range(n + 1) ]

    for i in range(n+1):
        subset[i][0] = True
    
    for i in range(1, sum + 1):
        subset[0][i] = False
    
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if l[i - 1] > j:
                subset[i][j] = subset[i-1][j]
            if j >= l[i - 1]:
                subset[i][j] = subset[i-1][j] or subset[i - 1][j - l[i - 1]]
    
    return subset[n][sum]


l = [3, 34, 4, 12, 5, 2]
s = 30

print(subset_sum_recur(l, s, len(l) - 1))


print(subset_sum_dp(l, 30))