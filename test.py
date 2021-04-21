def solution_recur(nums, index, s):
    if s == 0:
        return True
    
    if s < 0 or index < 0:
        return False
    
    if nums[index] <= s:
        return solution_recur(nums, index - 1, s - nums[index]) or solution_recur(nums, index - 1, s)
    
    return solution_recur(nums, index - 1, s)


# def solution_recur(l, index, s):
#     if s == 0:
#         return True

#     if index < 0 or s < 0:
#         return False
    
#     if l[index] > s:
#         return solution_recur(l, index - 1, s)
    
#     return any([
#         solution_recur(l, index - 1, s - l[index]),
#         solution_recur(l, index - 1, s)
#     ])

def solution_dp(nums, s):
    n = len(nums)
    # return cache[n][s]

    cache = [[False for i in range(s+1)] for j in range(n+1)]

    for j in range(s+1): cache[0][j] = False
    for i in range(n+1): cache[i][0] = True

    for i in range(1, n+1):
        for j in range(1, s+1):
            if j >= nums[i-1]:
                cache[i][j] = cache[i-1][j - nums[i-1]] or cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j]
    
    return cache[n][s]



nums = [23,13,11,7,6,5,5]
s = 70 // 2
# print(solution_recur(nums, len(nums) -1, s))
print(solution_dp(nums, s))