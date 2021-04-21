def solution_recur(l, index, s):
    if s == 0:
        return True

    if index < 0 or s < 0:
        return False
    
    if l[index] > s:
        return solution_recur(l, index - 1, s)
    
    return any([
        solution_recur(l, index - 1, s - l[index]),
        solution_recur(l, index - 1, s)
    ])



def solution_dp(nums, s):
    l = len(nums)
    # NEVER use this multiplication below to create matrices, because in the outer multiplication
    # the same object is copied to all indices, so if you modify the first row all the other rows is 
    # modified, hence
    # ALWAYS use list comprehension to create matrices
    # cache = [[False] * (s + 1)] * (l + 1)
    cache =([ [False for i in range(s + 1)] for j in range(l + 1)]) 
    # print(cache1 == cache)

    for i in range(l + 1): cache[i][0] = True
    for j in range(1, s + 1): cache[0][j] = False

    for i in range(1, l + 1):
        for j in range(1, s + 1):
            if nums[i-1] > j:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j] or cache[i-1][j - nums[i - 1]]

    for i in cache:
        print(i)    
    return cache[l][s]


      
def isSubsetSum(set, n, sum): 
      
    subset =([[False for i in range(sum + 1)]  
            for i in range(n + 1)]) 

    for i in range(n + 1): 
        subset[i][0] = True
          
    for i in range(1, sum + 1): 
         subset[0][i]= False
              
    for i in range(1, n + 1): 
        for j in range(1, sum + 1): 
            if j<set[i-1]: 
                subset[i][j] = subset[i-1][j] 
            if j>= set[i-1]: 
                subset[i][j] = (subset[i-1][j] or 
                                subset[i - 1][j-set[i-1]]) 
      
    return subset[n][sum] 


l = [2, 5, 9] 
s = 4

# if (isSubsetSum(l, 5, s) == True): 
#     print("Found a subset with given sum") 
# else: 
#     print("No subset with given sum") 


if solution_dp(l, s): 
    print("Found a subset with given sum") 
else : 
    print("No subset with given sum")

# if solution_recur(l, 5, s): 
#     print("Found a subset with given sum") 
# else : 
#     print("No subset with given sum") 
