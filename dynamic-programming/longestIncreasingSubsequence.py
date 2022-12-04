'''
https://leetcode.com/problems/longest-increasing-subsequence/description/
'''

def lengthOfLIS(nums):
    n = len(nums)
    # def lis(i):
    #   if i == n-1:
    #     return 1
    #   ans = 1
    #   for j in range(i+1,n):
    #     if nums[i] < nums[j]:
    #       ans = max(ans,1+lis(j))
    #       #print("enter"+str(i)+str(j), nums[i], nums[j], ans)
    #   return ans
    # ans = 1
    # for i in range(n):
    #   ans = max(ans,lis(i))
    # return ans
    dp = [1]*n
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i],1+dp[j])
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))