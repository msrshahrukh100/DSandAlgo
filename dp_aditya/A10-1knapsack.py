


def find_max_profit(weight, cost, max_weight, i):

    if i == 0 or max_weight == 0:
        return 0

    if weight[i-1] <= max_weight:
        return max(
            cost[i-1] + find_max_profit(weight, cost, max_weight-weight[i-1], i-1),
            find_max_profit(weight, cost, max_weight, i-1)
        )
    
    return find_max_profit(weight, cost, max_weight, i-1)


def find_max_profit_dp(weight, cost, max_weight, n):
    cache = [[0 for i in range(max_weight+1)] for j in range(n+1)]
    # cache[n][max_weight]

    for i in range(n+1):
        cache[i][0] = 0
    for j in range(max_weight+1):
        cache[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, max_weight+1):
            if weight[i-1] <= j:
                cache[i][j] = max(
                    cost[i-1] + cache[i-1][j-weight[i-1]],
                    cache[i-1][j-weight[i-1]]
                )
            else:
                cache[i][j] = cache[i-1][j-weight[i-1]]

    return cache[n][max_weight]
    


cost = [60, 100, 120]
weight = [10, 20, 30]
max_weight = 50
i = len(cost)
print(find_max_profit(weight, cost, max_weight, i))
print(find_max_profit_dp(weight, cost, max_weight, i))