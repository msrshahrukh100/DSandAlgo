# def knapsack(v, w, index, total_weight, total_value):
#     if total_weight == 0:
#         return total_value
    
#     if total_weight < 0:
#         return 0
    
#     if index >= len(v):
#         return total_value

#     if w[index] <= total_weight:
#         return max(
#             knapsack(v, w, index+1, total_weight - w[index], total_value + v[index]),
#             knapsack(v, w, index+1, total_weight, total_value)
#         )
#     return knapsack(v, w, index+1, total_weight, total_value)



# val = [60, 100, 120] 
# wt = [10, 20, 30] 
# W = 50
# print(knapsack(val, wt, 0, W, 0))

def knapsack(wt, val, W, n):

    if W == 0 or n == 0:
        return 0
    
    if wt[n-1] > W:
        return knapsack(wt, val, W, n-1)

    return max(
        val[n-1] + knapsack(wt, val, W - wt[n-1], n - 1),
        knapsack(wt, val, W, n - 1)
    )



def knapsack_dp():
    dp = [[-1 for j in range(W+1)] for i in range(n+1)]
    # Important 
    # dp[n+1][W+1]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    

    for i in range(1, n+1):
        for j in range(1, W+1):

            if wt[i-1] <= j:
                dp[i][j] = max(
                    val[i-1] + dp[i-1][j-wt[i-1]],
                    dp[i-1][j]
                )
            else:
                dp[i][j] = dp[i-1][j]





wt = [1, 2, 3, 4, 5]
val = [2, 3, 4, 5, 56]

W = 12




































