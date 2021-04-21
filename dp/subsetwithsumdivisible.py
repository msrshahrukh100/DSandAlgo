def subset_divisible_dp(nums, m):
    pass

def subset_divisible_recur(nums, s, m, index):
    if s != 0 and s % m == 0:
        return True
    
    if index < 0:
        return False
    
    return any([
        subset_divisible_recur(nums, s + nums[index], m, index - 1),
        subset_divisible_recur(nums, s, m, index - 1),
    ])


arr = [1, 7, 3, 2]
n = len(arr) 
m = 11
print("YES") if(subset_divisible_recur(arr, 0, m, n - 1)) else print("NO") 

