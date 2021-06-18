'''
https://leetcode.com/problems/house-robber/
'''

def rob(nums):
    size = len(nums)
    if size == 0: return 0
    cash = [0 for i in range(size)]
      
    for i in range(size):
        if i == 0: cash[0] = nums[0]
        elif i ==1: cash[1] = max(nums[0], nums[1])
        else: cash[i] = max(nums[i] + cash[i-2], cash[i-1])
      
    return cash[size-1]
    
print(rob([2,7,9,3,1]))