def knapsack(v, w, index, total_weight, total_value):
    if total_weight <= 0:
        return total_value
    
    if index >= len(v):
        return total_value

    if w[index] <= total_weight:
        return max(
            knapsack(v, w, index+1, total_weight - w[index], total_value + v[index]),
            knapsack(v, w, index+1, total_weight, total_value)
        )
    return knapsack(v, w, index+1, total_weight, total_value)



val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
print(knapsack(val, wt, 0, W, 0))