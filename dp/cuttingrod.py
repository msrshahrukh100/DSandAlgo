def solution_recur(p, index, size):
    if index < 0:
        return 0
    
    if size <= 0:
        return 0
    
    
    return max(
        p[index] + solution_recur(p, index - 1, size - (index + 1)),
        solution_recur(p, index - 1, size)
    )


    
arr = [1, 5, 8, 9, 10, 17, 17, 20] 
size = len(arr)
print(sum(arr))
print("Maximum Obtainable Value is", solution_recur(arr, size - 1, size))