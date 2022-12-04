'''
https://leetcode.com/problems/longest-valid-parentheses/description/
'''

def longestValidParentheses(A):
    n = len(A)
    dp = [0]*n
    res = 0
    for i in range(1,n):
        if A[i] == ")":
            if  A[i-1] == "(":
                dp[i] = dp[i-2] + 2
            else: 
                if i-dp[i-1]-1 >= 0 and A[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-dp[i-1]-2] + 2 + dp[i-1]
            res = max(res,dp[i])
    return res

print(longestValidParentheses(")()())"))